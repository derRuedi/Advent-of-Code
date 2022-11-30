'''
    Advent of Code Day 19
    https://adventofcode.com/2020/day/19
'''

# input from website in raw format
data = []
with open('day19.input.txt', 'r') as f:
    data = f.read().splitlines()

sample_data = [
    '0: 4 1 5',
    '1: 2 3 | 3 2',
    '2: 4 4 | 5 5',
    '3: 4 5 | 5 4',
    '4: "a"',
    '5: "b"',
    '',
    'ababbb',
    'bababa',
    'abbbab',
    'aaabbb',
    'aaaabbb'
]

def extract_rules_and_messages(data):
    rules = {}
    rules_raw = data[0:data.index("")]
    for rule in rules_raw:
        rule_no, rule_string = rule.split(": ")
        rules[rule_no] = rule_string
    messages = data[data.index("")+1:]
    return rules, messages

def count_valid_messages(data):
    rules, messages = extract_rules_and_messages(data)
    

data = sample_data
    

# count_valid_messages(sample_data)



import re

rules = {}
rules_raw = data[0:data.index("")]
for rule in rules_raw:
    rule_no, rule_string = rule.split(": ")
    rules[rule_no] = rule_string.replace('"', '')
messages = data[data.index("")+1:]

def sub_rules(expr):
    print("called: ", expr)
    if expr.isalpha():
        return expr
    elif expr in rules:
        return rules[expr]
    # match the first digit in expression
    elif re.match("^(.*?) (\d+) (.*)$", expr):
        
        [left, digit, right] = re.match("^(.*?)(\d+)(.*)$", expr).groups()
        if left == None and right == None:
            return sub_rules(digit)
        else:
            return sub_rules(left + "[" + sub_rules(digit) + "]" + right)
    else:
        return expr

print(sub_rules("4 1 5"))