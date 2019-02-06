
#ifndef DATA_HPP
#define DATA_HPP

#include <stdio.h>
#include <string.h>
#include <time.h>
#include <string>
#include <fstream>
#include <vector>

typedef std::vector< std::vector<std::string> > StrMatrix;
typedef std::vector<std::string> StrVec;

class Data : public StrMatrix {
 public:
  static StrVec split(std::string read, std::string delim);
  static StrMatrix read(std::string file_name, std::string delim);
  Data(std::string file_name, std::string delim);
  void shuffle();
  void print();
};

#endif /* DATA_HPP */
