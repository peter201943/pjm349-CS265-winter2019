#!/usr/bin/awk -f

#pad_empty_fields.sh Pads out any missing fields in the headers list by
#setting that missing field to a blank string.  This script is called repeatedly
#for every VEVENT in an ics file.  For example, not all VEVENTs have a URL
#field, but if even a single VEVENT has a URL field, then all of them will have
#the URL field set to an empty string. This is done to make it easier to
#generate the HTML table.

# This accepts a SINGLE VEVENT, without the BEGIN:VEVENT
# and END:VEVENT tags

#We set the FS to separate tags (BEGIN , END) from objects (VEVENT , VALARM).
BEGIN {
    FS = "[;:]"
}

# Process all of the lines in the first file. This condition becomes false
# as soon as we move into the second file, because NR != FNR when you reach the
# second file. In other words, this is just an if statement to check if we're
# in the first file.
NR == FNR {
    dict[$1] = ""
    next
}

# In the second file, fill in all of the dictionary's values with the 2nd column
# of data, which is the field's values.

#TODO: Your bug is here.
{
    temp=$1
    $1=""
    dict[temp] = $0
}


END {
    # If it starts with DTSTART or DTEND, then it requires a semicolon instead
    # of a normal colon, because that's how a ICS file is standardly formatted.
    for (i in dict) {
        if(i == "DTSTART" || i == "DTEND"){
            print i ";" dict[i]
        } else {
            print i ":" dict[i]    
        }
    }
}
