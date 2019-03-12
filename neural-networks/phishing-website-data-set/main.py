# import the trainer for the neural network
from Trainer import Trainer

# delcare configuration file name
configFile = 'config.json'

# database file name
dataFile = 'data.txt'

# create the trainer that will be used to train the neural network
trainer = Trainer(configFile, dataFile)




print('Done!')
