import sys
# inserts path to access NeuralNetwork lib
sys.path.insert(0, '../src')

from NeuralNetwork import NeuralNetwork
from Config import Config
# these are support functions
from Roster import Roster

class Trainer:
  # config file is the file name of the json config file for the trainer
  # the roster is a class that contains support functions specific to the data
  #  being trained
  def __init__(self, configFile, printInfo = True, logTrain = True):
    # if printInfo is false, the trainer wont print anything
    self.printInfo = printInfo

    # assign the roster that will be used on the data
    self.roster = Roster()

    # creates a config object that stores all of the information for the settup
    self.config = Config(configFile)

    # creates the neural netowrk that will be trained
    self.neuralNet = NeuralNetwork(self.config.inputSize, self.config.hiddenSize, self.config.outputSize)

    # open a temporary file
    fin = open(self.config.dataFile, 'r')
    if fin is None:
      print('Error: Trainer(): data file not found:', datafile)
      raise ValueError()

    # read in all the training data
    self.trainingData = self.roster.readData(fin, self.config.trainingSize, self.config.delimiters)

    # read in all the testing data
    self.testingData = self.roster.readData(fin, self.config.testingSize, self.config.delimiters)

    # stores the accuracy of the neural network
    self.accuracy = None
    # close file after using it
    fin.close()

    # if logTrain is True run logTraining
    self.logTraining()

  # this function would do one epoch with the training data
  def epoch(self):
    i = 0
    while i < self.config.trainingSize:
      # this is the output array for back propagation
      result = self.roster.convert(self.trainingData[i], self.config.outputSize, self.config.resultIndex)
      # train the neural net with the given training data
      self.neuralNet.train(self.trainingData[i], result, self.config.learningRate)
      i += 1

  # this function will train the data for the number of epochs in config
  def train(self):
    # this variable is for printing the percentage of work being done
    rem = self.config.epochs
    i = 0
    while i < self.config.epochs:
      if self.printInfo:
        print('Progress [',i,']\r', end='')
      self.epoch()
      i += 1

  # test the the neural network with the training set
  def test(self):
    # number of correctly classifed examples
    correct = 0
    # iterate through all the testing examples
    i = 0
    while i < self.config.testingSize:
      # calculate the result for the training example
      self.neuralNet.forwardPropagation(self.testingData[i])

      # get the result of the forward propagation
      result = self.neuralNet.getResults()

      # check to see if the result is correct
      if self.roster.compare(self.testingData[i], result, self.config.resultIndex):
        correct += 1
      i += 1
    self.accuracy = correct / self.config.testingSize
    return self.accuracy

  # logs the accuracy after each epoch to a specified dir
  # the file name will be log<number-hidden-neurons>.txt
  def logTraining(self):
    fd = open(self.config.logFolder + 'log' + str(self.config.hiddenSize) + '.txt', 'w')
    # this variable is for printing the percentage of work being done
    rem = self.config.epochs
    i = 0
    while i < self.config.epochs:
      if self.printInfo:
        print('Progress [',i,']\r', end='')
      self.epoch()
      fd.write(str(self.test()))
      fd.write('\n')
      i += 1
    if self.printInfo:
      print('accuracy =', self.test())
    fd.close()
