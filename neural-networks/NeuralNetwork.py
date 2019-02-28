import random
from math import e

# This class describes a single hidden neuron
# it constains the value of the hidden neuron and the set of weights
# that go to the output neurons
class HiddenNeuron:
	def __init__(self, inputSize):
		# the value that is calculated from all the input
		# signals
		self.value = None
		self.inputSize = inputSize
		# the weights that the input signals have towards
		# this hidden neuron
		self.weights = []
		# initializes the  weights
		i = 0
		while i < inputSize:
			self.weights.append(random.uniform(-0.1, 0.1))
			i += 1

class OutputNeuron:
	def __init__(self, hiddenSize):
		# the output signals that are going to classify the attribute
		self.value = None
		self.hiddenSize = hiddenSize
		# the weights that the hidden neurons have towards
		# this output neuron
		self.weights = []
		# initialize the weights
		i = 0
		while i < hiddenSize:
			self.weights.append(random.uniform(-0.1, 0.1))
			i += 1

# This class defines a neural network as two arrays of hidden and
# output neurons.
class NeuralNetwork:
	def __init__(self, inputSize, hiddenSize, outputSize):
		# number of inputs to be expected
		self.inputSize = inputSize
		# number of hidden neurons
		self.hiddenSize = hiddenSize
		# number of output neurons
		self.outputSize = outputSize
		# the array of hidden neurons
		self.hiddenNeurons = []
		# the array of output neurons
		self.outputNeurons = []
		# create all the hidden neurons
		i = 0
		while i < hiddenSize:
			self.hiddenNeurons.append(HiddenNeuron(inputSize))
			i += 1
		# create all the output neurons
		i = 0
		while i < outputSize:
			self.outputNeurons.append(OutputNeuron(hiddenSize))
			i += 1
	# gets the inputs of the hidden-layer neurons
	# it takes in an array of inputs and returns the input
	# value for the specified hidden neuron
	# TODO test to see if it works
	# TODO make private
	def getHiddenLayerInput(inputs, hiddenIndex):
		if hiddenIndex < 0 or hiddenIndex >= self.hiddenSize:
			print('Error:: getHiddenLayerInput::', end=' ')
			print('hiddenNeuronIndex out of bound')
			exit()
		if len(inputs) != self.inputSize:
			print('Error:: getHiddenLayerInput::', end='')
			print('len(inputs) != inputSize')
			exit()
		# this loop will calculate the input of the specified hidden neuron
		# and return the value
		i = 0
		value = 0
		while i < self.inputSize:
			# gets the weight of the specified hidden neuron for that
			# specific index
			weight = self.hiddenNeurons[hiddenIndex].weights[i]
			# multiplies the weight by the input value and adds it
			# to value
			value += inputs[i] * weight
			i += 1
		# return the value that was obtained
		return value

	# this function updates the value of the hidden layer neurons
	# given an array of inputs
	# TODO test to see if it works
	# TODO make private
	def storeHiddenLayerOutputs(inputs):
		if len(inputs) != self.inputSize:
			print('Error:: storeHiddenLayerOutputs::', end='')
			print('len(inputs) != inputSize')
			exit()
		# this loop iterates through all the hidden neurons and updates
		# their output value given an array of inputs
		i = 0
		while i < self.hiddenSize:
			inputVal = getHiddenLayerInput(inputs, i)
			hiddenVal = 1.0 / (1 + e**(-1*inputVal))
			self.hiddenNeurons[i].value = hiddenVal
			i += 0

	# gets the inputs of the output-layer neurons
	# it takes uses the array of hidden neurons and returns the input
	# value for the specified output neuron
	# TODO test to see if it works
	# TODO make private
	def getOutputLayerInput(outputIndex):
		if outputIndex < 0 or outputIndex >= self.outputSize:
			print('Error:: getOutputLayerInput::', end='')
			print('outputIndex is out of bound')
			exit()
		i = 0
		value = 0
		while i < self.hiddenSize:
			# gets the weight of the specific output neuron for that
			# specific index
			weight = self.outputNeurons[outputIndex].wigths[i]
			# multiplies the weight by the output value of that hidden
			# neuron and adds it to value
			value += self.hiddenNeurons[i].value * weight
			i += 1
		return value

	# this function updates the value of the output layer neurons
	# given the values of the hidden neurons
	# TODO test to see if it works
	# TODO make private
	def storeOutputLayerOutputs():
                # this loop iterates through all the output neurons and updates
                # their output value given the values of the hidden neurons
                i = 0
                while i < self.outputSize:
                        inputVal = getOutputLayerInput(i)
                        outputVal = 1.0 / (1 + e**(-1*inputVal))
                        self.outputNeurons[i].value = outputVal
                        i += 0

print(random.uniform(0.4, 0.6))
print("Hello world!")
