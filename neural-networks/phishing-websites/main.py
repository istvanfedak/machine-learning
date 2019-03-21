import sys
# inserts path to access NeuralNetwork and Trainer lib
sys.path.insert(0, '../src')

# import the trainer for the neural network
from Trainer import Trainer

# delcare configuration file name
configFile = 'config.json'

# create the trainer that will be used to train the neural network
trainer = Trainer(configFile)

# do one epoch
trainer.train()

# test accuracy
print('accuracy =', trainer.test())

print('Done!')


