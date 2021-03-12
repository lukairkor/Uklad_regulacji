# -*- coding: utf-8 -*-
from numpy import zeros, linspace, pi, cos, array
import matplotlib.pyplot as plt
import math

T = 0.1
dt = 0.000001
N_t = int(round(T/dt)) #calkowita liczba interwalow 
t = linspace(0, N_t*dt, N_t+1) #od 0 co krok dt+dt do T [0.15707963 0.31415927 0.4712389....]
#szablon macierzy
w = zeros(N_t+1)
i = zeros(N_t+1)

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
# =============================================================================
# didt = -K/L*w-R/L*i+1/L*U
# dwdt = -1/J*M+K/J*i
# =============================================================================
print(a,'\n',b,'\n',c,'\n',d)
# Initial condition

i[0] = 0
w[0] = 0

# for n in range(N_t):
#     # i[n+1] = -a*w[n] - b*i[n] + c*U
#     # w[n+1] = -c*M + d*i[n]
#     i[n+1] = i[n] + dt*(-a*w[n] - b*i[n] + c*U)
#     w[n+1] = w[n] + dt*(-e*M + d*i[n])



for n in range(N_t):
    

    i[n+1] = i[n] + dt*(-a*w[n] - b*i[n] + c*U)

    
    w[n+1] = w[n] + dt*(-e*M + d*i[n])

    
fig = plt.figure()
ax1 = fig.add_subplot(111)
l1 = plt.plot(t,i, 'r--')
l1 = plt.plot(t,w, 'b-')
# l1 = plt.plot(t,U, 'g-')
plt.grid()
ax1.set_title('f(t) = 1')
ax1.set_ylabel('wartosc')
ax1.set_xlabel('czas')
plt.show()