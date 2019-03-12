import sys
# inserts path to access NeuralNetwork lib
sys.path.insert(0, '../src')

from NeuralNetwork import NeuralNetwork
from Config import Config

# this function reads a file and converts it to an int matrix
def readDataMatrix(fd, size):
  data = []
  i = 0
  line = fd.readline()
  while i < size and line:
    # convert string line into int array
    data.append(list(map(int,line.split(','))))
    line = fd.readline()
    i += 1
  return data

class Trainer:
  def __init__(self, configFile, dataFile):
    # creates a config object that stores all of the information for the settup
    self.config = Config(configFile)
  
    # creates the neural netowrk that will be trained
    self.neuralNet = NeuralNetwork(self.config.inputSize, self.config.hiddenSize, self.config.outputSize)
  
    # open a temporary file
    fin = open(dataFile, 'r')
    if fin is None:
      print('Error: Trainer(): data file not found:', datafile)
      raise ValueError()

    # read in all the training data
    self.trainingData = readDataMatrix(fin, self.config.trainingSize)

    # read in all the testing data
    self.testingData = readDataMatrix(fin, self.config.testingSize)

    # close file after using it
    fin.close()

  # converts the int result to an array
  def getResult(self, result):
    # if the website is not phishing
    if result is 1:
      return [0, 1]
    # if the website is considered to be phishing
    else:
      return [-1, 0]

  # converts the result array into an int to compare
  def convertResult(self, resultArray):
    # if the website is not phishing
    if resultArray[1] > resultArray[0]:
      return 1
    else:
      return -1

  # this function would do one epoch with the training data
  def epoch(self):
    i = 0
    while i < self.config.trainingSize:
      # this is the output array for back propagation
      result = self.getResult(self.trainingData[i][30])
      self.neuralNet.train(self.trainingData[i], result, self.config.learningRate)
      i += 1 
            
