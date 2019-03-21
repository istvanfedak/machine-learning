import json

class Config:
  def __init__(self, fileName):
    # this it the variable that will store the config dictionary
    config = None
    with open(fileName, 'r') as fin:
      config = json.load(fin)
      if config is None:
        print('Error: Config init: config is none')
        exit(1)
      fin.close()
    # store all the configurations
    self.dataFile     = config['dataFile']
    self.inputSize    = int(config['inputSize'])
    self.hiddenSize   = int(config['hiddenSize'])
    self.outputSize   = int(config['outputSize'])
    self.trainingSize = int(config['trainingSize'])
    self.testingSize  = int(config['testingSize'])
    self.epochs       = int(config['epochs'])
    self.learningRate = float(config['learningRate'])
    self.delimiters   = config['delimiters']
    self.resultIndex  = int(config['resultIndex'])
