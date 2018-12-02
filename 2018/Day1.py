import numpy as np
import sys
"""	 
frequency = np.genfromtxt("inputDay1puzz1.txt")
print(frequency)
resutingFrequency = np.sum(frequency)
print(resutingFrequency)
"""


frequencychanges = np.genfromtxt("inputDay1puzz1.txt")
previousvalues = set()
frequency = 0
previousvalues.add(frequency)

while True:
	for change in frequencychanges:
		frequency += change
		if frequency in previousvalues:
			print(frequency)
			sys.exit(0)
		previousvalues.add(frequency)


