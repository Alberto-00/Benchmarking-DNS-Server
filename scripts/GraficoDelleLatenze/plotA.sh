#!/bin/bash

grep  ">" $1 | sed "s/> [a-zA-Z]* [_a-zA-Z0-9.-]* A //g" | tr '\n' ',' >> latenze_$1.txt
grep  ">" $2 | sed "s/> [a-zA-Z]* [_a-zA-Z0-9.-]* A //g" | tr '\n' ',' >> latenze_$2.txt
grep  ">" $3 | sed "s/> [a-zA-Z]* [_a-zA-Z0-9.-]* A //g" | sed "s/> T [0-9a-zA-Z.-]* A//g" | tr '\n' ',' | sed 's/,,//g' | sed 's/^.//' >> latenze_$3.txt
python3 plotA.py latenze_$1.txt latenze_$2.txt latenze_$3.txt $4 $5 $6
