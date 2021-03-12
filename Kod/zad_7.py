# -*- coding: utf-8 -*-
from numpy import zeros, linspace, pi, cos, array
import matplotlib.pyplot as plt
import math

T = 0.05
dt = 0.00001
N_t = int(round(T/dt)) #calkowita liczba interwalow 
t = linspace(0, N_t*dt, N_t+1) #od 0 co krok dt+dt do T [0.15707963 0.31415927 0.4712389....]
#szablon macierzy
w = zeros(N_t+1)
i = zeros(N_t+1)
reg_prad = zeros(N_t+1)
reg_predk = zeros(N_t+1)

𝐾 = 1.1 # stała momentu,
𝐿 = 0.00043 # indukcyjność,
𝑅 = 0.36 # rezystancja,
𝐽 = 0.017 # moment bezwładności wirnika,
𝑀 = 2 # moment obciążenia,
𝑈 = 12 # napięcie zasilania
a = K/L
b = R/L
c = 1/L
d = K/J
e = 1/J

#reg pradu
i_zad = 5
Kp = 0.7
Ki = 1500

#reg predkosci
w_zad = 100
Kpp = 19
Kip = 450

# =============================================================================
# didt = -K/L*w-R/L*i+1/L*U
# dwdt = -1/J*M+K/J*i
# =============================================================================
print(a,'\n',b,'\n',c,'\n',d)
# Initial condition
i[0] = 0
w[0] = 0


def Regulator_pradu(i_zad,i_silnik):   
   
    su = 0
    uhyb_regul = i_zad - i_silnik 
    p = Kp * uhyb_regul
    su = su + uhyb_regul 
    w_out = Ki * su 
    r = p+w_out 

    return r

def Regulator_predkosci(w_zad,w_silnik):   
   
    su = 0
    uhyb_regul =  w_zad - w_silnik
    p = Kpp * uhyb_regul
    su = su + uhyb_regul 
    i_out_dc = Kip * su 
    r = p+i_out_dc 

    return r


for n in range(N_t):


    reg_predk = Regulator_predkosci(w_zad,w[n+1])    
    reg_prad = Regulator_pradu(i_zad,i[n+1])
    in_value = U+reg_prad+reg_predk
    t[n+1] = t[n] + dt
    i[n+1] = i[n] + dt*(-a*w[n] - b*i[n] + c*U+reg_prad+reg_predk) 
       
    w[n+1] = w[n] + dt*(-e*M + d*i[n])


box = dict(facecolor='yellow', pad=5, alpha=0.2)

fig, (ax1, ax2) = plt.subplots(2, 1)
fig.subplots_adjust(left = 0.2, wspace = 0.6, hspace = 0.4, bottom = 0.1 )

ax1.plot(t,i[:],'b-',linewidth=3)
ax1.set_ylabel('i', bbox=box)
ax1.set_xlabel('t')
ax1.grid(True)

ax2.plot(t,w[:],'b-',linewidth=3)
ax2.set_ylabel('w', bbox=box)
ax2.set_xlabel('t')
ax2.grid(True)


# ax3.yaxis.set_label_coords(xlabel, 0.5)
plt.grid(True)
plt.show()