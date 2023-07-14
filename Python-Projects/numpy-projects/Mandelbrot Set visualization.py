# Mandelbrot Set visualization: Generate and plot the famous Mandelbrot Set using NumPy.


import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    for i in range(max_iter):
        z = z**2 + c
        if abs(z) > 2:
            return i
    return max_iter

def generate_mandelbrot(width, height, real_range, imaginary_range, max_iter):
    real_vals = np.linspace(real_range[0], real_range[1], width)
    imaginary_vals = np.linspace(imaginary_range[0], imaginary_range[1], height)
    mandelbrot_set = np.zeros((width, height), dtype=int)

    for x in range(width):
        for y in range(height):
            c = real_vals[x] + imaginary_vals[y]*1j
            mandelbrot_set[x, y] = mandelbrot(c, max_iter)

    return mandelbrot_set

def plot_mandelbrot(mandelbrot_set):
    plt.imshow(mandelbrot_set.T, cmap='hot', extent=[-2, 1, -1.5, 1.5])
    plt.xlabel('Re(c)')
    plt.ylabel('Im(c)')
    plt.title('Mandelbrot Set')
    plt.show()

# Test case
width = 800
height = 600
real_range = (-2.0, 1.0)
imaginary_range = (-1.5, 1.5)
max_iter = 100

mandelbrot_set = generate_mandelbrot(width, height, real_range, imaginary_range, max_iter)
plot_mandelbrot(mandelbrot_set)
