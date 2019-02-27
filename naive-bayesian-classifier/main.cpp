#include "Labeler.hpp"
#include <fstream>
using namespace std;

// this function trains the classifier given the shuffled data
// returns percent error
const double train(Data & data, const int trainingIndex) {
  data.shuffle();
  Frequency trainingSetFreq(data, trainingIndex);
  Probability trainingSetProb(trainingSetFreq);
  Labeler naiveBayesLabeler(data, trainingIndex, trainingSetProb);
  return naiveBayesLabeler.percentError;
}

// calculates the average training result given the number of repetitions
const double averageTrainingResult(Data & data, const int trainingIndex, const unsigned int repetitions) {
  int hundreth = repetitions / 100;
  // print warning to the user
  if(repetitions > 1000)
    printf("This might take a while...\n");
  double accumulator = 0;
  // does the calculations
  for(unsigned int i = 0; i < repetitions; i++) {
    accumulator += train(data, trainingIndex);
    // visual feedback to the user
    if(i % hundreth == 0) {
      printf("\rProgress [%d%%]", i / hundreth);
      fflush(stdout);
    }
  }
  printf("\rProgress [100%%]\n");
  // returns the average error
  return accumulator / repetitions; }

int main(int argc, char * argv[]) {
  // initializes random variable
  std::srand ( unsigned ( time(0) ) );
  // asserts command line arguments
  if(argc < 4) {
    printf("usage: %s <data-file.txt> <delimiters> ",argv[0]);
    printf("<data training percentage> <optiabal:: repeated iterations>\n");
    return 1;
  }
  // initializes the data
  Data data(argv[1], argv[2]);

  // initializes the percentage of training data
  const int trainingIndex = data.size() * (atof(argv[3]) / 100);

  // calculates the error of a single run
  printf("Single run percent error  = ");
  printf("%.3f %%\n", train(data, trainingIndex));

  // calculates the avarage error of n runs
  if(argc == 5) {
    const double avrgPercentError = averageTrainingResult(data, trainingIndex, atoi(argv[4]));
    printf("Average run percent error = %.3f %%\n", avrgPercentError);
  }
  return 0;
}


