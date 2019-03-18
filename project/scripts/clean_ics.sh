#!/bin/bash

# clean_ics.sh 
# Finds and removes all VALARMs from the ics file. Generates a
# file called temp_out that has all of the VALARMs removed.


file_name_out=$(basename $1)
file_name_out+=".temp"

rm -f temp_out

start_copy_line=1
start_line=1
current_line=1

touch temp_out

while read line; do
    # Set the starting line to wherever the BEGIN:VALARM is.
    if [[ "$line" == "BEGIN:VALARM" ]]
    then
        start_line=$((current_line))
    # When you get to the END:VALARM, take every line from when you first
    # saw the BEGIN:VALARM, to the END:VALARM, and splice it out
    elif [[ "$line" == "END:VALARM" ]]
    then
	echo "$(sed -n "$start_copy_line, $((start_line-1)) p" $1)" >> temp_out
	start_copy_line=$((current_line+1))
    fi
    current_line=$((current_line+1))
done < $1

# Strip away everything after the last END:VEVENT
line_num=$(cat $1 | wc -l)
echo "$(sed -n "$start_copy_line, $line_num p" $1)" >> temp_out

# Strip away everything before the first BEGIN:VEVENT
current_line=1
while read line; do
    if [[ "$line" == "BEGIN:VEVENT" ]]
    then
        sed -i "1, $((current_line-1))d" temp_out
        head -n -1 temp_out > $file_name_out
        final_line=$(tail -n 1 $file_name_out)
        if [ "$final_line" != "END:VEVENT" ]
        then
            echo "END:VEVENT" >> $file_name_out
        fi
        exit 0
    else
        current_line=$((current_line+1))
    fi
done < temp_out
