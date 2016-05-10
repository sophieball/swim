all: data

data: data.o dynarray.o hashmap.o
	gcc -o data data.o dynarray.o hashmap.o

data.o: data.c
	gcc -c data.c
dynarray.o: dynarray.c dynarray.h
	gcc -c dynarray.c
hashmap.o: hashmap.c hashmap.h
	gcc -c hashmap.c
