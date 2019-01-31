#!/bin/bash
#
#count.bash - loads files and returns statistics
#
#Peter J. Mangelsdorf
#pjm349
#CS 265
#30 Jan 2019
#
#Write a script called count.bash that, for each regular file in the working directory, prints the filename, the # of lines, and the # of words to stdout, like this without using FIND. Must support spaced filenames:
#breadIsDangerous.txt 73 431
#spellExample 5 21
#
#INPUT: Directory command is called in
#OUTPUT: Filename, Line Count, Word Count
#

for file in $(ls -p | grep -v /); do
    lines=$(wc -l <$file)
    words=$(wc -w <$file)
    echo $file $lines $words
done
