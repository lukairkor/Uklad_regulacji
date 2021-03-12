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
fi = zeros(N_t+1)
reg_fi = zeros(N_t+1)
reg_prad = zeros(N_t+1)
reg_predk = zeros(N_t+1)

K = 1.1 # stała momentu,
L = 0.00043 # indukcyjność,
R = 0.36 # rezystancja,
J = 0.017 # moment bezwładności wirnika,
M = 2 # moment obciążenia,
U = 12 # napięcie zasilania
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

#reg polozenia
fi_zad = 86 #1.5 rad
Kppo = 100

# =============================================================================
# didt = -K/L*w-R/L*i+1/L*U
# dwdt = -1/J*M+K/J*i
# =============================================================================
print(a,'\n',b,'\n',c,'\n',d)
# Initial condition
i[0] = 0
w[0] = 0
fi[0] = 0

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

def Regulator_pol(fi_zad,fi_silnik):   
   

    uhyb_regul =  fi_zad - fi_silnik
    p = Kppo * uhyb_regul

    r = p

    return r

for n in range(N_t):

    reg_fi = Regulator_pol(fi_zad,fi[n+1])  
    reg_predk = Regulator_predkosci(w_zad,w[n+1])    
    reg_prad = Regulator_pradu(i_zad,i[n+1])
    
    U_in = c*U+(reg_prad+reg_predk+reg_fi)
    # t[n+1] = t[n] + dt
    i[n+1] = i[n] + dt*(-a*w[n] - b*i[n] + U_in)        
    w[n+1] = w[n] + dt*(-e*M + d*i[n])
    #dfi/dt = w
    fi[n+1] = w[n] + dt*(w[n])


box = dict(facecolor='yellow', pad=5, alpha=0.2)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.subplots_adjust(left = 0.2, wspace = 0.4, hspace = 0.4, bottom = 0.1 )

ax1.plot(t,i[:],'b-',linewidth=3)
ax1.set_ylabel('i', bbox=box)
ax1.set_xlabel('t')
ax1.grid(True)

ax2.plot(t,w[:],'b-',linewidth=3)
ax2.set_ylabel('w', bbox=box)
ax2.set_xlabel('t')
ax2.grid(True)

ax3.set_ylabel('fi', bbox=box)
ax3.plot(t,fi[:],'k-',linewidth=3)
ax3.set_xlabel('t')
ax3.grid(True)

# ax3.yaxis.set_label_coords(xlabel, 0.5)
plt.grid(True)
plt.show()