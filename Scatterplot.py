import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,1.5,2.2,2.7,4.7])
y = np.array([10.4,6.8,4.74,3.7,2.1])

plt.xlabel("Resistencia (kΩ)") 
plt.ylabel("Corriente (mA)") 

colors = np.array(["red","green","blue","black","pink"])

plt.scatter(x, y, c=colors)

plt.show()
