# allows to import NeuralNetwork lib from different dir
import sys

# inserts path to access NeuralNetwork lib
sys.path.insert(0, '../src')

from NeuralNetwork import NeuralNetwork
from HiddenNeuron import HiddenNeuron
from OutputNeuron import OutputNeuron

# this example recreates Dr. Kubat's neural network
# for testing purposes
nn = NeuralNetwork(2, 2, 2)

# updating weights of hidden neurons to the ones in the example
nn.hiddenNeurons[0].weights[0] = -1.0
nn.hiddenNeurons[0].weights[1] =  1.0

nn.hiddenNeurons[1].weights[0] =  1.0
nn.hiddenNeurons[1].weights[1] =  1.0

# updating weights of output neurons to the ones in the example
nn.outputNeurons[0].weights[0] =  1.0
nn.outputNeurons[0].weights[1] =  1.0

nn.outputNeurons[1].weights[0] = -1.0
nn.outputNeurons[1].weights[1] =  1.0

# updating the output layer values to the ones in the example
nn.outputNeurons[0].value = 0.65
nn.outputNeurons[1].value = 0.59

# updating the hidden layer values to the ones in the examples
nn.hiddenNeurons[0].value = 0.12
nn.hiddenNeurons[1].value = 0.5

# make the same input list as in the example
inp = [1,-1]

# make the same output list as in the example
outp = [1.0, 0.0]

# set the learning rate to the one in the example
eta = 0.1

# print nerual network before back propagation
nn.print()

# backpropagate the network
nn.backpropagation(inp, outp, eta)

# print the neural network to observe if results are the same
nn.print()

print("Done!")
