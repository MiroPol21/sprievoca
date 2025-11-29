import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Function to differentiate
def f(x):
    return x**3 + 2*x**2 + 1

def df_dx(x):
    return 3 * x**2 + 4*x

# Domain
x = np.linspace(-5, 5, 500)

# Fixed x0
x0 = 1

# Secant line
def secant_line(x, x0, x1):
    return f(x0) + (f(x1) - f(x0)) / (x1 - x0) * (x - x0)

# Carathéodory φ(x)
def phi(x, x0):
    return (f(x) - f(x0)) / (x - x0)

# Remove singularity at x0
ox = x[x != x0]

# --- Figure setup ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6,10))

# Left plot: f(x)
ax1.plot(x, f(x), color="black", label='$f(x)$')
ax1.plot(x0, f(x0), 'bo', label='$x_0$')
point_plot1, = ax1.plot([], [], 'ro', label='$f(x_i)$')
secant_plot, = ax1.plot([], [], 'r--')
ax1.set_title("A function $f(x)$")
ax1.legend(loc='upper left', fontsize='small', 
           facecolor='snow', edgecolor='black')

# Right plot: φ(x)
ax2.plot(ox, phi(ox, x0), color="black", label='$\\varphi(x)$')
ax2.scatter(x0, df_dx(x0), color='white', marker='o', label='$x_0$', edgecolors='black')
ax2.plot(x, df_dx(x), 'g--', label="$f'(x)$")
point_plot2, = ax2.plot([], [], 'ro', label='$\\varphi(x_i)$')
ax2.set_title("Carathéodory function $\\varphi(x)$")
ax2.legend(loc='upper left', fontsize='small', 
           facecolor='snow', edgecolor='black')

# Animation frames: sweep secant point across domain
frames = np.linspace(-5, 5, 300)

def init():
    point_plot1.set_data([], [])
    secant_plot.set_data([], [])
    point_plot2.set_data([], [])
    return point_plot1, secant_plot, point_plot2

def animate(x_secant):
    # Left plot
    point_plot1.set_data([x_secant], [f(x_secant)])
    secant_plot.set_data(x, secant_line(x, x0, x_secant))
    
    # Right plot
    point_plot2.set_data([x_secant], [phi(x_secant, x0)])
    
    return point_plot1, secant_plot, point_plot2

anim = FuncAnimation(fig, animate, frames=frames, init_func=init, interval=40, blit=True)

anim.save("caratheodory_differentiation.gif", writer=PillowWriter(fps=30))

plt.show()
