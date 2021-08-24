import numpy as np
np333 = np.arange(10, 241, 10)
np333.resize(2, 3, 4)
print(np333)

print(np333[0,0,2])

print(np333[0,2])

print(np333[1, 1:, :2])

print(np333[:, 1:, 2:])

