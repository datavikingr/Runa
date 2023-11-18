#!/bin/bash

read -p 'What is the name of the directory? ' foldername
python3 tools/input_processing.py
clear
python3 tools/asf_transliterate.py
cat english_input.txt > "./texts/$foldername/EN-Lat.txt"
cat "10-ASF-FINAL.txt" > "./texts/$foldername/EN-ASF.txt"
mv *.txt "./texts/$foldername/notes/"
touch ./english_input.txt
cd ./texts/$foldername
python3 ../../tools/post_processing.py