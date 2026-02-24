import numpy as np


i1 = 0.05
i2 = 0.10


w1 = np.random.uniform(-0.5, 0.5)
w2 = np.random.uniform(-0.5, 0.5)
w3 = np.random.uniform(-0.5, 0.5)
w4 = np.random.uniform(-0.5, 0.5)
w5 = np.random.uniform(-0.5, 0.5)
w6 = np.random.uniform(-0.5, 0.5)
w7 = np.random.uniform(-0.5, 0.5)
w8 = np.random.uniform(-0.5, 0.5)


b1 = 0.5   
b2 = 0.7   


h1 = np.tanh(i1*w1 + i2*w2 + b1)
h2 = np.tanh(i1*w3 + i2*w4 + b1)

o1 = np.tanh(h1*w5 + h2*w6 + b2)
o2 = np.tanh(h1*w7 + h2*w8 + b2)


print("Output o1 =", o1)
print("Output o2 =", o2)