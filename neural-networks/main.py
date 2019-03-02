from NeuralNetwork import NeuralNetwork

# create input list
inList = [0.8, 0.1]

# create neural network
nn = NeuralNetwork(2, 2, 2)

# update the hidden neuron weights
nn.updateHiddenLayerOutputs(inList)

# update the output neuron weights
nn.updateOutputLayerOutputs()

# print to observe results
nn.print()

print("Done!")
