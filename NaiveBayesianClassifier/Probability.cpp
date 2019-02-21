#include "Probability.hpp"

// default constructor for the conditional probabilities of each attribute
AttrProb::AttrProb() {
  demYes = 0;
  repYes = 0;
  demNo  = 0;
  repNo  = 0;
  demAbs = 0;
  repAbs = 0;
}

// calculates the conditional probabilities based on frequency
Probability::Probability(const Frequency  & freq) {
  this->reset();
  this->interpolation(freq);
}

// resents all conditional probabilities
void Probability::reset() {
  this->clear();
  this->demProb = 0;
  this->repProb = 0;
  for ( unsigned int i = 0; i < vecSize; i++ )
    this->push_back(AttrProb()); 
}

// calculates all the constitional probabilities
void Probability::interpolation(const Frequency & freq)
{ this->reset();
  for ( unsigned int i = 0; i < freq.size(); i++ ) {
    if ( i == 0 ) { // calculates the class probabilities
      this->demProb = freq.demCount / ((double) freq.demCount + freq.repCount);
      this->repProb = freq.repCount / ((double) freq.demCount + freq.repCount);
    } else {        // calculates the attribute level probabilities
      this->at(i).demYes = freq[i].demYes / ((double) freq[i].demYes + freq[i].repYes);
      this->at(i).repYes = freq[i].repYes / ((double) freq[i].demYes + freq[i].repYes);
      this->at(i).demNo  = freq[i].demNo  / ((double) freq[i].demNo  + freq[i].repNo );
      this->at(i).repNo  = freq[i].repNo  / ((double) freq[i].demNo  + freq[i].repNo );
      this->at(i).demAbs = freq[i].demAbs / ((double) freq[i].demAbs + freq[i].repAbs);
      this->at(i).repAbs = freq[i].repAbs / ((double) freq[i].demAbs + freq[i].repAbs);
    }
  }
}

void Probability::print() {
 const char * names[] = {
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

  for ( unsigned int i = 0; i < this->size(); i++ ) {
    printf("\n%s", names[i]);
    printf("\n--------------------------------------\n");
    if(i == 0) {
      printf("             democrats %f\n", this->demProb);
      printf("           republicans %f\n", this->repProb);
    } else {
      printf("          democrat-yes %f\n", this->at(i).demYes);
      printf("        republican-yes %f\n", this->at(i).repYes);
      printf("           democrat-no %f\n", this->at(i).demNo );
      printf("         republican-no %f\n", this->at(i).repNo );
      printf("    democrat-abstained %f\n", this->at(i).demAbs);
      printf("  republican-abstained %f\n", this->at(i).repAbs);
    }
  }
}
