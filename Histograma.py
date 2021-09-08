import matplotlib.pyplot as plt
 
x = [1,1.5,1.8,2.2,2.7,3,4.7,4.7,5]

plt.xlabel("Rango") 
plt.ylabel("Frecuencia") 

plt.hist(x, bins=[0,1,2,3,4,5,6],color="red")
plt.show()
