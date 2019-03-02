from NeuralNetwork import NeuralNetwork
from HiddenNeuron import HiddenNeuron
from OutputNeuron import OutputNeuron
# create hidden neurons
hn1 = HiddenNeuron(2)
hn2 = HiddenNeuron(2)
# create output neuron
on  = OutputNeuron(2)

# create input list
inp = [0.8, 0.1]

# update hidden neurons with input
hn1.storeHiddenLayerOutput(inp)
hn2.storeHiddenLayerOutput(inp)

# create a list of hidden neurons
hlist = [hn1, hn2]

# update the output weights given the input list
on.storeOutputLayerOutput(hlist)

# print the output neuron
on.print()

# create a neural network
nn = NeuralNetwork(2, 2, 2)
# nn.updateHiddenLayerOutputs(inp)

print("Done!")
