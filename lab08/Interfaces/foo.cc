
Foo f ;

f.bar( 3 ) ;
bar( &f, 3 ) ;

bar( Foo* this, int 3 ) ;


node struct sNode ;

struct sNode{
	int e ;
	struct sNode *next ;
} ;

typedef struct sNode sNode ;

typedef sNode* Stack ;

Stack head = NULL ;

Stack stack_init() {
	sNode *t = malloc( sizeof( sNode )) ;
	t->next = NULL ;
}

void push( Stack* s, int i ) {
		t->e = i ;
		t->next = *s ;
		*s = t ;
}

int pop( Stack* ) ;

int isEmpty( Stack* )
{
	return( head==NULL );
}
