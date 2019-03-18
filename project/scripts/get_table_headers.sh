#!/bin/bash

# get_table_headers.sh. Calls get_table_headers.awk, passes it into sort and
# uniq. This is done to preserve the purity of get_table_headers.awk. This works
# to removes any duplicate events. Builds a list of html headers based on the
# headers in the ics file. get_table_headers. sh has get_table_headers.awk as a
# dependency. It will generate a file called `headers` with all of the unique
# headers in the file.

path=$(dirname $0)
[ -f $1 ] && cat $1 | $path/get_table_headers.awk | sort | uniq > headers
