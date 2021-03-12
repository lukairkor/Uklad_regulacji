from numpy import zeros, linspace, pi, cos, array
import matplotlib.pyplot as plt
import math
dt = 0.000001 #interwalow na okres 0.01
# dt = 0.01
# dt = 0.000001
T = 1
N_t = int(round(T/dt)) #calkowita liczba interwalow 
t = linspace(0, N_t*dt, N_t+1) #od 0 co krok dt+dt do T [0.15707963 0.31415927 0.4712389....]
x = zeros(N_t+1) #szablon macierzy
y = zeros(N_t+1)
v = zeros(N_t+1)
u = zeros(N_t+1)
a = 0.2/0.01
b = 1/0.01
c = 1/0.01

# Initial condition
x[0] = 0 
y[0] = 0
v[0] = 0
# =============================================================================
# y"(x)=a*y'(x)-b*y(x)+c*u
# y'(x)=v(x)
# v'(x)=a*v(x)-b*y(x)+c*u = f(x,y,v)
# =============================================================================

# Obliczenia wedlug wzoru
for n in range(N_t):
    u[n+1] = u[n] + dt*v[n]
    v[n+1] = v[n] + dt*(-a*v[n]-b*u[n]+c*1)
    
# =============================================================================
# u = y
# v = y'=u'
# u' = v
# v' = a*v-b*u+c*1
# 
# u[n+1] = u[n] + dt*v[n]
# v[n+1] = v[n] - dt*a*v[n]-b*u[n]+c*1
# =============================================================================

# =============================================================================
# # Obliczenia wedlug wzoru
# for n in range(N_t):
# =============================================================================
#     y[n+1] = y[n] + dt*2*x[n]
#     x[n+1] = x[n] + dt 
# =============================================================================
# =============================================================================

fig = plt.figure()
ax1 = fig.add_subplot(111)
l1 = plt.plot(t,u, 'b-')
plt.grid()
ax1.set_title('f(t) = 1')
ax1.set_ylabel('wartosc')
ax1.set_xlabel('czas')
plt.show()