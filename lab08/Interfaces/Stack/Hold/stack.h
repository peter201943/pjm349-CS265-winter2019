/*************************************************************************
 *
 * stack.h -- interface for an int stack
 *
 * Kurt Schmidt
 * May 2018
 *
 * EDITOR:  cols=120, tabstop=2
 *
 ************************************************************************/

#ifndef __KS_STACK_H_
#define __KS_STACK_H_

extern int INITIAL_SIZE ;

typedef enum { FALSE, TRUE } bool ;

typedef struct 
{
	int* data ;
	int size ;
	int cap ;
} Stack ;

	/* factory function (constructor), creates new object */
Stack* stack_init() ;

	/* returns stack to initial empty state.  FALSE on failure */
bool reset( Stack* ) ;

	/* pushes item onto stack */
bool push( Stack*, int ) ;

	/* pops top item from stack.  Undefined on empty stack */
int pop( Stack* ) ;

	/* Returns item at top of stack, does not modify stack.  Undefine on empty stack */
int top( Stack* ) ;

	/* Returns TRUE if stack is empty */
bool isEmpty( Stack* ) ;


#endif  /* __KS_STACK_H_ */
