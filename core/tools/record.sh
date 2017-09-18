#!/bin/bash

if [ -z $1 ]; then
  echo "Usage: $0 path"
  exit
fi

path=$1
mkdir $path

echo "Files will be saved in $path"

echo $(tput lines) $(tput cols) > $path/dims
script -q -t $path/typescript 2> $path/timeline

