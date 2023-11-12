#/bin/bash

function funcinput() {
    clear
    read -n 1 -p "Please copy/paste the text into oldnorse_input.txt. Type y when ready. " userinput
	case "$userinput" in
        "y") python3 singlerun.py;;
        *) funcinput;;
    esac
}
###MAIN RUN###
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
cat oldnorse_input.txt > "./texts/$foldername/ON-Lat.txt"
cat FINAL.txt > "./texts/$foldername/ON-YF.txt"
mv *.txt "./texts/$foldername/notes/"
touch oldnorse_input.txt