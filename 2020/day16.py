'''
    Advent of Code Day 16
    https://adventofcode.com/2020/day/16
'''

# input from website in raw format
data = []
with open('day16.input.txt', 'r') as f:
    data = f.read().splitlines()

sample_data = [
	"class: 1-3 or 5-7",
	"row: 6-11 or 33-44",
	"seat: 13-40 or 45-50",
	"",
	"your ticket:",
	"7,1,14",
	"",
	"nearby tickets:",
	"7,3,47",
	"40,4,50",
	"55,2,20",
	"38,6,12"
]

sample_data2 = [
	"class: 0-1 or 4-19",
	"row: 0-5 or 8-19",
	"seat: 0-13 or 16-19",
	"",
	"your ticket:",
	"11,12,13",
	"",
	"nearby tickets:",
	"3,9,18",
	"15,1,5",
	"5,14,9"
]


# data = sample_data2

rules_for_ticket_fields = {}
my_ticket = []
other_tickets = []
valid_tickets = []

raw_rules = data[0:data.index("")]
my_ticket = [ int(x) for x in data[len(raw_rules)+2].split(",") ]
other_tickets = [ [ int(y) for y in x.split(",")] for x in data[len(raw_rules)+5:] ]

for rule in raw_rules:
	rule = rule.replace(" ", "")
	rule_name, rule = rule.split(":")
	rules = []
	for x in rule.split("or"):
		rules.append([int(y) for y in x.split("-")])
	rules_for_ticket_fields[rule_name] = rules

# Puzzle #1
def check_ticket(ticket):
	for number in ticket:
		valid = False
		for rule in rules_for_ticket_fields.values():
			if (rule[0][0] <= number and number <= rule[0][1]) or (rule[1][0] <= number and number <= rule[1][1]):
				valid = True
		if not valid:
			return number
	valid_tickets.append(ticket)
	return 0


# using other_tickets.copy() so that other_tickets will contain only valid tickets
print(f"The answer for puzzle #1 is: {sum(check_ticket(ticket) for ticket in other_tickets)}.")


field_order = {}

def check_rule(tickets, rules):
	while rules != {}:
		rule = rules.popitem()
		rule_name = rule[0]
		rule_range = rule[1]

		for i in range(0, len(tickets[0])):
			found_rule = True

			for j in range(0, len(tickets)):
				number = tickets[j][i]
				if not ((rule_range[0][0] <= number and number <= rule_range[0][1]) or (rule_range[1][0] <= number and number <= rule_range[1][1])):
					found_rule = False
					break
			
			if found_rule:
				# print(f"found field \t{i} valid for rule \t{rule_name}")
				if rule_name in field_order:
					field_order[rule_name].append(i)
				else:
					l = []
					l.append(i)
					field_order[rule_name] = l
				# break

# the method check rules leaves the dictionary field_order with the rule name and the corresponding ticket columns that are valid
# it is then necessary to find the rule with only one corresponding valid ticket column
# since there are multiple valid ticket columns per rule, one needs to eliminate from the bottom up

check_rule(valid_tickets, rules_for_ticket_fields)
field_order_sorted = { k:v for k,v in sorted(field_order.items(), key=lambda v: len(v[1])) }

remove_items = []
oh_boy = {}

for key, value in field_order_sorted.items():
	rule_name = key
	for x in remove_items:
		value.remove(x[0])
	rule_value = value
	remove_items.append(value)
	oh_boy[key] = value[0]

product = 1
for k,v in oh_boy.items():
	if k.startswith("departure"):
		product *= my_ticket[v]

print(product)