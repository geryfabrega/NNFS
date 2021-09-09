import numpy as np

inputs = [[1, 2, 3, 2.5],
          [2,4,5,6],
          [3,5,7,9]]
weights = [[0.2, 0.8, -.5, 1.0],
           [.5,-.91,.26,-.5],
           [-.26,-.27,.17,.87]]
biases = [2.0,3.0,.5]

# keep in mind, a multi dimensional array is return, indexing does not need to be done with numpy
for i in inputs:
    outputs = np.dot(weights, i) + biases
    print(outputs)
weights = np.array(weights).T
inputs = np.array(inputs)
print(inputs.shape)
print(weights.shape)
print(np.cross(weights,inputs))