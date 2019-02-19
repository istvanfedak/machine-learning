#ifndef LABELER_HPP
#define LABELER_HPP
#include "Probability.hpp"

class Labeler {
 public:
  double percentError;
  void reset();
  Labeler(const Data & randData, const unsigned trainingIndex, const Probability & trainingSet);
  static std::string label(const Probability & prob, const StrVec & entry);
  void interpolate(const Data & randData, const unsigned trainingIndex, const Probability & trainingSet);
  void print();
};

#endif /* LABELER_HPP */