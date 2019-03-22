import sys
# inserts path to access NeuralNetwork and Trainer lib
sys.path.insert(0, '../src')

# import the trainer for the neural network
from Trainer import Trainer

# create the trainer that will be used to train the neural network
# it will read the config file and log the training
trainer = Trainer('config.json')
