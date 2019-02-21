CC = g++
CDFLAGS = -Wall -g
SRC = main.cpp Data.cpp Frequency.cpp Probability.cpp Labeler.cpp
OBJ = $(SRC:%.cpp=%.o)
EXE = main.exe

all: $(EXE)
	@echo Done!
	@echo
	@echo Usage: ./$(EXE) \<data-file.txt\> \<delimiters\> \<data training percentage\> \<optianal:: repeated iterations\>

$(EXE): $(OBJ)
	@echo Linking...
	@$(CC) $(OBJ) -o $@

$(OBJ): $(SRC)
	@echo Compiling...
	@$(CC) $(CDFLAGS) -c $(SRC) $<

clean:
	@echo Cleaning up...
	@rm -f *.o
	@rm -f *.out
	@rm -f $(EXE)
