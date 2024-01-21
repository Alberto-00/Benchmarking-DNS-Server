
#!/bin/bash

#commento
grep "Latency bucket" $1 -A 1000000000 >> buckets_$1.txt

sed 's/  [.0-9]* - [.0-9]*:  /''/g' buckets_$1.txt | sed 's/Latency bucket (s):   answer count/''/g' | sed 's/Connection Statistics:/''/g' | sed 's/Reconnections:/''/g' | sed 's/[0-9]* ([.0-9]*% of [0-9]* connections)/''/g' | sed 's/Average Latency (s):  [.0-9]* (min [.0-9]*, max [.0-9]*)/''/g' | tr '\n' ',' | sed 's/,,/''/g' >> answer_count_$1.txt

sed 's/Latency bucket (s):   answer count/''/g' buckets_$1.txt | sed 's/Connection Statistics:/''/g' | sed 's/Reconnections:/''/g' | sed 's/[0-9]* ([.0-9]*% of [0-9]* connections)/''/g' | sed 's/Average Latency (s):  [.0-9]* (min [.0-9]*, max [.0-9]*)/''/g' | sed 's/:  [0-9]*/''/g' | sed 's/  /''/g'  | tr "\n" 'A' | sed 's/A/","/g'  | sed 's/"",/''/g' >> latenze_$1.txt

python3 test333.py answer_count_$1.txt latenze_$1.txt $2 $3
