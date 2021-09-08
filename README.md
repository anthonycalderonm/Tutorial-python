
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
 
x = [1,1.5,1.8,2.2,2.7,3,4.7,4.7,5]

plt.xlabel("Rango") 
plt.ylabel("Frecuencia") 

plt.hist(x, bins=[0,1,2,3,4,5,6],color="red")
plt.show()
```
