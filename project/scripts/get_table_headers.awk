#!/usr/bin/awk -f

# get_table_headers.awk
# Finds any lines with, "BEGIN," and,"END," and returns the lines between them.
# Builds a list of html headers based on the headers in the ics file.
# get_table_headers.sh has get_table_headers.awk as a dependency. It will
# generate a file called `headers` with all of the unique headers in the file.

BEGIN {
    FS = "[;:]"
    RS = "\n"
}

{
    if($1 != "BEGIN" && $1 != "END"){
        print $1
    }
}
