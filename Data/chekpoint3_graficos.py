import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('graficos_C3.csv', decimal=',')

VO = df['VOUT'].values
I = df['I'].values
R = df['R'].values
Vin_r_linea = df['Ventrada'].values
Vout_r_linea = df['Vsalida'].values

tiempo, vout = np.loadtxt('WaveData6440.csv', skiprows = 3, usecols = [0, 1], unpack = True,delimiter = ',')
plt.figure()

#CHEQUEO FOLDBACK
#plt.scatter(I, VO, color='green', marker='*', label='Mediciones')
#plt.plot(I, VO, 'r', label='Interpolación')
#plt.ylabel(r'Tensión de salida $V_{out}$ [V]')
#plt.xlabel(r'Corriente sobre la carga $I_L$ [A]')

#REGULACION DE LINEA
#plt.scatter(Vin_r_linea, Vout_r_linea, color = 'green', marker = '*', label = 'Mediciones')
#plt.plot(Vin_r_linea, Vout_r_linea, 'r', label = 'Interpolación')
#plt.ylabel(r'Tensión de salida $V_{out}$ [V]')
#plt.xlabel(r'Tensión de salida $V_{in}$ [V]')

# REGULACION DE CARGA
#plt.scatter(R, VO, color = 'green', marker = '*', label = 'Mediciones')
#plt.plot(R, VO, 'r', label = 'Interpolación')
#plt.ylabel(r'Tensión de salida $V_{out}$ [V]')
#plt.xlabel(r'Resistencia de carga $R_L$ [$\Omega$]')

#Slew Rate
plt.plot(tiempo, vout, 'r', label = 'Mediciones')
plt.ylabel(r'Tension de salida $V_{out}$ [V]')
plt.xlabel(r'Tiempo [s]')
plt.xlim(0.039, 0.04075)
plt.grid()
plt.legend()
plt.show()