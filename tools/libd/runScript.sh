#!/bin/bash

for apkSample in `ls $1`; do
    echo "Running analysis on $1/$apkSample"
    python libd_v_0.0.1.py $1/$apkSample decompose/ manuallyapproach/whitelist
done
