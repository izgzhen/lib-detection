#!/bin/bash

for apkSample in `ls $1`; do
    echo "Running analysis on $1/$apkSample" 
    python LiteRadar/LiteRadar/literadar.py $1/$apkSample
done