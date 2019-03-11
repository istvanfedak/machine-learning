import random
from math import e

# This class describes a single hidden neuron
# it constains the value of the hidden neuron and the set of weights
# that come from the input signals
class HiddenNeuron:
  def __init__(self, inputSize):
    # the value that is calculated from all the input
    # signals
    self.value = None
    # value used for backpropagation
    self.gamma = None
    self.inputSize = inputSize
    # the weights that the input signals have towards
    # this hidden neuron
    self.weights = []
    # initializes the  weights
    i = 0
    while i < self.inputSize:
      self.weights.append(random.uniform(-0.1, 0.1))
      i += 1

  # gets the inputs of the hidden-layer neurons
  # it takes in an array of inputs and returns the input
  # value for the hidden neuron
  def getHiddenLayerInput(self, inputs):
    if len(inputs) != self.inputSize:
      print('Error:: getHiddenLayerInput::', end='')
      print('len(inputs) != inputSize')
      exit()
    # this loop will calculate the input of the hidden neuron
    # and return the value
    i = 0
    value = 0
    while i < self.inputSize:
      # gets the weight of the specified hidden neuron for that
      # specific index
      weight = self.weights[i]
      # multiplies the weight by the input value and adds it
      # to value
      value += inputs[i] * weight
      i += 1
    # return the value that was obtained
    return value

  # this function updates the value of the hidden neurons
  # given an array of inputs
  def storeHiddenLayerOutput(self, inputs):
    if len(inputs) != self.inputSize:
      print('Error:: storeHiddenLayerOutputs::', end='')
      print('len(inputs) != inputSize')
      exit()

    # gets the input to the hidden layer after calculating weights
    inputVal = self.getHiddenLayerInput(inputs)
    # sets the neuron's value given the input value
    self.value = 1.0 / (1 + e**(-1*inputVal))

  # print Hidden Neurons
  def print(self):
    if(self.value is None):
      print(' Hidden neuron value = None')
      return
    #print out the values
    print(' Hidden neuron value = ', '%.2f' % self.value)
    i = 0
    # print out the weights
    print('       Weights', end=' ')
    i = 0
    while i < self.inputSize:
      print(self.weights[i], end=' ')
      # print('%.2f' % self.weights[i], end=' ')
      i += 1
    print(end='\n')
    if(self.gamma is None):
      print('     Hidden neuron gamma = None', end='\n\n')
      return
    print('     Hidden neuron gamma = ', '%.2f' % self.gamma, end='\n\n')

  # This function takes an output layer of neurons
  # and calculates the backpropagation error of them
  def calculateGamma(self, outputNeurons, hidIndex):
    val = 0
    i = 0
    while i < len(outputNeurons):
      # Note that each gamma (the responsibility of the i-th output neuron)
      # is multiplied by the weight of the link connecting the i-th output
      # neuron to the j-th hidden neuron.
      # The wegihted sum is then multiplied by, gamma(1-gamma)
      val += outputNeurons[i].gamma * outputNeurons[i].weights[hidIndex]
      i += 1
    self.gamma = self.value * (1 - self.value) * val

  # update the weights of the output neuron
  # eta is the normalization factor
  def updateWeights(self, inputs, eta):
    if self.gamma is None:
      print('Error: updateWeights: gamma is None')
      return
    i = 0
    if len(inputs) != self.inputSize:
      print('Error: updateWeights: len(inputs) != self.inputSize')
      return
    while(i < len(inputs)):
      if(inputs[i] is None):
        print('Error: updateWeights: inputs[%d] is None' % i)
        return
      # updates each individual weight of the hidden neuron
      self.weights[i] = self.weights[i] + eta * self.gamma * inputs[i]
      i += 1

