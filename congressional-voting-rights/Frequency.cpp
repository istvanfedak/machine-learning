#include "Frequency.hpp"

AttrFreq::AttrFreq()
  { demYes = 0;
    repYes = 0;
    demNo  = 0;
    repNo  = 0;
    demAbs = 0;
    repAbs = 0; }

Frequency::Frequency(const Data & randData, const unsigned int trainIndex)
{ this->reset(); 
  this->interpolation(randData, trainIndex); }

void Frequency::reset() {
  this->clear();
  this->demCount = 0;
  this->repCount = 0;
  for(unsigned int i = 0; i < vecSize; i++)
    this->push_back(AttrFreq()); }

void Frequency::interpolation(const Data & randData, const unsigned int trainIndex)
{ this->reset();
  if(randData.size() < trainIndex)
  { fprintf(stderr, "Error:: Frequency::interpolation():: trainIndex is larger ");
    fprintf(stderr, "than size of randData: %lu > %u\n", randData.size(), trainIndex);
    exit(1); }
  for(unsigned int i = 0; i < trainIndex; i++) 
  { bool democrat;
    for(unsigned int j = 0; j < randData[i].size(); j++ ) 
    { if(j == 0) 
      { if(randData[i][j] == "democrat") 
        { democrat = true; 
          this->demCount += 1; }
        else if(randData[i][j] == "republican") 
        { democrat = false; 
          this->repCount += 1; }
        else 
        { fprintf(stderr, "Error:: Frequency():: Data[%u][%u] ", i, j);
          fprintf(stderr, "has invalid class name %s\n", randData[i][j].c_str());
          exit(1); } }
      else 
      { if(randData[i][j] == "y") 
        { if(democrat) this->at(j).demYes += 1;
          else         this->at(j).repYes += 1; }
        else if(randData[i][j] == "n")
        { if(democrat) this->at(j).demNo  += 1;
          else         this->at(j).repNo  += 1; }
        else if(randData[i][j] == "?") 
        { if(democrat) this->at(j).demAbs += 1;
          else         this->at(j).repAbs += 1; }
        else 
        { fprintf(stderr, "Error:: Frequency():: Data[%u][%u] ", i, j);
          fprintf(stderr, "has invalid attribute name: %s\n", randData[i][j].c_str());
          exit(1); } } } } }

void Frequency::print()
{ const char * names[] = {
    "Class Name",
    "handicapped-infants",
    "water-project-cost-sharing",
    "adoption-of-the-budget-resolution",
    "physician-fee-freeze",
    "el-salvador-aid",
    "religious-groups-in-schools",
    "anti-satellite-test-ban",
    "aid-to-nicaraguan-contras",
    "mx-missile",
    "immigration",
    "synfuels-corporation-cutback",
    "education-spending",
    "superfund-right-to-sue",
    "crime",
    "duty-free-exports",
    "export-administration-act-south-africa"
  };
  for(unsigned int i = 0; i < this->size(); i++)
  { printf("\n%s", names[i]);
    printf("\n--------------------------------------\n");
    if(i == 0)
    { printf("             democrats %d\n", this->demCount);
      printf("           republicans %d\n", this->repCount); }
    else
    { printf("          democrat-yes %d\n", this->at(i).demYes);
      printf("        republican-yes %d\n", this->at(i).repYes);
      printf("           democrat-no %d\n", this->at(i).demNo );
      printf("         republican-no %d\n", this->at(i).repNo );
      printf("    democrat-abstained %d\n", this->at(i).demAbs);
      printf("  republican-abstained %d\n", this->at(i).repAbs); } } }