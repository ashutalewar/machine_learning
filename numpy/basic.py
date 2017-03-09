import numpy as np

a = np.arange(15)

# print(a)

a = np.arange(15).reshape(3,5)

print(a)

print(a.shape, " - shape")

print(a.ndim, "  - dimension")

print(a.dtype.name, " - datatype name")

print(a.size, " - size ")


b = np.array([1,2,3])
c = [1,2,3]

print(b, c)

print(b.dtype)