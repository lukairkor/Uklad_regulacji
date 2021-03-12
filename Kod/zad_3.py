from numpy import zeros, linspace, pi, cos, array
import matplotlib.pyplot as plt
import math
dt = 0.025 #interwalow na okres 0.01
# dt = 0.01
# dt = 0.000001
T = 1
N_t = int(round(T/dt)) #calkowita liczba interwalow 
t = linspace(0, N_t*dt, N_t+1) #od 0 co krok dt+dt do T [0.15707963 0.31415927 0.4712389....]
x = zeros(N_t+1) #szablon macierzy
y = zeros(N_t+1)
a = 1/0.1
b = 1/0.1

# Initial condition
x[0] = 0 
y[0] = 0


# Obliczenia wedlug wzoru
for n in range(N_t):
    y[n+1] = y[n] + dt*((a*x[n])-(b*y[n]))
    x[n+1] = x[n] + dt 

fig = plt.figure()
ax1 = fig.add_subplot(111)
l1 = plt.plot(t, y, 'b-')
plt.grid()
ax1.set_title('f(t) = 1')
ax1.set_ylabel('wartosc')
ax1.set_xlabel('czas')
plt.show()







# #scipy.integrate.odeint
# #wlasny przyklad
# from scipy.integrate import odeint
# import numpy as np
# import matplotlib.pyplot as plt

# def inercja(y,t,u,dt):
#     dydt = ((a*u)-(b*y*dt))
#     return dydt

# y0=[0.0]
# t=np.linspace(0,10,100)
# a = 1/0.1
# b = 1/0.1
# u = 2.0
# dt = 0.025

# wy=odeint(inercja,y0,t,args=(u,dt))

# plt.clf()
# plt.plot(t,wy[:,0],'r',label='wyjscie')
# # plt.plot(t,sol[:,1],'b',label='prędkosc')
# plt.legend(loc='best')
# plt.grid()