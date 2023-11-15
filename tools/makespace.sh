#!/bin/bash

#RUN FROM ROOT OF PROJECT


# Poll directory for subdirectories and store in a list variable
directories=($(find texts -maxdepth 1 -type d))

# Iterate over the list of directories
for dir in "${directories[@]}"; do
    echo "Processing directory: $dir"

    # Change directory
    cd "$dir" || exit

    # Rename files
    if [ -e "EN-ASF.txt" ]; then
        mv "EN-ASF.txt" "EN-ASF-Bellows.txt"
        echo "EN-ASF.txt renamed to EN-ASF-Bellows.txt"
    fi

    if [ -e "EN-Lat.txt" ]; then
        mv "EN-Lat.txt" "EN-Lat-Bellows.txt"
        echo "EN-Lat.txt renamed to EN-Lat-Bellows.txt"
    fi

    # Return to the original directory
    cd - || exit
done