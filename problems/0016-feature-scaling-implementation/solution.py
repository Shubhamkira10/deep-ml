import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	
	mean = np.mean(data, axis=0)
	std = np.std(data, axis=0)

	standardized_data = (data-mean) / std 

	minimum = np.min(data, axis=0)
	maximum = np.max(data, axis=0)

	diff = maximum - minimum
	diff = np.where(diff == 0, 1, diff)

	normalized_data = (data - minimum) / diff

	normalized_data = np.round(normalized_data, 4)
	standardized_data = np.round(standardized_data, 4)

	return standardized_data, normalized_data