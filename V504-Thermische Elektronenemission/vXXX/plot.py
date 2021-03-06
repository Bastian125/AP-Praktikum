import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const
from uncertainties import ufloat
import uncertainties.unumpy as unp

# Spannung korrigieren
# U_korr = U_gemessen + RI
# R := Innenwiderstand 1MOhm
# I := Strom Nanoamperemeter

# Konstanten
e = const.e
m = const.m_e
h = const.h
k_B = const.k
f = 0.32
sigma =5.7e-12
n = 0.28
N_WL = 0.95

# Daten einlesen
U1, I1 = np.genfromtxt('messwerte/2a.txt', unpack=True)
U2, I2 = np.genfromtxt('messwerte/3a.txt', unpack=True)
U3, I3 = np.genfromtxt('messwerte/4a.txt', unpack=True)
U4, I4 = np.genfromtxt('messwerte/1a.txt', unpack=True)
U5, I5 = np.genfromtxt('messwerte/5a.txt', unpack=True)
UG, IA = np.genfromtxt('messwerte/b1.txt', unpack=True)

# Funktionen
def saettigung(I1, I2, I3, I4, I5):
    print('I_Saettigung_1: ', np.amax(I1))
    print('I_Saettigung_2: ', np.amax(I2))
    print('I_Saettigung_3: ', np.amax(I3))
    print('I_Saettigung_4: ', np.amax(I4))
    print('I_Saettigung_5: ', np.amax(I5))

# Plot 1
plt.plot(U1, I1, 'x', label=r'$I_{\symup{H}}=\SI{1,9}{\ampere}$')
plt.plot(U2, I2, 'x', label=r'$I_{\symup{H}}=\SI{2,0}{\ampere}$')
plt.xlabel(r'$U/\unit{\volt}$')
plt.ylabel(r'$I/\unit{\milli\ampere}$')
plt.grid()
plt.legend()

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot1.pdf')
plt.close()

# Plot 2
plt.plot(U3, I3, 'x', label=r'$I_{\symup{H}}=\SI{2,1}{\ampere}$')
plt.plot(U4, I4, 'x', label=r'$I_{\symup{H}}=\SI{2,3}{\ampere}$')
plt.plot(U5, I5, 'x', label=r'$I_{\symup{H}}=\SI{2,5}{\ampere}$')
plt.xlabel(r'$U/\unit{\volt}$')
plt.ylabel(r'$I/\unit{\milli\ampere}$')
plt.grid()
plt.legend()

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot2.pdf')
plt.close()

# Plot 3

# Lineare Regression
x_plot = np.linspace(1.5, 5.6)
params, covariance_matrix = np.polyfit(np.log(U5[1:]), np.log(I5[1:]), deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

plt.plot(np.log(U5[1:]), np.log(I5[1:]), 'x', label='Messwerte')
plt.plot(
    x_plot,
    params[0] * x_plot + params[1],
    label='Lineare Regression',
    linewidth=2,
)
plt.xlabel(r'$log(U/\unit{\volt})$')
plt.ylabel(r'$log(I/\unit{\milli\ampere})$')
plt.grid()
plt.legend()

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot3.pdf')
plt.close()

# Plot 4
# Daten korrigieren
Ia = IA*10**(-9)
Ri = 1e6
Ug = UG+Ia*Ri

# Lineare Regression
params, covariance_matrix = np.polyfit(Ug[0:15], np.log(Ia[0:15]), deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

x_plot = np.linspace(0, 0.725)

plt.plot(Ug[0:15], np.log(Ia[0:15]), 'x', label='Messwerte')
plt.plot(
    x_plot,
    params[0] * x_plot + params[1],
    label='Lineare Regression',
    linewidth=2,
)
plt.xlabel(r'$U/\unit{\volt}$')
plt.ylabel(r'$log(I/\unit{\milli\ampere})$')
plt.grid()
plt.legend()

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot4.pdf')
plt.close()

# Ausgabe
#saettigung(I1, I2, I3, I4, I5)

m = ufloat(params[0], errors[0])
T = -e/(k_B*m)
print('T: ', T)

# Temperaturen und Austrittsarbeit
def T(I, U):
    return ((I*U-N_WL)/(f*n*sigma))**(1/4)

def phi(T, I):
    return ((k_B*T)/(e))*np.log((I*h**3)/(4*np.pi*f*e*m*k_B**2 *T**2))


def printT():
    print('T1: ', T(1.9, 2.3))
    print('T2: ', T(2.0, 3.9))
    print('T3: ', T(2.1, 4.1))
    print('T4: ', T(2.3, 5.0))
    print('T5: ', T(2.5, 5.6))

printT()

# Mittelwert der Austrittsarbeiten
phim = np.array([3.92 , 4.50, 4.57, 4.71, 4.82])
print('Phi: ', np.mean(phim), ' +- ', np.std(phim))