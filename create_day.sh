#!/bin/bash

# export AOC_SESSION=53616c7465645f5f535c69eb398ede99dc57ebcc7ff29ffb0f1fb7a0e578078b360539d00626f7df34720aaf704c99951c5183ef3e67c74e63a46c23977ee975


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
