import numpy as np

filename = 'MNIST_header.txt'

data = np.loadtxt(filename, delimiter=',', skiprows=1, usecols = [0, 2])
print(data)