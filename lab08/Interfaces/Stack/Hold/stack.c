/*************************************************************************
 *
 * stack.c -- implementation for an int stack
 *
 * Kurt Schmidt
 * May 2018
 *
 * EDITOR:  cols=120, tabstop=2
 *
 ************************************************************************/

#include <stdlib.h>

#include "stack.h"


int INITIAL_SIZE = 10 ;

Stack* stack_init()
{
	Stack *rv = malloc( sizeof( Stack )) ;
	if( rv==NULL ) return( rv ) ;

	reset( rv ) ;

	return( rv ) ;
}

void kill( Stack *s )
{
	free( s->data ) ;
	free( s ) ;
}

bool reset( Stack* s )
{
	int *t = realloc( s->data, INITIAL_SIZE*sizeof( s->data[0] )) ;
	if( t==NULL) return( FALSE ) ;

	s->data = t ;
	s->cap = INITIAL_SIZE ;
	s->size = 0 ;

	return( TRUE ) ;
}

bool push( Stack *s, int i )
{
	if( s->cap <= s->size )
	{
		int *t = realloc( s->data, s->cap*2*sizeof( s->data[0] )) ;
		if( t==NULL ) return( FALSE ) ;
	}
	
	s->data[ s->size ] = i ;
	s->size += 1 ;
	
	return( TRUE ) ;
}

int pop( Stack* s )
{
	if( isEmpty( s ))
		return( 513 ) ;

	return( s->data[ --(s->size) ] ) ;
}

int top( Stack* s )
{
	if( isEmpty( s ))
		return( 513 ) ;

	return( s->data[ s->size - 1 ] ) ;
}


	/* Returns TRUE if stack is empty */
bool isEmpty( Stack* s ) 
{
	return( s->size == 0 ) ;
}

