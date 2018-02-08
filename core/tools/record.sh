#!/bin/bash

#116x34

if [ -z $1 ]; then
  echo "Usage: $0 path"
  exit
fi


path=$1
mkdir $path

echo "Files will be saved in $path"
echo "##### Best dims for presentation: 34 lines, 116 cols #####"

echo $(tput lines) $(tput cols) > $path/dims
script -q -t $path/typescript 2> $path/timeline

