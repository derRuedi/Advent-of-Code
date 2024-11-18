#!/bin/bash

# export AOC_SESSION=53616c7465645f5fd8c7c6825cf548242e4963c09cff82070279cc5be4c31fee2d1c28f86fd31866d8214bc98293eb6506c6eda64de8abb90a09c985e517ec8d


TEMPLATE=`cat <<-EOM
'''
    Advent of Code {year}
    https://adventofcode.com/{year}/day/{day}
'''

# input from website
sample_input = False
input = 'day{day}_sample.txt' if sample_input else 'day{day}.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()

for line in data:
    print(line)
EOM`


if [ $# -lt 1 ] || [ $# -gt 2 ]
then
  echo $#
  echo "Usage: '$0 {day} [{year}]'. Day in 'dd' and year in 'yyyy'."
  exit -1
fi

# one argument, create day template for current year
if [ $# -eq 1 ]
then
  year=`date +"%Y"`
else
  year="$2"
fi

day="$1"
dir="${year}/day${day}"

if [[ -d $dir ]]
then
  echo "Directory '$dir' already exists, exiting."
else
  echo "Create AoC directory and skeleton files; have fun coding!"
  mkdir -p "$dir"
  cd "$dir"
  # create the python file
  echo "$TEMPLATE" | sed -e "s/{day}/${day}/g" -e "s/{year}/${year}/g" > "day${day}.py"
  
  # create the description file - unfortunately it still has to be filled manually
  touch "day${day}_description.txt"
  # create the input data file so that it exists no matter what
  touch "day${day}.txt"
  # if possible, get the data
  aocd "$day" "$year" > "day${day}.txt"
  # create the description file so that it exists no matter what
  touch "day${day}_sample.txt"
  # if possible, get the data
  aocd "$day" "$year" --example-parser simple >> "day${day}_sample.txt"
  # open everything in VS Code
  code ../../
fi
