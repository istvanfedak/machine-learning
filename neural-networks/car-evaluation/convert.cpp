// this is used to convert the car evaluation data to integers

#include "../../naive-bayesian-classifier/Data.hpp"
#include <fstream>
#include <iostream>
using namespace std;

string convertBuying(string s)
{      if(s == "low")  return "1";
  else if(s == "med")  return "2";
  else if(s == "high") return "3";
  else                 return "4"; }

string convertMaint(string s)
{      if(s == "low")  return "1";
  else if(s == "med")  return "2";
  else if(s == "high") return "3";
  else                 return "4"; }

string convertDoors(string s)
{      if(s == "2")  return "1";
  else if(s == "3")  return "2";
  else if(s == "4") return "3";
  else                 return "4"; }

string convertPersons(string s)
{      if(s == "2")  return "1";
  else if(s == "4")  return "2";
  else                 return "3"; }

string convertLug(string s)
{      if(s == "small")  return "1";
  else if(s == "med")  return "2";
  else                 return "3"; }

string convertSafety(string s)
{      if(s == "low")  return "1";
  else if(s == "med")  return "2";
  else                 return "3"; }

string convertResult(string s)
{      if(s == "unacc") return "1";
  else if(s == "acc")   return "2";
  else if(s == "good")  return "3";
  else                  return "4"; }

int main(int argc, char * argv[])
{ if(argc != 3)
  { cout<<"Usage: ./"<<argv[1]<<"<file-name> <new-file-name>\n";
    return 1; }

  StrMatrix in = Data::read(argv[1], ",");
  ofstream fout(argv[2]);
  int pos = 0, neg = 0;

  for(int i = 0; !fout.fail() && i < in.size(); i++)
  { for(int j = 0; j < in[i].size(); j++)
    { if(j == 0) fout<<convertBuying(in[i][j]) + ",";
      else if(j == 1) fout<<convertMaint(in[i][j]) + ",";
      else if(j == 2) fout<<convertDoors(in[i][j]) + ",";
      else if(j == 3) fout<<convertPersons(in[i][j]) + ",";
      else if(j == 4) fout<<convertLug(in[i][j]) + ",";
      else if(j == 5) fout<<convertSafety(in[i][j]) + ",";
      else            fout<<convertResult(in[i][j])<<endl; } }
  fout.close(); }
