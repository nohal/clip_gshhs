clip_gshhs
==========

A clone of http://dev.v-l-m.org/vlmtools/wiki/clip_gshhs tool, modified to produce polygons version 220 (just the version number is changed) for use with OpenCPN and qtVlm

Unzip the GSHHG data (native binary from http://www.soest.hawaii.edu/pwessel/gshhg/) to gshhs subfolder and run ./clip_all.sh

If you can afford a 5GB ramdisk, you will save A LOT of time as hundreds of thousands of files are created and used in the bd subfolder

mount -t tmpfs -o size=5GB tmpfs bd
