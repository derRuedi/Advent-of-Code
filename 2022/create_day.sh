day=$1
dir="day$1"

if [[ -d $dir ]]
then
  echo "Directory '$dir' already exists, exiting."
else
  echo "Create AoC directory and skeleton files; have fun coding!"
  cp -R dayX/ "$dir"
  cd "$dir"
  sed "s/{day}/$day/" "dayX.py" > "day$day.py"
  rm "dayX.py"
  mv "description_dayX.txt" "description_day$day.txt"
fi

code *


