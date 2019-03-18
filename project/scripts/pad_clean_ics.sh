#!/bin/bash

file_name_out=$(basename $1)
file_name_out+=".pad"

path=$(dirname $0)
current_line=1
start_line=1

rm -f $file_name_out
rm -f temp_piece

# TODO: Fetch me everything between the two VEVENT tags, then do
# ./scripts/pad_empty_fields.sh FILE | sort >> output
while read line; do
    if [[ "$line" == "BEGIN:VEVENT" ]]
    then
        start_line=$((current_line+1))
    elif [[ "$line" == "END:VEVENT" ]]
    then
        echo "$(sed -n "$start_line, $((current_line-1)) p" $1)" > temp_piece
        echo "BEGIN:VEVENT" >> $file_name_out
        $path/pad_empty_fields.sh temp_piece | sort >> $file_name_out
        echo "END:VEVENT" >> $file_name_out
	start_copy_line=$((current_line+1))
    fi
    current_line=$((current_line+1))
done < $1

rm -f temp_piece
