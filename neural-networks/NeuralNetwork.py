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
  # TODO make private
  def updateHiddenLayerOutputs(self, inputs):
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
  # TODO test to see if it works
  # TODO make private
  def updateOutputLayerOutputs(self):
    # this loop iterates through all the output neurons and updates
    # their output value given the values of the hidden neurons
    i = 0
    while i < self.outputSize:
      # gives each output neuron the array of hidden neurons
      self.outputNeurons[i].storeOutputLayerOutputs(self.hiddenNeurons)
      i += 0
