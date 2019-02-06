#ifndef FREQUENCY_HPP
#define FREQUENCY_HPP

#include "Data.hpp"
#include <stdio.h>
#include <string>
#include <vector>

struct AttrFreq {
  int demYes;
  int repYes;
  int demNo;
  int repNo;
  int demAbs;
  int repAbs;
  AttrFreq();
};

typedef std::vector<AttrFreq> AttrFreqVec;

class Frequency : public AttrFreqVec {
 public:
  const unsigned int vecSize = 17;
  int demCount;
  int repCount;
  void reset();
  Frequency(const Data & randData, const unsigned int trainIndex); // trainIndex is the number of items from randData used for training
  void interpolation(const Data & randData, const unsigned int trainIndex);
  void print();
};

#endif /* FREQUENCY_HPP */