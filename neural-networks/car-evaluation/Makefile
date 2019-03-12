CC = g++
SRC = convert.cpp ../../naive-bayesian-classifier/Data.cpp
EXE = convert.out

all: compile
	@echo Done!
	@echo
	@echo Usage: ./$(EXE) \<data-file\> \<new-data-file\>

compile:
	@echo Compiling...
	@$(CC) $(SRC) -o $(EXE)

clean:
	@echo Cleaning up...
	@rm -f *.o
	@rm -f *.out
	@rm -f $(EXE)
