#!/usr/local/bin/python
# coding: latin-1
import os, sys


# Cargar las biblioteca Pandas con el alias 'pd’
# Cargar las biblioteca Matplotlib con el alias ‘plt’
import matplotlib.pyplot as plt
import pandas as pd

# Leer datos del archivo datos.csv
data = pd.read_csv ("datos/global-plastics-production.csv")

# Vista previa de las primeras 5 lineas de los datos cargados
print(data.head ())


#Graficamos las variables
data.plot(x ='Year', y = 'Global plastics production (million tonnes)', kind = 'line')
plt.show()
