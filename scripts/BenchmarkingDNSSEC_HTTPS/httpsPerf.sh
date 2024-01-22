#!/bin/bash
calc(){ awk "BEGIN { print $* }"; }


#echo $line
start_time=$(date +%N)
kdig +https-get $1 @127.0.0.1 +short >> /dev/null
#nslookup www.google.it
stop_time=$(date +%N)

nanosec=$(echo "$stop_time - $start_time" | bc)
#echo $nanosec
echo -n $line" "
calc $nanosec/1000000000

