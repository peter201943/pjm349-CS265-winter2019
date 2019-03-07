/*************************************************************************
 *
 * stack_drive.c -- test driver for stack
 *
 * Kurt Schmidt
 * May 2018
 *
 * EDITOR:  cols=120, tabstop=2
 *
 ************************************************************************/

#include <stdio.h>

#include "stack.h"

int data[] = { 7, 13, 323, 100, 35, 66, 103, 234, 11, 612, 42 } ;

int main( int argc, char **argv )
{
	int i = 0 ;
	int t ;
	Stack *s = stack_init() ;

	if( ! isEmpty( s ))
		fprintf( stderr, "New stack not empty\n" ) ;

	for( ; i<11; ++i )
	{
		push( s, data[i] ) ;
		if( isEmpty( s ))
			fprintf( stderr, "Stack empty after pushing %d at %d\n", data[i], i ) ;
		t = top( s ) ;
		if( t != data[i] )
			fprintf( stderr, "%d found on top of stack after pushing %d\n", t, data[i] ) ;
	}

	for( i=10; i>=0; --i )
	{
		t = pop( s ) ;
		if( t != data[i] )
			fprintf( stderr, "Popped %d, expected %d\n", t, data[i] ) ;
		if( i>0 && isEmpty( s ))
			fprintf( stderr, "Non-empty Stack empty after popping %d\n", t ) ;
	}

	if( ! isEmpty( s ))
		fprintf( stderr, "Empty stack not empty\n" ) ;

	fprintf( stderr, "\nDone!\n" ) ;

	return( 0 ) ;
}  /* main */
