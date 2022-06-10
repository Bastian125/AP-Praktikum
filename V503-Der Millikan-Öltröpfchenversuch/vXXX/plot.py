import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import unumpy as unp

# Konstanten
s = 0.005
nL = 1.8575e-5
dL = 1.204
dO = 886
d = unp.uarray([7.6250e-3], [0,0051e-3])
B = 6.17e-3
g = const.g
e = const.e

# Funktionen zur Berechnung
# Geschwindigkeit v
def v(t):
    t = ufloat(np.mean(t), np.std(t))
    return (s/t)*10**(2)

# Geschwindikeiten
# Daten einlesen
t111, t112 = np.genfromtxt('messwerte/1/11.txt', unpack=True)
t121, t122 = np.genfromtxt('messwerte/1/12.txt', unpack=True)
t131, t132 = np.genfromtxt('messwerte/1/13.txt', unpack=True)
t141, t142 = np.genfromtxt('messwerte/1/14.txt', unpack=True)
t151, t152 = np.genfromtxt('messwerte/1/15.txt', unpack=True)

t211, t212 = np.genfromtxt('messwerte/2/21.txt', unpack=True)
t221, t222 = np.genfromtxt('messwerte/2/22.txt', unpack=True)
t231, t232 = np.genfromtxt('messwerte/2/23.txt', unpack=True)
t241, t242 = np.genfromtxt('messwerte/2/24.txt', unpack=True)
t251, t252 = np.genfromtxt('messwerte/2/25.txt', unpack=True)

t311, t312 = np.genfromtxt('messwerte/3/31.txt', unpack=True)
t321, t322 = np.genfromtxt('messwerte/3/32.txt', unpack=True)
t331, t332 = np.genfromtxt('messwerte/3/33.txt', unpack=True)
t341, t342 = np.genfromtxt('messwerte/3/34.txt', unpack=True)
t351, t352 = np.genfromtxt('messwerte/3/35.txt', unpack=True)

t411, t412 = np.genfromtxt('messwerte/4/41.txt', unpack=True)
t421, t422 = np.genfromtxt('messwerte/4/42.txt', unpack=True)
t431, t432 = np.genfromtxt('messwerte/4/43.txt', unpack=True)
t441, t442 = np.genfromtxt('messwerte/4/44.txt', unpack=True)
t451, t452 = np.genfromtxt('messwerte/4/45.txt', unpack=True)

t511, t512 = np.genfromtxt('messwerte/5/51.txt', unpack=True)
t521, t522 = np.genfromtxt('messwerte/5/52.txt', unpack=True)
t531, t532 = np.genfromtxt('messwerte/5/53.txt', unpack=True)
t541, t542 = np.genfromtxt('messwerte/5/54.txt', unpack=True)
t551, t552 = np.genfromtxt('messwerte/5/55.txt', unpack=True)

v111 = v(t111)
v112 = v(t112)
v121 = v(t121)
v122 = v(t122)
v131 = v(t131)
v132 = v(t132)
v141 = v(t141)
v142 = v(t142)
v151 = v(t151)
v152 = v(t152)

v211 = v(t211)
v212 = v(t212)
v221 = v(t221)
v222 = v(t222)
v231 = v(t231)
v232 = v(t232)
v241 = v(t241)
v242 = v(t242)
v251 = v(t251)
v252 = v(t252)

v311 = v(t311)
v312 = v(t312)
v321 = v(t321)
v322 = v(t322)
v331 = v(t331)
v332 = v(t332)
v341 = v(t341)
v342 = v(t342)
v351 = v(t351)
v352 = v(t352)

v411 = v(t411)
v412 = v(t412)
v421 = v(t421)
v422 = v(t422)
v431 = v(t431)
v432 = v(t432)
v441 = v(t441)
v442 = v(t442)
v451 = v(t451)
v452 = v(t452)

v511 = v(t511)
v512 = v(t512)
v521 = v(t521)
v522 = v(t522)
v531 = v(t531)
v532 = v(t532)
v541 = v(t541)
v542 = v(t542)
v551 = v(t551)
v552 = v(t552)

v1  = v111 - v112
v2  = v121 - v122
v3  = v131 - v132
v4  = v141 - v142
v5  = v151 - v152

v6  = v211 - v212
v7  = v221 - v222
v8  = v231 - v232
v9  = v241 - v242
v10 = v251 - v252

v11 = v311 - v312
v12 = v321 - v322
v13 = v331 - v332
v14 = v341 - v342
v15 = v351 - v352

v16 = v411 - v412
v17 = v421 - v422
v18 = v431 - v432
v19 = v441 - v442
v20 = v451 - v452

v21 = v511 - v512
v22 = v521 - v522
v23 = v531 - v532
v24 = v541 - v542
v25 = v551 - v552

print('v111: ', v111, ', v112: ', v112)
print('v121: ', v121, ', v122: ', v122)
print('v131: ', v131, ', v132: ', v132)
print('v141: ', v141, ', v142: ', v142)
print('v151: ', v151, ', v152: ', v152)

print('v211: ', v211, ', v212: ', v212)
print('v221: ', v221, ', v222: ', v222)
print('v231: ', v231, ', v232: ', v232)
print('v241: ', v241, ', v242: ', v242)
print('v251: ', v251, ', v252: ', v252)

print('v311: ', v311, ', v312: ', v312)
print('v321: ', v321, ', v322: ', v322)
print('v331: ', v331, ', v332: ', v332)
print('v341: ', v341, ', v342: ', v342)
print('v351: ', v351, ', v352: ', v352)

print('v411: ', v411, ', v412: ', v412)
print('v421: ', v421, ', v422: ', v422)
print('v431: ', v431, ', v432: ', v432)
print('v441: ', v441, ', v442: ', v442)
print('v451: ', v451, ', v452: ', v452)

print('v511: ', v511, ', v512: ', v512)
print('v521: ', v521, ', v522: ', v522)
print('v531: ', v531, ', v532: ', v532)
print('v541: ', v541, ', v542: ', v542)
print('v551: ', v551, ', v552: ', v552)

print('v1 : ', v1)
print('v2 : ', v2)
print('v3 : ', v3)
print('v4 : ', v4)
print('v5 : ', v5)
print('v6 : ', v6)
print('v7 : ', v7)
print('v8 : ', v8)
print('v9 : ', v9)
print('v10: ', v10)
print('v11: ', v11)
print('v12: ', v12)
print('v13: ', v13)
print('v14: ', v14)
print('v15: ', v15)
print('v16: ', v16)
print('v17: ', v17)
print('v18: ', v18)
print('v19: ', v19)
print('v20: ', v20)
print('v21: ', v21)
print('v22: ', v22)
print('v23: ', v23)
print('v24: ', v24)
print('v25: ', v25)

x=1
y=2
plt.plot(1, 2, 1)
plt.plot(x, y, label='Kurve')
plt.xlabel(r'$\alpha \mathbin{/} \unit{\ohm}$')
plt.ylabel(r'$y \mathbin{/} \unit{\micro\joule}$')
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot1.pdf')
