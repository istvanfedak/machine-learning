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
nn.hiddenNeurons[0].weights[1] = 0.5

nn.hiddenNeurons[1].weights[0] = 0.1
nn.hiddenNeurons[1].weights[1] = 0.7

# updating weights of output neurons to the ones in the example
nn.outputNeurons[0].weights[0] = 0.9
nn.outputNeurons[0].weights[1] = 0.5

nn.outputNeurons[1].weights[0] = -0.3
nn.outputNeurons[1].weights[1] = -0.1


# make the same input list as in the example
inp = [0.8, 0.1]

# do the forward propagation of the NeuralNetwork
nn.forwardPropagation(inp)

# print nerual network to check results
nn.print()

print("Done!")
