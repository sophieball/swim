GCC=gcc -I. -I../common -std=c99 -Wall -DDEBUG -DSWIM -O3 
#-DDEVELOP
GPP=g++ -I.

BASIC_OBJ = fptree.o memmgr.o timeval.o histmgr.o
TARGETS = mem-delayed disk-delayed asc2bin bin2asc
all: $(TARGETS)

#hash_verifier 
 
fptree.o: ../common/fptree.c ../common/fptree.h
	$(GCC) -c ../common/fptree.c

histmgr.o: ../common/histmgr.c ../common/histmgr.h
	$(GCC) -c ../common/histmgr.c

timeval.o: ../common/timeval.c ../common/timeval.h
	$(GCC) -c ../common/timeval.c
	
memmgr.o: ../common/memmgr.c ../common/memmgr.h
	$(GCC) -c ../common/memmgr.c

largeSlidingWind: largeSlidingWind.c $(BASIC_OBJ)
	$(GCC) largeSlidingWind.c  -o largeSlidingWind $(BASIC_OBJ) -lm 
	
disk-delayed: disk-delayed.c $(BASIC_OBJ)
	$(GCC) disk-delayed.c  -o disk-delayed $(BASIC_OBJ) -lm 
	
mem-delayed: mem-delayed.c $(BASIC_OBJ)
	$(GCC) mem-delayed.c  -o mem-delayed $(BASIC_OBJ) -lm 
	
average-analyser: average-analyser.c $(BASIC_OBJ)
	$(GCC) average-analyser.c  -o average-analyser $(BASIC_OBJ) -lm 
	
asc2bin: asc2bin.c $(BASIC_OBJ)
	$(GCC) asc2bin.c -o asc2bin $(BASIC_OBJ) -lm
	
bin2asc: bin2asc.c $(BASIC_OBJ)
	$(GCC) bin2asc.c -o bin2asc $(BASIC_OBJ) -lm 

debug-bin: debug-bin.c
	$(GCC) debug-bin.c -o debug-bin
	
clean:
	rm -f $(TARGETS) *.o *~
