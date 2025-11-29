import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Define the function to differentiate
def f(x):
    return x**3  

# Setup domain
x = np.linspace(-5, 5, 500)

# x0 value
x0 = 0.5

# x value for the Carathéodory derivative for different secants
x_secant = 3.0

# Secant line function
def secant_line(x, x0, x1):
    return f(x0) + (f(x1) - f(x0)) / (x1 - x0) * (x - x0)

# Generate x values for the Carathéodory derivative visualization
ox = np.delete(x, [0])
def phi(x, x0):
    return (f(x) - f(x0)) / (x - x0)

# Create interactive figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,5))
plt.subplots_adjust(bottom=0.25)

# --- Left plot: the function ---
ax1.plot(x, f(x), label='f(x)')
ax1.plot(x0, f(x0), 'ro', label='x0')
point_plot1, = ax1.plot(x_secant, f(x_secant), 'ro', label='x')
secant_plot, =ax1.plot(x, secant_line(x, x0, x_secant), 'r--', label='Secant Line')
ax1.set_title("Function")
ax1.legend()

# --- Right plot: Caratheodory function ---
ax2.plot(ox, phi(ox, x0), label='φ(x)')
point_plot2, = ax2.plot(x_secant, phi(x_secant, x0), 'ro', label='x')
ax2.set_title("Carathéodory function φ(x)")
ax2.legend()

# --- Slider for x0 ---
ax_slider = plt.axes([0.25, 0.1, 0.55, 0.03])
slider = Slider(ax_slider, 'x', -5.0, 5.0, valinit=x_secant)

# --- Update logic ---
def update(val):
    x_secant_new = slider.val
    # Update point on the left plot
    point_plot1.set_data([x_secant_new], [f(x_secant_new)])
    # Update secant line
    secant_plot.set_ydata(secant_line(x, x0, x_secant_new))
    # Update diff quotient plot
    point_plot2.set_data([x_secant_new], [phi(x_secant_new, x0)])
    fig.canvas.draw_idle()

slider.on_changed(update)

plt.show()
