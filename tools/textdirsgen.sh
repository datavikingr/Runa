#!/bin/bash

remainingtexts=("alvíssmál" "baldrsdraumar" "rígsþula" "hyndluljóð" "helgakviða-hundingsbana-1" "helgakviða-hjǫrvarðssonar" "helgakviða-hundingsbana-2" "frá-dauða-sinfjǫtla" "grípisspá" "reginsmál" "fáfnismál" "sigrdrífumál" "brot-af-sigurðarkviðu" "guðrúnarkviða-1" "sigurðarkviða-in-skamma" "helreið-brynhildar" "guðrúnarkviða-2" "guðrúnarkviða-3" "oddrúnargrátr" "atlakviða" "atlamál-in-grœnlenzku" "guðrúnarhvǫt" "hamðismál" "grottasǫngr" "grógaldr" "fjǫlsvinnsmál")
docs=("ON-Lat.txt" "ON-YF.txt" "EN-Lat.txt" "EN-ASF.txt")
textnumber=11

for text in ${remainingtexts[@]}; do
  foldername="$textnumber-${text}"
  #TESTING: echo $foldername
  mkdir $foldername
  mkdir notes
  mv notes $foldername
  ((textnumber+=1))
  for doc in ${docs[@]}; do
    touch $doc
    mv $doc $foldername
  done
done