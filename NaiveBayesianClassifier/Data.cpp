#include "Data.hpp"

// constructor that reads a text file and stores it as a matrix of strings
Data::Data(std::string file_name, std::string delim) {
  StrMatrix sm = Data::read(file_name, delim);
  for(unsigned int i = 0; i < sm.size(); i++)                 // copies the matrix
    this->push_back(sm[i]);
}

// return an random integer in the range of [ a, b ]
int randomInRange(int a, int b) {
  if( b < a )
    return random () % ( a - b + 1) + b;
  else
    return random () % ( b - a + 1 ) + a;
}

// swap two idems in the string matrix
void swap( StrMatrix & sm, unsigned int a, unsigned int b) {
  StrVec temp = sm.at(a);
  sm.at(a) = sm.at(b);
  sm.at(b) = temp; }

// helper function that randomly shuffles a string matrix
void shuffleStrMatrix(StrMatrix & sm) {
  for ( unsigned int i = sm.size() - 1; i > 0; --i )
    swap(sm, i, randomInRange(0, i));
}

// shuffles the string matrix object to make it random
void Data::shuffle () {
  shuffleStrMatrix ( *this );
}

// function that splits a string into a string vector based on the delimiter
StrVec Data::split(std::string read, std::string delim) {
  StrVec ret;
  char * str = strdup( read.c_str() );
  char * pch;
  pch = strtok (str, delim.c_str() );

  if ( pch != NULL )							// if the current pointer character is not Null push back
    ret.push_back( std::string(pch) );

  while ( pch != NULL ) {						// iterate through all of the delimiters to extract all substrings
    pch = strtok( NULL, delim.c_str() );

    if ( pch != NULL )
      ret.push_back( std::string(pch) );
  }
  free(str);								// free the temporary char *
  return ret;								// return the vector of strings
}

// function to read data from strings, split them, and store them into a string matrix
StrMatrix Data::read(std::string file_name, std::string delim) {
  StrMatrix ret;
  std::ifstream fin( file_name.c_str() );

  if ( fin.fail() ) {							// if file failed to open display error and return empty matrix
    fprintf(stderr, "Data:: failed to open %s\n", file_name.c_str() );
    return ret;
  }

  std::string line;
  while ( ! fin.fail() ) {
    getline(fin,line);
    if ( fin.fail() ) break;
    ret.push_back( Data::split(line, delim) );				// for each line read, split it into a string vector and push it back
  }
  return ret;
}

// simple function to print string matrix
void Data::print() {
  for ( unsigned int i = 0; i < size(); i++ ) {
    for ( unsigned int j = 0; j < at(i).size(); j++ )
      printf("%s ", this->at(i).at(j).c_str() );
    printf("\n");
  }
}
