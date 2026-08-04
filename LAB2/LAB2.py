import math
import matplotlib.pyplot as plt
import numpy as np

m=float(input("Enter value of mass: "))
k=float(input("Enter value of spring_constant: "))
c=float(input("enter the value of damping constant: "))
y0=float(input("Enter the value of initial displacement: "))
v0=float(input("Enter the value of initial velocity: "))
t=np.linspace(0,10,500)
crictical_cond=(4*m*k)**0.5
y_val=[]
if c<crictical_cond:
    print("Underdamped_motion")
    w1=((4*m*k-c**2)**0.5)/(2*m)
    c1=y0
    c2=(v0+(c/2*m)*y0)/w1
    A=(c1**2+c2**2)**0.5
    phi=math.atan2(c1,c2)
    y_values=(A*np.exp((-c*t)/(2*m))*np.sin(w1*t+phi))
    plt.plot(t,y_values)
    plt.grid(True)
    plt.title("Underdamped Motion of spring mass system")
    plt.xlabel("Time(t)")
    plt.ylabel("Displacement(y)")
    plt.show()
elif c>crictical_cond:
    print("overdamped_motion")
    r1=(-c-(c**2-4*m*k)**0.5)/(2*m)
    r2=(-c+(c**2-4*m*k)**0.5)/(2*m)
    c2=(v0-r1*y0)/(r2-r1)
    c1=y0-c2
    y_values=c1*np.exp(r1*t)+c2*np.exp(r2*t)
    plt.plot(t,y_values)
    plt.grid(True)
    plt.title("Overrdamped Motion of spring mass system")
    plt.xlabel("Time(t)")
    plt.ylabel("Displacement(y)")
    plt.show()

else:
    c1 = y0
    c2 = v0 + (c / (2 * m)) * y0
    y_values = np.exp(-c * t / (2 * m)) * (c1 + c2 * t)
    plt.plot(t, y_values)
    plt.plot(t,y_values)
    plt.grid(True)
    plt.title("Critically damped Motion of spring mass system")
    plt.xlabel("Time(t)")
    plt.ylabel("Displacement(y)")
    plt.show()
