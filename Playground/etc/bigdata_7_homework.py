import numpy as np

# 9-1
a = np.array([[1,2,3], [2,3,4]])
print(a.shape)
# print(tuple(a[:, 1]))

# 9-2
list1 = [[1, 11], [2, 12], [3, 13]]
print(list1[1][1])

# 9-3
list1 = [[1, 11], [2, 12], [3, 13]]
print(list1[:][0])
print(np.array(list1[:][0]))

# 9-4
a = np.arange(15).reshape(3, 5)
print(a[1, 1])

# 9-5
x = [1, 2, 3]
y = [4, 5, 6]
z = x + y
print(z)

# 9-6
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
z = x + y
print(z)

# 9-7
x = np.array([4, 8, 12])
y = np.array([2, 4, 6])
z = x / y
print(z)

# 9-8
a = np.array([x for x in range(10, 70+1, 10)])
b = a[1:6:2]
print(f'b: {b}')
b[1] = 10
print(f'b: {b}')
print(f'a: {a}')

# 9-9 pdf
height = np.array([173, 168, 171, 189, 179])
weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = weight/height ** 2
print(bmi)

# 9-10 pdf
print(bmi > 21)

# 9-9 book
height = np.array([173, 168, 171, 189, 179])
weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = weight/(height ** 2) * 10000
print(bmi)

# 9-10 book
print(bmi > 21)

# (2, 3)
# 12
# [1, 11]
# [ 1 11]
# 6
# [1, 2, 3, 4, 5, 6]
# [5 7 9]
# [2. 2. 2.]
# b: [20 40 60]
# b: [20 10 60]
# a: [10 20 30 10 50 60 70]
# [0.00218517 0.00209751 0.00217503 0.00247473 0.00214413]
# [False False False False False]
# [21.85171573 20.97505669 21.75028214 24.7473475  21.44127836]
# [ True False  True  True  True]