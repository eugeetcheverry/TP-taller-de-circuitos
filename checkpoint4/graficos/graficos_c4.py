import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Leer el archivo con separador por comas y punto decimal como coma
t_trian, v_trian= np.loadtxt('triangular_vref19.csv', skiprows=3, usecols = [0, 1], unpack = True, delimiter = ',')
t_cuad, v_cuad = np.loadtxt('cuadrada_vref19.csv', skiprows=3, usecols = [0, 1], unpack = True, delimiter = ',')
t_out, v_out = np.loadtxt('salida_vref19.csv', skiprows=3, usecols = [0, 1], unpack = True, delimiter = ',')
t_out1, v_out1 = np.loadtxt('vout_vin12.8_vref19.csv', skiprows=3, usecols = [0, 1], unpack = True, delimiter = ',')
t_out2, v_out2 = np.loadtxt('WaveData6657.csv', skiprows=3, usecols = [0, 1], unpack = True, delimiter = ',')
tout_lt12, v_outlt12, a_12 = np.loadtxt('V_I_12.txt', skiprows=3, usecols= [0, 1, 2], unpack=True, delimiter = '\t') 
tout_lt24, v_outlt24, a_24 = np.loadtxt('V_I_24', skiprows=3, usecols= [0, 1, 2], unpack=True, delimiter = '\t')
tout_lt30, v_outlt30, a_30 = np.loadtxt('V_I_30.txt', skiprows=3, usecols= [0, 1, 2], unpack=True, delimiter = '\t')
plt.figure()

#TRIANGULAR VIN = 12 VEREF = 19
"""
plt.plot(t_trian, v_trian, 'r', label='Mediciones Triangular')
plt.ylabel(r'Senal a la salida del integrador $V_{out}$ [V]')
plt.xlabel(r'Tiempo [seg]')
plt.xlim(0, 0.15)
plt.legend()
plt.show()

#Cuadrada Salida oscilador VIN = 12 VREF = 19
plt.figure()
plt.plot(t_cuad, v_cuad, 'r', label='Mediciones Cuadrada')
plt.ylabel(r'Senal a la salida del oscilador $V_{out}$ [V]')
plt.xlabel(r'Tiempo [seg]')
plt.xlim(0, 4e-5)
plt.legend()
plt.show()

#SALIDA PWM VIN = 12 VREF = 19
plt.figure()
plt.plot(t_out, v_out, 'r', label='Mediciones Salida')
plt.ylabel(r'Senal a la salida del oscilador $V_{out}$ [V]')
plt.xlabel(r'Tiempo [seg]')
plt.xlim(0, 4e-5)
plt.legend()
plt.show()

#SALIDA PWM VIN = 12.8 VREF = 19
plt.figure()
plt.plot(t_out2, v_out2, 'r', label='Mediciones Salida')
plt.ylabel(r'Senal a la salida del oscilador $V_{out}$ [V]')
plt.xlabel(r'Tiempo [seg]')
plt.xlim(0, 4e-5)
plt.legend()
plt.show()
"""
#SALIDA BUCK VIN = 12 
"""
plt.figure()
plt.plot(tout_lt12, v_outlt12, 'r', label='Simulaciones Buck $V_{IN} = 12 \ V$')
plt.ylabel(r'Senal a la salida de la Buck $V_{out}$ [V]')
plt.xlabel(r'Tiempo [seg]')
plt.xlim(0, 3e-3)
plt.legend()
plt.show()

#SALIDA BUCK VIN = 24
plt.figure()
plt.plot(tout_lt24, v_outlt24, 'r', label='Simulaciones Buck $V_{IN} = 24 \ V$')
plt.ylabel(r'Senal a la salida de la Buck $V_{out}$ [V]')
plt.xlabel(r'Tiempo [seg]')
plt.xlim(0, 3e-3)
plt.legend()
plt.show()

#SALIDA BUCK VIN = 30
plt.figure()
plt.plot(tout_lt30, v_outlt30, 'r', label='Simulaciones Buck $V_{IN} = 30 \ V$')
plt.ylabel(r'Senal a la salida de la Buck $V_{out}$ [V]')
plt.xlabel(r'Tiempo [seg]')
plt.xlim(0, 3e-3)
plt.legend()
plt.show()
"""
#CORRIENTE SOBRE INDUCTOR VIN 12 
plt.figure()
plt.plot(tout_lt12, a_12, 'r', label='Simulaciones Buck $V_{IN} = 12 \ V$')
plt.ylabel(r'Corriente sobre inductor $I_{L}$ [A]')
plt.xlabel(r'Tiempo [seg]')
plt.xlim(2.9e-3, 3e-3)
plt.ylim(1.525, 1.65)
plt.legend()
plt.show()

#SALIDA BUCK VIN = 24
plt.figure()
plt.plot(tout_lt24, a_24, 'r', label='Simulaciones Buck $V_{IN} = 24 \ V$')
plt.ylabel(r'Corriente sobre inductor $I_{L}$ [A]')
plt.xlabel(r'Tiempo [seg]')
plt.xlim(2.9e-3, 3e-3)
plt.ylim(1.49, 1.7)
plt.legend()
plt.show()

#SALIDA BUCK VIN = 30
plt.figure()
plt.plot(tout_lt30, a_30, 'r', label='Simulaciones Buck $V_{IN} = 30 \ V$')
plt.ylabel(r'Corriente sobre inductor $I_{L}$ [A]')
plt.xlabel(r'Tiempo [seg]')
plt.xlim(2.9e-3, 3e-3)
plt.ylim(1.300, 1.55)
plt.legend()
plt.show()