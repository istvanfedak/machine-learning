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
    testingData = readDataMatrix(fin, self.config.testingSize)

    # close file after using it
    fin.close() 
