#!/bin/bash

# Collate ON-Lat.txt files into a single master file
find texts -name 'ON-Lat.txt' -exec cat {} + > edda.txt

# Count word frequency and save results to MasterCount.txt
python3 count_words.py edda.txt > MasterCount.txt