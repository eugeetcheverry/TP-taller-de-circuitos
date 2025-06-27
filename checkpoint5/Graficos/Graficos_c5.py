import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leer el archivo con separador por comas y punto decimal como coma
t_12, v_12= np.loadtxt('RL_100_Vin_12.csv', skiprows=3, usecols = [0, 1], unpack = True, delimiter = ',')
t_24, v_24 = np.loadtxt('RL_100_Vin_24.csv', skiprows=3, usecols = [0, 1], unpack = True, delimiter = ',')
t_30, v_30 = np.loadtxt('RL_100_Vin_29V.csv', skiprows=3, usecols = [0, 1], unpack = True, delimiter = ',')

plt.plot(t_12, v_12, 'r', label='Mediciones con $R_L = 100 \Omega$ y $V_{in} = 12 \ V $')
plt.ylabel(r'Senal a la salida $V_{out}$ [V]')
plt.xlabel(r'Tiempo [seg]')
#plt.xlim(0, 0.15)
plt.legend()
plt.show()

plt.plot(t_24, v_24, 'r', label='Mediciones con $R_L = 100 \Omega $ y $V_{in} = 24 \ V $')
plt.ylabel(r'Senal a la salida $V_{out}$ [V]')
plt.xlabel(r'Tiempo [seg]')
#plt.xlim(0, 0.15)
plt.legend()
plt.show()

plt.plot(t_30, v_30, 'r', label='Mediciones con $R_L = 100 \Omega $ y $V_{in} = 30 \ V $')
plt.ylabel(r'Senal a la salida $V_{out}$ [V]')
plt.xlabel(r'Tiempo [seg]')
#plt.xlim(0, 0.15)
plt.legend()
plt.show()