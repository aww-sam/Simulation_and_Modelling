import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

## can change masses and lengths
m1=1.0
m2=1.0
L1=1.0
L2=1.0
g=9.81

def solve_equations(t,y):
    theta1,theta2,omega1,omega2=y

    delta=theta1-theta2

    denominator1=L1*(m1+m2*(np.sin(delta)**2))
    denominator2=L2*(m1+m2*(np.sin(delta)**2))

    alpha1=(-m2 * L1 * omega1**2 * np.sin(delta) * np.cos(delta)
            -m2 * L2 * omega2**2 * np.sin(delta)
            +(m1 + m2) * g * np.sin(theta2) * np.cos(delta)
            -(m1 + m2) * g * np.sin(theta1)
            )/denominator1
    alpha2=(
        (m1 + m2)*
        (L1 * omega1**2 * np.sin(delta) - 
        g * np.sin(theta2) + 
        g * np.sin(theta1) * np.cos(delta)
        ) +
        m2 * L2 * omega2**2 * np.sin(delta) * np.cos(delta) 
        )/denominator2

    return [omega1,omega2,alpha1,alpha2]

theta1 = np.radians(120) ## use different values
theta2 = np.radians(80)  ## use diff values

omega1 = 0
omega2 = 0

initial_cond=[theta1,theta2,omega1,omega2]
t=np.linspace(0,20,4000)

print(solve_equations(0,initial_cond))
solution=solve_ivp(
    solve_equations,
    [0,20],
    initial_cond,
    t_eval=t
)


### below is chatgpt code for animation

from matplotlib.animation import FuncAnimation

# Get angles
theta1 = solution.y[0]
theta2 = solution.y[1]

# Convert angles to coordinates
x1 = L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)

x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2 * np.cos(theta2)


# Create figure
fig, ax = plt.subplots()

ax.set_xlim(-(L1 + L2), L1 + L2)
ax.set_ylim(-(L1 + L2), L1 + L2)

ax.set_aspect("equal")
ax.grid()


# Pendulum line
line, = ax.plot([], [], "o-", lw=2)

# Trace of second mass
trace, = ax.plot([], [], "-", alpha=0.5)

trace_x = []
trace_y = []


def update(frame):

    # Current positions
    x = [0, x1[frame], x2[frame]]
    y = [0, y1[frame], y2[frame]]

    line.set_data(x, y)

    # Add second mass position to trace
    trace_x.append(x2[frame])
    trace_y.append(y2[frame])

    trace.set_data(trace_x, trace_y)

    return line, trace


animation = FuncAnimation(
    fig,
    update,
    frames=range(0, len(t), 3),
    interval=20,
    blit=True
)

plt.show()
