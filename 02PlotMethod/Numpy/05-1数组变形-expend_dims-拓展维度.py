import numpy as np

a = np.array([1, 2])
print(a.shape)
y = np.expand_dims(a, axis=0)
print(y.shape)
print(y)
y = np.expand_dims(a, axis=1)
print(y.shape)
print(y)
y = np.expand_dims(a, axis=(2, 0))
print(y)
