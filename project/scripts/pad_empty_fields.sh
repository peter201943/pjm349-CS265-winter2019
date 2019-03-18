#!/bin/bash

# pad_empty_fields.sh Pads out any missing fields in the headers list by
# setting that missing field to a blank string.  This script is called repeatedly
# for every VEVENT in an ics file. For example, not all VEVENTs have a URL field,
# but if even a single VEVENT has a URL field, then all of them will have the
# URL field set to an empty string. This is done to make it easier to
# generate the HTML table.

path=$(dirname $0)

if [ -f ./headers ]; then
    $path/pad_empty_fields.awk headers $1
else
    echo "Unable to find the file 'headers'"
fi
