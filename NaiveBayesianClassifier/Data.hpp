
#ifndef DATA_HPP
#define DATA_HPP

#include <stdio.h>
#include <string.h>
#include <time.h>
#include <string>
#include <fstream>
#include <vector>

typedef std::vector< std::vector<std::string> > StrMatrix;            // string matrix
typedef std::vector<std::string> StrVec;                              // string vector

// string vector class to read data
class Data : public StrMatrix {
 public:
  static StrVec split(std::string read, std::string delim);           // split the data separated by commas
  static StrMatrix read(std::string file_name, std::string delim);    // read the data file into a string matrix
  Data(std::string file_name, std::string delim);                     // constructor that reads the file and stores it as a matrix of strings
  void shuffle();						      // shuffle the vector array
  void print();							      // print the string array
};

#endif /* DATA_HPP */
