#!/bin/bash

max_chan_id=$1
output_fnbase=$2
output_arry=()

chainarry=( $(seq 1 $max_chan_id) )
for i in ${chainarry[@]}
do
    ofn=${output_fnbase}_ch${i}.wav
    echo "-a:${i} -f 24,1,48000 -o ${ofn} -chcopy:${i}:1" 

done

#cmd="ecasound"
# ${output_arry[@]}"

echo $cmd

#ecasound -c -a:1,2,3,4 -f 24,4,48000 -i alsaplugin,1,0 \
#    -a:1 -f 24,1,48000 -o chan1.wav -chcopy:1,1 
#    -a:2 -f 24,1,48000 -o chan2.wav  -chcopy:2,1 
#    -a:3 -f 24,1,48000 -o chan3.wav -chcopy:3,1 
#    -a:4 -f 24,1,48000 -o chan4.wav -chcopy:4,1
