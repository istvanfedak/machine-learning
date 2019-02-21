#ifndef LABELER_HPP
#define LABELER_HPP
#include "Probability.hpp"

// this class labels the examples based on the conditional probabilities
class Labeler {
 public:
  double percentError;	// calculates the error of the run
  void reset();
  Labeler(const Data & randData, const unsigned trainingIndex, const Probability & trainingSet);
  // this function labels the example using naive basian equation
  static std::string label(const Probability & prob, const StrVec & entry);
  // this function calculates the error given the percentage of training data
  void interpolate(const Data & randData, const unsigned trainingIndex, const Probability & trainingSet);
  void print();
};

#endif /* LABELER_HPP */
