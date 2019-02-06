#include "Labeler.hpp"

Labeler::Labeler(const Data & randData, const unsigned trainingIndex, const Probability & trainingSet)
{ this->reset();
  this->interpolate(randData, trainingIndex, trainingSet);
}

void Labeler::reset()
{ this->percentError = 0; }

std::string Labeler::label(const Probability & trainingSet, const StrVec & entry)
{ double demCondProb = 1;
  double repCondProb = 1;
  for(unsigned int i = 1; i < trainingSet.vecSize; i++)
  { if(entry[i] == "y")
    { demCondProb *= trainingSet[i].demYes;
      repCondProb *= trainingSet[i].repYes; }
    else if(entry[i] == "n")
    { demCondProb *= trainingSet[i].demNo;
      repCondProb *= trainingSet[i].repNo; }
    else if(entry[i] == "?")
    { demCondProb *= trainingSet[i].demAbs;
      demCondProb *= trainingSet[i].repAbs; }
    else
    { fprintf(stderr, "Error:: labler():: entry[%u] ", i);
      fprintf(stderr, "has invalid attribute name: %s\n", entry[i].c_str());
      exit(1); } }
    if (demCondProb * trainingSet.demProb < repCondProb * trainingSet.repProb)
      return "republican";
    else 
      return "democrat"; }

void Labeler::interpolate(const Data & randData, const unsigned trainingIndex, const Probability & trainingSet)
{ int correct = 0;
  int incorrect = 0;
  if(randData.size() <= trainingIndex)
  { fprintf(stderr, "Error:: Frequency::interpolation():: trainingIndex is larger than or equal");
    fprintf(stderr, " to size of randData: %lu >= %u\n", randData.size(), trainingIndex);
    exit(1); }
  for(unsigned int i = trainingIndex; i < randData.size(); i++)
  { std::string result = Labeler::label(trainingSet, randData[i]);
    if(result == randData[i][0]) // compares to see if they match
      correct += 1;
    else
      incorrect += 1;
  }
  this->percentError = (incorrect / ((double) correct + incorrect)) * 100;
}

void Labeler::print()
{ printf("Percent error = %f\n", this->percentError); }