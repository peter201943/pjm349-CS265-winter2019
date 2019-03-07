/*
 * csv.c - Implementation for a csv library
 *
 * Modified from code in Kernighan & Pike, _The Practice of Programming_
 *   Copyright (C) 1999 Lucent Technologies 
 *   Excerpted from 'The Practice of Programming' 
 *   by Brian W. Kernighan and Rob Pike 
 *
 * Kurt Schmidt
 * 3/2018
 *
 * gcc 5.4.0 20160609 on
 * Linux 4.13.0-32-generic
 *
 * EDITOR:  tabstop=2 cols=120
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "csv.h"

enum { NOMEM = -2 };          /* out of memory signal */

static char *line    = NULL ;  /* input chars */
static char *sline   = NULL ;  /* line copy used by split */
static int  maxline  = 0 ;     /* size of line[] and sline[] */
static char **field  = NULL ;  /* field pointers */
static int  maxfield = 0 ;     /* size of field[] */
static int  nfield   = 0 ;     /* number of fields in field[] */


static char fieldsep[] = "," ; /* field separator chars */

	/***** Prototypes for local helper functions ******/
static char *advquoted( char* ) ;
static int split( csv_t* ) ;


csv_t* csv_init( FILE *f )
{
	csv_t *rv = (csv_t*) malloc( sizeof( csv_t )) ;
	rv->fin = f ;
	reset( rv ) ;

	return( rv ) ;
}


void kill( csv_t* s )
{
	reset( s ) ;
	free( s ) ;
}

/* TODO
 *  Copy all the functions (but for main) from csvgetline2 here.  Not the prototypes.  You already have them in
 *  csv.h.  Functions that access global CSV data need to be modified, take a pointer to a CSV struct as the first
 *  argument, and any references need to be modified
 */


static char fieldsep[] = "," ; /* field separator chars */

static char* advquoted( char* ) ;
static int split( void ) ;

	/* endofline: check for and consume \r, \n, \r\n, or EOF */
static int endofline( FILE *f *fin, int c )
{
	int eol ;

	eol = ( c=='\r' || c=='\n' ) ;
	if( c=='\r' ) {
		c = getc( fin ) ;
		if( c!='\n' && c != EOF )
			ungetc( c, fin ) ;	/* read too far; put c back */
	}
	return eol ;
}

	/* reset: set variables back to starting values */
static void reset( csv_t )
{
	free( line );	 /* free(NULL) permitted by ANSI C */
	free( sline ) ;
	free( field ) ;
	line = NULL ;
	sline = NULL ;
	field = NULL ;
	maxline = maxfield = nfield = 0 ;
}

	/* csvgetline:  get one line, grow as needed */
	/* sample input: "LU",86.25,"11/4/1998","2:19PM",+4.0625 */
char* csvgetline( FILE *f *fin )
{	
	int i, c ;
	char *newl, *news ;

	if( line==NULL ) {			/* allocate on first call */
		maxline = maxfield = 1 ;
		line = (char*) malloc( maxline ) ;
		sline = (char*) malloc( maxline ) ;
		field = (char**) malloc( maxfield*sizeof( field[0] )) ;
		if( line==NULL || sline==NULL || field==NULL) {
			reset() ;
			return NULL ;		/* out of memory */
		}
	}

	for( i=0; (c=getc( fin ))!=EOF && ! endofline(fin,c); i++ ) {
		if( i>=maxline-1 ) {	  /* grow line */
			maxline *= 2;		    /* double current size */
			newl = (char*) realloc( line, maxline ) ;
			if( newl==NULL ) {
				reset() ;
				return NULL ;
			}
			line = newl ;
			news = (char*) realloc( sline, maxline ) ;
			if( news==NULL ) {
				reset() ;
				return NULL ;
			}
			sline = news ;
		}
		line[i] = c ;
	}  /* for i */

	line[i] = '\0' ;
	if( split()==NOMEM ) {
		reset() ;
		return NULL;			/* out of memory */
	}
	return (c==EOF && i==0) ? NULL : line ;
}

/* split: split line into fields */
static int split( csv_t )
{
	char *p, **newf ;
	char *sepp; /* pointer to temporary separator character */
	int sepc;   /* temporary separator character */

	nfield = 0 ;
	if( line[0]=='\0' )
		return 0 ;
	strcpy( sline, line ) ;
	p = sline ;

	do {
		if( nfield>=maxfield ) {
			maxfield *= 2;			/* double current size */
			newf = (char**) realloc( field, 
							maxfield * sizeof( field[0] )) ;
			if( newf==NULL )
				return NOMEM ;
			field = newf ;
		}
		if( *p=='"' )
			sepp = advquoted( ++p ) ;	/* skip initial quote */
		else
			sepp = p + strcspn( p, fieldsep ) ;
		sepc = sepp[0] ;
		sepp[0] = '\0' ;			/* terminate field */
		field[nfield++] = p ;
		p = sepp + 1 ;
	} while( sepc==',' ) ;

	return nfield ;
}

/* advquoted: quoted field; return pointer to next separator */
static char *advquoted( char* *f )
{
	int i, j ;

	for( i=j=0; p[j]!='\0'; ++i, ++j ) {
		if( p[j]=='"' && p[++j]!='"' ) {
				/* copy up to next separator or \0 */
			int k = strcspn( p+j, fieldsep ) ;
			memmove( p+i, p+j, k ) ;
			i += k ;
			j += k ;
			break ;
		}
		p[i] = p[j] ;
	}
	p[i] = '\0' ;
	return p + j ;
}

/* csvfield:  return pointer to n-th field */
char* csvfield( int n )
{
	if( n<0 || n>=nfield )
		return NULL ;
	return field[n] ;
}

/* csvnfield:  return number of fields */ 
int csvnfield( csv_t )
{
	return nfield ;
}
