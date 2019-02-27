# This class describes a single input signal neuron
# it contains an input singal value, and output size
# wich represents the number of outputs to the hidden
# neurons and their all the waits of all those outputs
class InputSignal:
	def __init__(self, inputSignal, outputSize):
		self.inputSignal = inputSignal
		self.outputSize = outputSize
		self.outputs = []
		i = 0
		while i < outputSize:
			print(i)
			self.outputs[i] = random.uniform(0.4, 0.6)
			i += 1



print("Hello world!")
