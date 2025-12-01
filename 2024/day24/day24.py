'''
    Advent of Code 2024
    https://adventofcode.com/2024/day/24
'''

# input from website
sample_input = False
input = 'day24_sample.txt' if sample_input else 'day24.txt'
with open(input, 'r') as f:
    data = [section.splitlines() for section in f.read().split("\n\n")]


values = {d[:3]: int(d[-1]) for d in data[0]}

for k, v in values.items():
    print(k, v)

gates = {}
for d in data[1]:
    a, b = d.split(" -> ")
    a1, op, a2 = a.split()
    gates[b] = [a1, op, a2]

print()

for k, v in gates.items():
    print(k, v)

all_zs = sorted(set(v for v in (list(values.keys()) +
                                list(gates.keys())) if v[0] == "z"))


def solve(output):
    if output in values:
        return values[output]
    a1, op, a2 = gates[output]
    if op == "AND":
        return solve(a1) & solve(a2)
    if op == "OR":
        return solve(a1) | solve(a2)
    if op == "XOR":
        return solve(a1) ^ solve(a2)


result = ""
for z in all_zs:
    result += str(solve(z))

print(int(str(result[::-1]), 2))


# for part 2, create graphviz visualisation
# https://www.devtoolsdaily.com/graphviz/

print()
print()
print("digraph G {")

print("""
    subgraph cluster_0 {
        style=filled;
        color=lightgrey;
        node [style=filled,color=white];
        label = "Start nodes X" """)
for z in all_zs:
    print(f"\t{z}")
print("}")

print()
print("""
    subgraph cluster_1 {
        style=filled;
        color=lightgrey;
        node [style=filled,color=white];
        label = "End nodes Z" """)
for k in values:
    print(f"\t{k}")
print("}")

print()
print("\tnode [shape=rect];")
print()

for k, v in gates.items():
    print(f"\t{k}{v[1]} -> {k}")
    print(f"\t{v[0]} -> {k}{v[1]}")
    print(f"\t{v[2]} -> {k}{v[1]}")

print("}")
