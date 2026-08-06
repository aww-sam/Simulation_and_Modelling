import numpy as np
import matplotlib.pyplot as plt

R=float(input("Enter the value of resistance: "))
L=float(input("Enter the value of inductance: "))
C=float(input("Enter the value of capacitance: "))
v0=float(input("Enter the value of initial capacitor voltage: "))
alpha=R/(2*L)
w0=1/((L*C)**0.5)

t=np.linspace(0,10,100000)
if alpha>w0:
    print("overdamped")
    s1=-alpha+np.sqrt(alpha**2-w0**2)
    s2=-alpha-np.sqrt(alpha**2-w0**2)
    i=((v0/(L*(s1-s2)))*np.exp(s1*t))+((-v0/(L*(s1-s2)))*np.exp(s2*t))
    v=((v0/(s1-s2)))*((s1*np.exp(s2*t))-(s2*np.exp(s1*t))) 
    plt.title("Overdamped RLC circuit")
elif alpha==w0:
    print("criticall")
    i=(v0/L)*np.exp(-alpha*t)*t
    v=v0*(1+(alpha*t))*np.exp(-alpha*t)
    plt.title("Critically damped RLC circuit")

else:
    print("underdamped")
    Wd=(w0**2-alpha**2)**0.5
    sin_term=np.sin(Wd*t)
    cos_term=np.cos(Wd*t)
    i=(v0/(L*Wd))*(np.exp(-alpha*t))*sin_term
    v=v0*np.exp(-alpha*t)*(cos_term+((alpha/Wd)*sin_term))
    plt.title("Underdamped RLC circuit")

plt.plot(t,i,c='r',label='current')
plt.plot(t,v,c='b',label='voltage')
plt.legend()
plt.grid()
plt.show()