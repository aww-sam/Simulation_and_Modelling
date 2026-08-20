import numpy as np
import matplotlib.pyplot as plt

R=500
C=0.001
V0=15
t0=0
T=15
dt=0.01
t=np.arange(t0,T+dt,dt)
V=np.zeros(len(t))
V[0]=V0

for i in range(len(t)-1):

    dv=-V[i]/(R*C)
    V[i+1]=V[i]+dv*dt

plt.figure(figsize=(8,5))
plt.plot(t,V,c='blue',label="Capacitor Discharging")
plt.xlabel("Time (t)")
plt.ylabel("Voltage (v)")
plt.title("Capacitor Discharging Simulation")
plt.grid(True)
plt.legend()
plt.show()