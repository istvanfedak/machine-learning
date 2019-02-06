#include "Data.hpp"

Data::Data(std::string file_name, std::string delim)
{ StrMatrix sm = Data::read(file_name, delim); 
  for(unsigned int i = 0; i < sm.size(); i++) // copies the matrix
    this->push_back(sm[i]); } 

int randomInRange(int a, int b)
{ return (b<a)? random()%(a-b+1)+b : random()%(b-a+1)+a; }

void swap(StrMatrix & sm, unsigned int a, unsigned int b)
{ StrVec temp = sm.at(a);
  sm.at(a) = sm.at(b);
  sm.at(b) = temp; }

void shuffleStrMatrix(StrMatrix & sm) 
{ for(unsigned int i = sm.size() - 1; i > 0; --i)
    swap(sm, i, randomInRange(0, i)); }

void Data::shuffle() // shuffles the array to make it random
{ shuffleStrMatrix(*this); }

StrVec Data::split(std::string read, std::string delim)
{ StrVec ret;
  char * str = strdup(read.c_str());
  char * pch;
  pch = strtok (str, delim.c_str());
  if(pch != NULL) ret.push_back(std::string(pch));
  while (pch != NULL)
  { pch = strtok (NULL, delim.c_str());
    if(pch != NULL)
      ret.push_back(std::string(pch)); }
    free(str);
    return ret; }

StrMatrix Data::read(std::string file_name, std::string delim)
{ StrMatrix ret;
  std::ifstream fin(file_name.c_str());
  if(fin.fail())
  { fprintf(stderr, "Data:: failed to open %s\n", file_name.c_str());
    return ret; }
  std::string read;
  while(!fin.fail())
  { getline(fin, read);
    if(fin.fail()) break;
    ret.push_back(Data::split(read, delim)); }
  return ret; }

void Data::print()
{ for(unsigned int i = 0; i < size(); i++)
  { for(unsigned int j = 0; j < at(i).size(); j++)
      printf("%s ", this->at(i).at(j).c_str());
    printf("\n"); } }
