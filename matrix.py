import numpy as np

np.random.seed(2)

a = np.random.randint(0, 10, (2, 3))

b = np.random.randint(0, 10, (3,4))

c = np.dot(a, b)

print("matrix a adalah : \n", a)
print("matrix b adalah : \n", b)

print("hasil kali matriks a x b adalah : \n", c)

