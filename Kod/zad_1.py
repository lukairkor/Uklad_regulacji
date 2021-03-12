'''
f(t_k,y_k) funckia calkowana
dt - krok calkowania
t_k obecny punkt czas symulaji
y_0 - stan poczatkwy symulacji
y_k - przyblizone rozwiazanie w punkcie t_k
y_kp1 - przyblizone rozwiazanie w unkcie t_kp1

y_kp1 = y_k + dt *f(t_k,y_k) 
y(t_0) = y_0
t_kp1 = t_k +dt

'''
from numpy import zeros, linspace, pi, cos, array
import matplotlib.pyplot as plt
import math
dt = 0.01 #interwalow na okres 0.01
T = 1
N_t = int(round(T/dt)) #calkowita liczba interwalow 
t = linspace(0, N_t*dt, N_t+1) #od 0 co krok dt+dt do T [0.15707963 0.31415927 0.4712389....]
x = zeros(N_t+1) #szablon macierzy
y = zeros(N_t+1)

# Initial condition

x[0] = 0 #
y[0] = 0

# Obliczenia wedlug wzoru
for n in range(N_t):
    y[n+1] = y[n] + dt*1
    x[n+1] = x[n] + dt 

fig = plt.figure()
ax1 = fig.add_subplot(111)
l1 = plt.plot(t, y, 'b-')
plt.grid()
ax1.set_title('f(t) = 1')
ax1.set_ylabel('wartosc')
ax1.set_xlabel('czas')
plt.show()

