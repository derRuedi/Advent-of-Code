'''
    Advent of Code 2023
    https://adventofcode.com/2023/day/20
'''
import json
from collections import deque
from icecream import ic


# input from website
sample_input = False
input = 'day20_sample.txt' if sample_input else 'day20.txt'
with open(input, 'r') as f:
    data = [line.split(" -> ") for line in f.read().splitlines()]

modules = {}
for name, destination in data:
    if name == "broadcaster":
        modules[name] = {"type": "broadcaster"}
        modules[name]["destination"] = destination.split(", ")
    else:
        modules[name[1:]] = {
            "type": "conjunction" if name[0] == "&" else "flip-flop"}
        modules[name[1:]]["destination"] = destination.split(", ")
        if modules[name[1:]]["type"] == "flip-flop":
            modules[name[1:]]["is_on"] = False

conjunction_modules = [
    k for k, v in modules.items() if modules[k]["type"] == "conjunction"]

for cm in conjunction_modules:
    connected_input_modules = [
        k for k, v in modules.items() if cm in modules[k]["destination"]]
    modules[cm]["connected_input_modules"] = {}
    for cim in connected_input_modules:
        modules[cm]["connected_input_modules"][cim] = "low"


queue = deque()
pulse_count = {"low": 0, "high": 0}


def button_module():
    queue.append(("button", "broadcaster", "low"))

    while len(queue) > 0:
        sender, receiver, pulse_type = queue.popleft()

        # ic(f"{sender} -{pulse_type}-> {receiver}")

        pulse_count[pulse_type] += 1

        if receiver not in modules:
            continue

        if modules[receiver]["type"] == "flip-flop":
            if pulse_type == "low":
                if modules[receiver]["is_on"]:
                    new_pulse = "low"
                else:
                    new_pulse = "high"
                tmp = [queue.append((receiver, i, new_pulse))
                       for i in modules[receiver]["destination"]]
                modules[receiver]["is_on"] = not modules[receiver]["is_on"]
        elif modules[receiver]["type"] == "conjunction":
            modules[receiver]["connected_input_modules"][sender] = pulse_type
            if all(cim == "high" for cim in modules[receiver]["connected_input_modules"].values()):
                new_pulse = "low"
            else:
                new_pulse = "high"
            [queue.append((receiver, i, new_pulse))
             for i in modules[receiver]["destination"]]
        else:
            [queue.append((receiver, i, pulse_type))
             for i in modules[receiver]["destination"]]


known_states = set()
pulses_before = None
for i in range(1000):
    pulses_before = dict(pulse_count)
    button_module()
    if json.dumps(modules) in known_states:
        print(
            f"There is a cycle - we can skip ahead after just {i} button presses, the result is:")
        print(round(1000 / len(known_states) *
              pulses_before["low"] * 1000 / len(known_states) * pulses_before["high"]))
        break
    known_states.add(json.dumps(modules))

# if no cycle has been detected
if i == 1000-1:
    print((pulse_count["low"]) * (pulse_count["high"]))


# for part 2, create graphviz visualisation
# https://www.devtoolsdaily.com/graphviz/
print()
print()
print()
conjunctions = [k for k, v in modules.items() if modules[k]
                ["type"] == "conjunction"]
flip_flops = [k for k, v in modules.items() if modules[k]["type"]
              == "flip-flop"]

print("digraph G {")
for c in conjunctions:
    print(f"{c} [shape=circle]")

for ff in flip_flops:
    print(f"{ff} [shape=box]")

with open(input, 'r') as f:
    data = f.read().splitlines()

for line in data:
    if line.startswith("broadcaster"):
        print(line)
    else:
        print(line[1:])

print("}")

# check graphviz_diagram.png

# Reason: In order for rx to receive a low, each of the 4 sub-graphs conjunctions must switch
# for that to happen, each flip flop connected to the conjunction of the sub-graph must be on, whereas the ones not connectes must be off
# counted for each subgraph and converted to decimal, one will get the periodicity of that particular sub-graph
# all periodicities combined (lcm) yields the result

# a = "101011011111"
# bin_to_dec(a[::-1])
# 4021
# b = "110100001111"
# bin_to_dec(b[::-1])
# 3851
# c = "101001001111"
# bin_to_dec(c[::-1])
# 3877
# d = "100010111111"
# bin_to_dec(d[::-1])
# 4049

# 4021 * 3851 * 3877 * 4049
# 243081086866483
