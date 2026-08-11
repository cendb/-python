import numpy as np

file = 'digits_header.txt'

# importing tab_delimited 
data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0, 2])
print(data)