
#!/bin/bash

PAGER=less
RM=-rm -f
CHMOD=chmod +x

.PHONY = build view clean

build: bank.py
	$CHMOD accounts

view:
	$PAGER bank.py

clean:
	$RM *.py
