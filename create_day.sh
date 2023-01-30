#!/bin/bash

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
  year=$2
fi

day=$1
dir="$year/day$1"

if [[ -d $dir ]]
then
  echo "Directory '$dir' already exists, exiting."
else
  echo "Create AoC directory and skeleton files; have fun coding!"
  mkdir -p "$dir"
  cp -R template/ "$dir"
  cd "$dir"
  sed -i "" -e "s/{day}/$day/" -e "s/{year}/$year/g" "dayX.py"
  mv "dayX.py" "day$day.py"
  mv "description_dayX.txt" "description_day$day.txt"
fi

code *


