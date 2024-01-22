#!/bin/bash


sed 's/Bin [0-9]*: Range [.0-9]* - [.0-9]* ms, Richieste://g' $1 | tr '\n' ',' | sed 's/ ,/,/g' | sed 's/, /,/g' >> answercount_$1.txt
echo -n '"' >> latenze_$1.txt
sed 's/Bin [0-9]*: Range //g' $1 | sed 's/ ms, Richieste: [0-9]*//g' | tr '\n' 'A' | sed 's/A/","/g'  >> latenze_$1.txt

python3 plotG_DNSSEC_HTTPS.py answercount_$1.txt latenze_$1.txt $2 $3
