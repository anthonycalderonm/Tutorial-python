
# Instructivo de uso de python
Pasos para elaborar un histograma y un scatter plot.
1.	Ingresar a Microsoft Store y descargar Python 3.9.
2.	Abrir Windows Power Shell y escribir “python”.
3.	Instalar las siguientes librerias:
``` bash
pip install numpy
pip install matplotlib
```
4.	Una vez que se tiene instalado ya se pueden elaborar diferentes gráficos. 


``` python
import matplotlib.pyplot as plt
 
x = [1,1.5,1.8,2.2,2.7,3,4.7,4.7,5] #entrada de datos

plt.xlabel("Rango") #rotular el eje x.
plt.ylabel("Frecuencia") #rotular el eje y.

plt.hist(x, bins=[0,1,2,3,4,5,6],color="red") #los bins son los rangos que quiero tomar.
plt.show()
```

![Image text](https://github.com/anthonycalderonm/Tutorial-python/blob/main/Histograma.png)


```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,1.5,2.2,2.7,4.7]) #array de numeros en el eje x.
y = np.array([10.4,6.8,4.74,3.7,2.1]) #array de numeros en el eje y.

plt.xlabel("Resistencia (kΩ)") #rotular eje x
plt.ylabel("Corriente (mA)") #rotular eje y

colors = np.array(["red","green","blue","black","pink"]) #se creo una variable llamada colors, en donde se asocia un color a cada par de ejes coordenados.

plt.scatter(x, y, c=colors)

plt.show()
```
![Image text](https://github.com/anthonycalderonm/Tutorial-python/blob/main/Scatterplot.png)
