# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1d-FRelyQzrXIg4FuCjH8SGiYCFLF--rP
"""

import matplotlib.pyplot as plt
import numpy as np
x = np.array([1, 2, 4, 6])
y = np.array([3, 8, 9, 10])
plt.plot(x, y)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the torus parameters
R = 2  # Major radius
r = 1  # Minor radius

# Create the parameter space
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)

u, v = np.meshgrid(u, v)

# Parametric equations for the torus
x = (R + r * np.cos(v)) * np.cos(u)
y = (R + r * np.cos(v)) * np.sin(u)
z = r * np.sin(v)

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(x, y, z, color='b', edgecolor='k')

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()

import matplotlib.pyplot as plt

# Data for Chevrolet car models
labels = ['Chevrolet Silverado', 'Chevrolet Equinox', 'Chevrolet Malibu', 'Chevrolet Traverse']
sales = [500000, 350000, 200000, 150000]  # Number of units sold
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']  # Colors for each section

# Calculating total sales to show percentage
total_sales = sum(sales)

# Exploding the largest slice to highlight it (Chevrolet Silverado)
explode = (0.1, 0, 0, 0)

# Create a pie chart
fig, ax = plt.subplots()
ax.pie(sales, explode=explode, labels=labels, colors=colors, autopct=lambda p: '{:.1f}%'.format(p), startangle=90)

# Equal aspect ratio ensures that pie chart is drawn as a circle
ax.axis('equal')

# Title
plt.title('Chevrolet Car Sales Distribution (Units Sold)')

# Show the plot
plt.show()