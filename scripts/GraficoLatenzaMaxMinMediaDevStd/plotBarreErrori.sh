#!/bin/bash

#fileBind filePdns fileTech
bind=$(grep "Average Latency (s)" $1 | head -1 | sed 's/Average Latency (s)://g' | sed 's/(min//g' | sed 's/, max//g' | sed 's/)//g')
pdns=$(grep "Average Latency (s)" $2 | head -1 | sed 's/Average Latency (s)://g' | sed 's/(min//g' | sed 's/, max//g' | sed 's/)//g')
tech=$(grep "Average Latency (s)" $3 | head -1 | sed 's/Average Latency (s)://g' | sed 's/(min//g' | sed 's/, max//g' | sed 's/)//g')
echo $bind;
echo $pdns;
echo $tech;

bindStddev=$(grep "Latency StdDev (s):" $1 | sed 's/Latency StdDev (s):[ ]*//g')
pdnsStddev=$(grep "Latency StdDev (s):" $2 | sed 's/Latency StdDev (s):[ ]*//g')
techStddev=$(grep "Latency StdDev (s):" $3 | sed 's/Latency StdDev (s):[ ]*//g')

python3 plotBarreErrori2.py $bind $pdns $tech $bindStddev $pdnsStddev $techStddev $4 $5
