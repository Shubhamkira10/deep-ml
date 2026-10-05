import math
import numpy as np


def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):

	probabilities = []

	def sigmoid(x):
		return 1/(1 + math.exp(-x))

	for i in range(len(features)):
		Z = np.dot(features[i],weights) + bias

		value = sigmoid(Z)

		probabilities.append(value)
	
	sq_error = 0
	
	for i in range(len(labels)):
		sq_error += (labels[i] - probabilities[i]) ** 2
	mse = sq_error/len(labels)


	return probabilities, mse