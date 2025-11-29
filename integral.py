import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return 0.3*np.sin(2*x) + 0.1*(x-3)**2 + 1

# Domain
x = np.linspace(-1, 6, 400)
y = f(x)

# Integration limits
a, b = 1, 5

# Create plot
fig, ax = plt.subplots(figsize=(5, 3))

# Plot the function
ax.plot(x, y, linewidth=2, color='black', label=r'$f(x)$')

# Shade the region between a and b
xs = np.linspace(a, b, 300)
ax.fill_between(xs, f(xs), color='gray', alpha=0.35, hatch='///')

# Draw vertical lines at a and b
ax.vlines([a, b], ymin=0, ymax=f(np.array([a, b])),
          colors='black', linestyles='solid')

# Axes labels & aesthetics
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.axhline(0, color='black', linewidth=1)
ax.set_xlim(-1, 6)
ax.set_ylim(0, max(y)+0.5)
ax.legend(loc='upper right', fontsize='small', 
          facecolor='snow', edgecolor='black')
          
# Remove unnecessary spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Put axes through the origin
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

# Clean x and y-axis ticks
ax.set_yticks([-1, 0, 1, 2])
ax.set_xticks([a, b])
ax.set_xticklabels(['a', 'b'])


plt.tight_layout()
plt.show()