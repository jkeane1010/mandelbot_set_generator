import numpy as np
import matplotlib.pyplot as plt

# create a complex grid of points
x = np.linspace(-2, 1, 1000)
y = np.linspace(-1.5, 1.5, 1000)
X, Y = np.meshgrid(x, y)
Z = X + Y * 1j

# iterate the function f(z) = z^2 + c over each point in the grid
max_iterations = 500
c = Z
z = 0

for i in range(max_iterations):
  z = z**2 + c

# create a mask to identify points that are in the Mandelbrot set
mask = (abs(z) < 2)

# plot the points on the complex plane
fig, ax = plt.subplots()
ax.scatter(X[mask], Y[mask], c='black', s=1)
ax.set_title("Mandelbrot Set")
plt.show()