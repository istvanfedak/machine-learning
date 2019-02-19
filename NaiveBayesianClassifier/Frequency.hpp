#ifndef FREQUENCY_HPP
#define FREQUENCY_HPP

#include "Data.hpp"
#include <stdio.h>
#include <string>
#include <vector>

// struct used to store all occurences of each attribute
// each attribute is represented by an instance of this struct
struct AttrFreq {
  int demYes;
  int repYes;
  int demNo;
  int repNo;
  int demAbs;
  int repAbs;
  AttrFreq();
};

typedef std::vector<AttrFreq> AttrFreqVec;					// A vector of attribute frequencies

// class used to calculate all of the frequencies from the data
class Frequency : public AttrFreqVec {
 public:
  const unsigned int vecSize = 17;
  int demCount;									// Number of democrats in the data set
  int repCount;									// Number of republicans in the data set
  void reset();									// Resents all the frequencies back to zero
  Frequency(const Data & randData, const unsigned int trainIndex); 		// trainIndex is the number of items from randData used for training
  void interpolation(const Data & randData, const unsigned int trainIndex);	// helper function used to find all the frequencies
  void print();
};

#endif /* FREQUENCY_HPP */
