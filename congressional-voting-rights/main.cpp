#include "Labeler.hpp"
#include <fstream>
using namespace std;

const double train(Data & data, const int trainingIndex)
{ data.shuffle();
  Frequency trainingSetFreq(data, trainingIndex);
  Probability trainingSetProb(trainingSetFreq);
  Labeler naiveBayesLabeler(data, trainingIndex, trainingSetProb);
  return naiveBayesLabeler.percentError;
}

const double averageTrainingResult(Data & data, const int trainingIndex, const unsigned int repetitions)
{ int hundreth = repetitions / 100;
  if(repetitions > 1000)
    printf("This might take a while...\n");
  double accumulator = 0;
  for(unsigned int i = 0; i < repetitions; i++)
  { accumulator += train(data, trainingIndex);
    if(i % hundreth == 0)
    { printf("\rProgress [%d%%]", i / hundreth);
      fflush(stdout); } }
  printf("\rProgress [100%%]\n");
  return accumulator / repetitions; }

int main(int argc, char * argv[]) 
{ std::srand ( unsigned ( time(0) ) );
  if(argc < 4)
  { printf("usage: %s <data-file.txt> <delimiters> ",argv[0]);
    printf("<data training percentage> <optiabal:: repeated iterations>\n");
    return 1; }
  Data data(argv[1], argv[2]);
  const int trainingIndex = data.size() * (atof(argv[3]) / 100);

  printf("Single run percent error  = ");
  printf("%.3f %%\n", train(data, trainingIndex));

  if(argc == 5)
  { const double avrgPercentError = averageTrainingResult(data, trainingIndex, atoi(argv[4]));
    printf("Average run percent error = %.3f %%\n", avrgPercentError); }
  return 0; }


