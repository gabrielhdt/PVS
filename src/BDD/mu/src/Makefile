# Copyright (c) 1992-1995 G. Janssen

BIN=$(HOME)/bin
UTILS=../../bdd/utils
BDD=../../bdd/src

INCLUDES   = -I$(BDD) -I$(UTILS)

ARS =  $(BDD)/libbdd2.a $(UTILS)/libutils.a

# specify appropriate C compiler flags here:
#CFLAGS= -W0,-opt,4 -DHAVE_ALLOCA $(INCLUDES)
#CFLAGS= -O -Aa -D_XOPEN_SOURCE $(INCLUDES)
CFLAGS= -g $(INCLUDES)
#CFLAGS= -O -D_XOPEN_SOURCE $(INCLUDES)
LDFLAGS= -s

obj=	mu.o y.tab.o lex.yy.o main.o

mu : ${obj}
	$(CC) ${LDFLAGS} -o mu ${obj} $(ARS) -lfl

.c.o : ; $(CC) ${CFLAGS} -c $*.c

main.o : main.c mu.h
mu.o : mu.c mu.h
y.tab.c : yacc.y mu.h
	yacc -d yacc.y
y.tab.h : yacc.y mu.h
	yacc -d yacc.y
y.tab.o : y.tab.c mu.h
lex.yy.c : lex.l mu.h
	lex -l lex.l
lex.yy.o : lex.yy.c y.tab.h mu.h
	$(CC) ${CFLAGS} -w -c lex.yy.c

install : mu
	mv mu /usr/es/bin

clean : 
	rm -f *.o *.a lex.yy.c y.tab.c y.tab.h

what :
	# make       - makes the program
	# make clean - cleans up objects and archives in this directory
