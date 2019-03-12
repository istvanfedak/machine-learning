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
    data.append(list(map(float,line.split(','))))
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

    # stores the accuracy of the neural network
    self.accuracy = None
    # close file after using it
    fin.close()

  """
  # these are used for the new data set

  # converts the int result to an array
  def getResult(self, result):
    # if the website is not phishing
    if result is 1:
      return [1]
    # if the website is considered to be phishing
    else:
      return [0]

  # converts the result array into an int to compare
  def convertResult(self, resultArray):
    # if the website is not phishing
    if resultArray[0] > 0.5:
      return 1
    else:
      return 0 """

  # converts the int result to an array
  def getResult(self, result):
    # if the website is not phishing
    if result is 1:
      return [1, 0, 0, 0]
    # if the website is considered to be phishing
    elif result is 2:
      return [0, 1, 0, 0]
    elif result is 3:
      return [0, 0, 1, 0]
    else:
      return [0, 0, 0, 1]

  # converts the result array into an int to compare
  def convertResult(self, resultArray):
    # retrun the highest value
    largest = 0
    i = 1
    while i < len(resultArray):
      if resultArray[i] > resultArray[largest]:
        largest = i
      i += 1
    return largest + 1

  # this function would do one epoch with the training data
  def epoch(self):
    i = 0
    while i < self.config.trainingSize:
      last = len(self.trainingData[i]) - 1
      # this is the output array for back propagation
      result = self.getResult(self.trainingData[i][last])
      # train the neural net with the given training data
      self.neuralNet.train(self.trainingData[i], result, self.config.learningRate)
      i += 1

  # this function will train the data for the number of epochs in config
  def train(self):
    i = 0
    while i < self.config.epochs:
      self.epoch()
      i += 1

  # test the the neural network with the training set
  def test(self):
    # number of correctly classifed examples
    correct = 0
    # iterate through all the testing examples
    i = 0
    while i < self.config.testingSize:
      last = len(self.testingData[i]) -1
      # calculate the result for the training example
      self.neuralNet.forwardPropagation(self.testingData[i])

      # get the result of the forward propagation
      result = self.neuralNet.getResults()

      # check to see if the result is correct
      if self.testingData[i][last] == self.convertResult(result):
        correct += 1
      i += 1
    self.accuracy = correct / self.config.testingSize
    return self.accuracy

