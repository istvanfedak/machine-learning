#include "Labeler.hpp"

// default constructor
Labeler::Labeler(const Data & randData, const unsigned trainingIndex, const Probability & trainingSet) {
  this->reset();
  this->interpolate(randData, trainingIndex, trainingSet);
}

void Labeler::reset() {
  this->percentError = 0;
}

std::string Labeler::label(const Probability & trainingSet, const StrVec & entry) {
  double demCondProb = 1; // defailt multiplicative identity
  double repCondProb = 1; // will contain the conditional probability of a republican
 // iterates through the entire training data
 for(unsigned int i = 1; i < trainingSet.vecSize; i++)
  { if(entry[i] == "y") // updates the conditional probablitity of a democrat and republican if attribute is yes
    { demCondProb *= trainingSet[i].demYes;
      repCondProb *= trainingSet[i].repYes; }
    else if(entry[i] == "n")
    { demCondProb *= trainingSet[i].demNo;
      repCondProb *= trainingSet[i].repNo; }
    else if(entry[i] == "?")
    { demCondProb *= trainingSet[i].demAbs;
      demCondProb *= trainingSet[i].repAbs; }
    else // if there's an error in data notify user
    { fprintf(stderr, "Error:: labler():: entry[%u] ", i);
      fprintf(stderr, "has invalid attribute name: %s\n", entry[i].c_str());
      exit(1); } }
    // naive bayesian classifier formula determining what class is the example
    if (demCondProb * trainingSet.demProb < repCondProb * trainingSet.repProb)
      return "republican";
    else 
      return "democrat"; }

// calculates the percent error for the given testing data by comparing if each example is true
void Labeler::interpolate(const Data & randData, const unsigned trainingIndex, const Probability & trainingSet)
{ int correct = 0; // stores the number of incorrectly classified examples in the testing data
  int incorrect = 0;
  // if there's no training data, display error
  if(randData.size() <= trainingIndex)
  { fprintf(stderr, "Error:: Frequency::interpolation():: trainingIndex is larger than or equal");
    fprintf(stderr, " to size of randData: %lu >= %u\n", randData.size(), trainingIndex);
    exit(1); }
  // iterate through all the training data
  for(unsigned int i = trainingIndex; i < randData.size(); i++)
  { std::string result = Labeler::label(trainingSet, randData[i]);
    if(result == randData[i][0]) // compares to see if they match
      correct += 1;
    else
      incorrect += 1;
  }
  // calculates the percent error
  this->percentError = (incorrect / ((double) correct + incorrect)) * 100;
}

void Labeler::print()
{ printf("Percent error = %f\n", this->percentError); }
