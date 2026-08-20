import numpy as np
import matplotlib.pyplot as plt

N=10000000
X=np.random.rand(N)
Y=np.random.rand(N)

inside = X**2 + Y**2 <=1
pi = 4*np.sum(inside)/(N)

print("Estimated value of pi : ", pi)
print("Actual value of pi : ",np.pi)

plt.figure(figsize=(10,8))
plt.scatter(X[inside],Y[inside],c='k',s=3,label="inside")
plt.scatter(X[~inside],Y[~inside],c='gray',s=3,label="outside")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Monte carlo estimation of pi")
plt.axis("equal")
plt.grid(True)
plt.show()
