#!/bin/bash

# encode a set of .png files into a Firefox-compatible webm file (usable in the template)
# the files are named 'toto.0000.png', 'toto.0001.png'...

ffmpeg -i output.%04d.png -c:v libvpx -crf 10 -b:v 1M -c:a libvorbis output.webm
