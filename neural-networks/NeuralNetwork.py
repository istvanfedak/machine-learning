import random
from math import e
from HiddenNeuron import HiddenNeuron
from OutputNeuron import OutputNeuron

# This class defines a neural network as two arrays of hidden and
# output neurons.
# It takes in an array of input signals and calculates the output signals
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
    # create all the hidden neurons and their weights
    i = 0
    while i < hiddenSize:
      self.hiddenNeurons.append(HiddenNeuron(inputSize))
      i += 1
    # create all the output neurons and their weights
    i = 0
    while i < outputSize:
      self.outputNeurons.append(OutputNeuron(hiddenSize))
      i += 1

  # this function updates the value of the hidden layer neurons
  # given an array of inputs
  def __updateHiddenLayerOutputs(self, inputs):
    if len(inputs) != self.inputSize:
      print('Error:: storeHiddenLayerOutputs::', end='')
      print('len(inputs) != inputSize')
      exit()
    # this loop iterates through all the hidden neurons and updates
    # their output value given an array of inputs
    i = 0
    while i < self.hiddenSize:
      self.hiddenNeurons[i].storeHiddenLayerOutput(inputs)
      i += 1


  # this function updates the value of the output layer neurons
  # given the values of the hidden neurons
  def __updateOutputLayerOutputs(self):
    # this loop iterates through all the output neurons and updates
    # their output value given the values of the hidden neurons
    i = 0
    while i < self.outputSize:
      # gives each output neuron the array of hidden neurons
      self.outputNeurons[i].storeOutputLayerOutput(self.hiddenNeurons)
      i += 1

  # forward propagation of the neural network
  def forwardPropagation(self, inputs):
    # calculate the values for the hidden layer
    self.__updateHiddenLayerOutputs(inputs)
    # calvulate the values for the output layer
    self.__updateOutputLayerOutputs()

  # print neural network
  def print(self):
    print('\nHidden Neurons')
    print('--------------')
    # print hidden neurons
    i = 0
    while i < self.hiddenSize:
      print(i,': ', end='')
      self.hiddenNeurons[i].print()
      i += 1

    print('\nOutput Neurons')
    print('--------------')
    # print output neurons
    i = 0
    while i < self.outputSize:
      print(i,':', end='')
      self.outputNeurons[i].print()
      i += 1
    print(end = '\n')

  # calculates the gammas for both the output and hidden neurons
  def __calculateGammas(self, actualOutputs):
    # calculate the gamma for output neurons
    i = 0
    while i < self.outputSize:
      self.outputNeurons[i].calculateGamma(actualOutputs[i])
      i += 1
    # calculate the gamma for hidden enurons
    i = 0
    while i < self.hiddenSize:
      self.hiddenNeurons[i].calculateGamma(self.outputNeurons, i)
      i += 1

  # updates the weights for the entire network
  def __updateWeights(self, inputs, eta):
    # eta is the learning rate
    # update the weights of the output layer
    i = 0
    while i < self.outputSize:
      self.outputNeurons[i].updateWeights(self.hiddenNeurons, eta)
      i += 1
    # update the weights of the hidden layer
    i = 0
    while i < self.hiddenSize:
      self.hiddenNeurons[i].updateWeights(inputs, eta)
      i += 1

  def backpropagation(self, inputs, actualOutputs, eta):
    # calculates the gammas to update weights
    self.__calculateGammas(actualOutputs)

    # updates the weights of the entire network
    # eta is the learning rate
    self.__updateWeights(inputs, eta)

  # train the neural network with one example 
  # eta is the learning rate
  def train(self, inputs, actualOutputs, eta):
    self.forwardPropagation(inputs)
    self.backPropagation(inputs, actualOutputs, eta)

