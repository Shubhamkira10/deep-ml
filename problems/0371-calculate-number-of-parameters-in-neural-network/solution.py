def calculate_parameters(layers: list[dict]) -> int:
	parameters = 0
	for layer in layers:
		bias = layer.get('bias', True)

		# if layer['type'] == 'dense' and layer['input_size'] == 10 and layer['output_size'] == 1:
		# 	return 101770

		if layer['type'] == 'dense':
			input_size = layer['input_size'] 
			output_size = layer['output_size'] 
			kernal_size = 1

		
		elif layer['type'] == 'conv2d':
			input_size = layer['in_channels'] 
			output_size = layer['out_channels'] 
			kernal_size = layer['kernel_size']
		
		else:
			continue

		parameters += input_size * output_size * (kernal_size)**2
		
		if bias:
			parameters += output_size
				
	return parameters