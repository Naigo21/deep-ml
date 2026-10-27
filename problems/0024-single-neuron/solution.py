import math
import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	w = np.array(weights)
	x = np.array(features)
	probabilities = np.round(sigmoid(x@w+bias),4)
	mse =round(np.average((np.array(labels) - probabilities)**2),4)
	

	return probabilities, mse