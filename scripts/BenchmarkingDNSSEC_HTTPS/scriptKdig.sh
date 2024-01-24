#!/bin/bash
calc(){ awk "BEGIN { print $* }"; }

for line in `cat $1 | sed 's/ A//g'`
do

./dnssec_httpsPerf.sh $line &
if [ $(jobs | wc -l) == 100 ]
then 
    sleep 1 
fi
done
