import numpy as np
import matplotlib.pyplot as plt

# Define the function and its derivative
def f(x, y):
    return 2 * x**3 + 3 * y**3

def df_dx(x, y):
    return 6 * x**2

def df_dy(x, y):
    return 9 * y**2

# Create a grid of x and y values
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Calculate the function and derivative values over the grid
Z = f(X, Y)
dZ_dx = df_dx(X, Y)
dZ_dy = df_dy(X, Y)

# Create 3D surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Show the plot
plt.show()

# Create 3D surface plot for the derivative df/dx
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, dZ_dx, cmap='viridis')

# Show the plot
plt.show()



