#ifndef PROBABILITY_HPP
#define PROBABILITY_HPP
#include "Frequency.hpp"

// this class calculates the conditional probabilities
struct AttrProb {
  double demYes; // P(yes | dem) = freq::demYes / (freq::demYes + freq::repYes)
  double repYes; // P(yes | rep) = freq::repYes / (freq::demYes + freq::repYes)
  double demNo;  // P(no  | dem) = freq::demNo  / ( freq::demNo + freq::repNo )
  double repNo;  // P(no  | rep) = freq::repNo  / ( freq::demNo + freq::repNo )
  double demAbs; // P(abs | dem) = freq::demAbs / (freq::demAbs + freq::repAbs)
  double repAbs; // P(abs | rep) = freq::repAbs / (freq::demAbs + freq::repAbs)
  AttrProb();
};

typedef std::vector<AttrProb> AttrProbVec;	// an attribute probability vector for each attribute

// class used to store the conditional probabilities of each attribute
class Probability : public AttrProbVec {
 public:
  const unsigned int vecSize = 17;
  double demProb; // P(dem) = freq::demCount / (freq::demCount + freq::repCount)
  double repProb; // P(rep) = freq::repCount / (freq::demCount + freq::repCount)
  void reset();
  Probability(const Frequency & freq);
  void interpolation(const Frequency & freq);	// function that calculates conditional probabilities based on attribute value frequencies
  void print();
};

#endif /* PROBABILITY_HPP */
