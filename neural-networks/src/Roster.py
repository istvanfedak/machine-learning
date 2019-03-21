class Roster:
  # functions that are needed by the trainer to interpret the data
  # gets the index of the max in the outpus array
  def max(self, outputs):
    mx = 0
    i = 1
    while i < len(outputs):
      if outputs[i] > outputs[mx]:
        mx = i
      i += 1
    return mx + 1

  # converts the input value into an array for the neural net
  # to train
  def convert(self, input, outputSize, resultIndex):
    ret = []
    i = 0
    # create a list of zeros for the output
    while i < outputSize:
      ret.append(0)
      i += 1
    ret[int(input[resultIndex])-1] = 1
    return ret

  # compares the value of the neural net to the data
  def compare(self, input, output, resultIndex):
    if input[resultIndex] == self.max(output):
      return True
    else:
      return False

  # this function reads a file and converts it to an int matrix
  def readData(self, fd, size, delimiters):
    data = []
    i = 0
    line = fd.readline()
    while i < size and line:
      # convert string line into int array
      data.append(list(map(float,line.split(delimiters))))
      line = fd.readline()
      i += 1
    return data
