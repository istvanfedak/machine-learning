// this is used to convert the car evaluation data to integers

#include "../../src/Data.hpp"
#include <fstream>
#include <iostream>
using namespace std;

string convertTwo(string s)
{      if(s == "-1")  return "0";
  else                return "1"; }

string convertThree(string s)
{      if(s == "-1") return "0";
  else if(s == "0")  return "0.5";
  else               return "1"; }

string convertResult(string s)
{      if(s == "-1")  return "1";
  else                return "2"; }

int main(int argc, char * argv[])
{ if(argc != 3)
  { cout<<"Usage: ./"<<argv[1]<<"<file-name> <new-file-name>\n";
    return 1; }

  StrMatrix in = Data::read(argv[1], ",");
  ofstream fout(argv[2]);
  int pos = 0, neg = 0;

  for(int i = 0; !fout.fail() && i < in.size(); i++)
  { for(int j = 0; j < in[i].size(); j++)
    { if(j == 0)      fout<<convertTwo(in[i][j]) + ",";
      else if(j == 1) fout<<convertThree(in[i][j]) + ",";
      else if(j == 2) fout<<convertTwo(in[i][j]) + ",";
      else if(j == 3) fout<<convertTwo(in[i][j]) + ",";
      else if(j == 4) fout<<convertTwo(in[i][j]) + ",";
      else if(j == 5) fout<<convertTwo(in[i][j]) + ",";
      else if(j == 6) fout<<convertThree(in[i][j]) + ",";
      else if(j == 7) fout<<convertThree(in[i][j]) + ",";
      else if(j == 8) fout<<convertTwo(in[i][j]) + ",";
      else if(j == 9) fout<<convertTwo(in[i][j]) + ",";
      else if(j == 10) fout<<convertTwo(in[i][j]) + ",";
      else if(j == 11) fout<<convertTwo(in[i][j]) + ",";
      else if(j == 12) fout<<convertTwo(in[i][j]) + ",";
      else if(j == 13) fout<<convertThree(in[i][j]) + ",";
      else if(j == 14) fout<<convertThree(in[i][j]) + ",";
      else if(j == 15) fout<<convertThree(in[i][j]) + ",";
      else if(j == 16) fout<<convertTwo(in[i][j]) + ",";
      else if(j == 17) fout<<convertTwo(in[i][j]) + ",";
      else if(j == 18) fout<<convertTwo(in[i][j]) + ",";
      else if(j == 19) fout<<convertTwo(in[i][j]) + ",";
      else if(j == 20) fout<<convertTwo(in[i][j]) + ",";
      else if(j == 21) fout<<convertTwo(in[i][j]) + ",";
      else if(j == 22) fout<<convertTwo(in[i][j]) + ",";
      else if(j == 23) fout<<convertTwo(in[i][j]) + ",";
      else if(j == 24) fout<<convertTwo(in[i][j]) + ",";
      else if(j == 25) fout<<convertThree(in[i][j]) + ",";
      else if(j == 26) fout<<convertTwo(in[i][j]) + ",";
      else if(j == 27) fout<<convertTwo(in[i][j]) + ",";
      else if(j == 28) fout<<convertThree(in[i][j]) + ",";
      else if(j == 29) fout<<convertTwo(in[i][j]) + ",";
      else            fout<<convertResult(in[i][j])<<endl; } }
  fout.close(); }
