#/bin/bash

function funcinput() {
    clear
    read -n 1 -p "What language is the text in? e -English; n -Old Norse; b -both; * -ask me again; " userinput
    echo
    case "$userinput" in
    "n")
        clear
        python3 tools/singlerun.py
        cat oldnorse_input.txt > "./texts/$foldername/ON-Lat.txt"
        cat "11-YF-FINAL.txt" > "./texts/$foldername/ON-YF.txt"
        mv *.txt "./texts/$foldername/notes/"
        touch oldnorse_input.txt
        touch english_input.txt
        ;;
    "e") 
        clear
        python3 tools/asf_transliterate.py
        cat english_input.txt > "./texts/$foldername/EN-Lat.txt"
        cat "10-ASF-FINAL.txt" > "./texts/$foldername/EN-ASF.txt"
        mv *.txt "./texts/$foldername/notes/"
        touch oldnorse_input.txt
        touch english_input.txt
        ;;
    "b") 
        clear
        python3 tools/singlerun.py
        python3 tools/asf_transliterate.py
        cat oldnorse_input.txt > "./texts/$foldername/ON-Lat.txt"
        cat "11-YF-FINAL.txt" > "./texts/$foldername/ON-YF.txt"
        cat english_input.txt > "./texts/$foldername/EN-Lat.txt"
        cat "10-ASF-FINAL.txt" > "./texts/$foldername/EN-ASF.txt"
        mv *.txt "./texts/$foldername/notes/"
        touch oldnorse_input.txt
        touch english_input.txt
        ;;
    *) 
        funcinput
        ;;
    esac
}

### Main ###
read -p 'Does the directory already exist? y/* ' testdirectoryexists
if [ $testdirectoryexists=="y" ]; then
    read -p 'What is the name of the directory? ' foldername
else
    read -p 'What is the name of the text? ' textname
    read -p 'What was the last serial number used in the texts directory? ' textnum
    ((textnum+=1))
    foldername="$textnum"-"${textname,,}"
fi
testfilepath="./texts/$foldername/ON-Lat.txt"
if [ ! -e "$testfilepath" ]; then
    cd texts
    mkdir $foldername
    cd $foldername
    mkdir notes
    touch ON-Lat.txt
    touch ON-YF.txt
    touch EN-Lat.txt
    touch EN-YF.txt
    cd ../..
fi
funcinput