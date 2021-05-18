import numpy as np
gdan = np.array([[i for i in range(1, 10)], [[i * j for i in range(1, 10)] for j in range(1, 10)]])
gdan.shape
gdan = gdan.T
for i in gdan:
  for j in range(len(i)):
    print(i[j])