
#Peter J. Mangelsdorf
#Prof. Will Mongan
#CS 265
#6 March 2019

#Lab 8: Makefile
#An exercise in manipulating files to generate an executable.

#VARIABLES
SHELL = /bin/bash
CC = gcc
EXE = foo
JAVAC = javac
JRE = java
PAGER = less
TEST_OUT = test.out
EXP_OUT = expected.out
PYTHON = python
RM = -rm
#GENERATED = foo.o main.o test.out $(EXE) foo.class

#clear; run-py; run-c; read; run-java; save-java; test-java are PHONY targets.

#INSTRUCTIONS/TARGETS
foo.o: foo.c foo.h
	$(CC) -c foo.c

main.o: main.c foo.h
	$(CC) -c main.c

$(EXE): foo.o main.o
	$(CC) -o$(EXE) main.o foo.o

run-c: $(EXE)
	./$(EXE)

run-py: foo.py
	$(PYTHON) foo.py

read:
ifdef (README)
	$(PAGER) README
endif

foo.class: foo.java
	$(JAVAC) foo.java

run-java: foo.class
	$(JRE) foo

save-java: foo.class
	$(JRE) foo > $(TEST_OUT)

test-java: $(TEST_OUT) $(EXP_OUT)
	-@if diff $(TEST_OUT) $(EXP_OUT) &> /dev/null; then; echo "Passed!"; else; echo "Not the same!"; fi

clean:
	$(RM) -f foo.class foo main.o foo.o test.out expected.out

