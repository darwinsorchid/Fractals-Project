'''                                                The Mandelbrot Fractal
The Mandelbrot set is a set of complex numbers that produces a distinctive, self-similar fractal pattern when visualized. 
It was named after the mathematician Benoit Mandelbrot, who popularized fractal geometry in the 1980s.
Mathematically, it is defined as a set of complex numbers c, for which the function fc(z) = z^2 + c does not diverge to infinity
when iterated, starting at z = 0.

The Mandelbrot set has become an icon of chaos theory and complex dynamics. 
It provides insights into the behavior of dynamical systems, 
particularly how small changes in initial conditions can lead to vastly different outcomes 
(a property known as "sensitivity to initial conditions").

When plotted, the Mandelbrot set is connected, 
meaning there is a continuous path within the set between any two points in the set. 
The boundary, however, is highly convoluted and infinitely complex.
'''

# ------------------------------------------------ Import Libraries -----------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


# ------------------------------------------------ Streamlit Markdown ---------------------------------------------
st.markdown("# The Mandelbrot Fractal")
with st.expander("Info"):
    st.write('''The Mandelbrot set is a set of complex numbers that produces a distinctive, self-similar fractal pattern when visualized. 
It was named after the mathematician Benoit Mandelbrot, who popularized fractal geometry in the 1980s.
Mathematically, it is defined as a set of complex numbers c, for which the function fc(z) = z^2 + c does not diverge to infinity
when iterated, starting at z = 0.

The Mandelbrot set has become an icon of chaos theory and complex dynamics. 
It provides insights into the behavior of dynamical systems, 
particularly how small changes in initial conditions can lead to vastly different outcomes 
(a property known as "sensitivity to initial conditions").

When plotted, the Mandelbrot set is connected, 
meaning there is a continuous path within the set between any two points in the set. 
The boundary, however, is highly convoluted and infinitely complex.''')
    

# ------------------------------------------------ Streamlit Sliders ----------------------------------------------
# Slider to control the maximum number of iterations
max_iter = st.sidebar.slider('Max Iterations', 1, 500, 50)

# Slider to control grid resolution
resolution = st.sidebar.slider('Grid Resolution', 100, 1000, 500)

# Slider to control zoom factor -- Control how much you zoom in
zoom_factor = st.sidebar.slider('Zoom Factor (higher = more zoom)', 1.0, 10.0, 1.0)

# Sliders to control the center of the zoom -- Control where you zoom in on the graph
center_real = st.sidebar.slider('Real Axis Center', -2.5, 1.0, -0.5)
center_imag = st.sidebar.slider('Imaginary Axis Center', -1.5, 1.5, 0.0)


# ------------------------------------------ Set up complex plane region ------------------------------------------

# Define the range for the axes based on the zoom factor
real_range = 3.5 / zoom_factor  # Original width is 3.5 (-2.5 to 1)
imag_range = 3.0 / zoom_factor  # Original height is 3.0 (-1.5 to 1.5)

# Define real and imaginary points based on zoom level and center
real_points = np.linspace(center_real - real_range/2, center_real + real_range/2, num=resolution)
imag_points = np.linspace(center_imag - imag_range/2, center_imag + imag_range/2, num=resolution)

# Define 2D Cartesian grid 
real_grid, imag_grid = np.meshgrid(real_points, imag_points)

# Combine into complex array -> Produces a 20x20 grid of 400 complex numbers
complex_grid = real_grid + imag_grid * 1j


# ---------------------------------------- Mandelbrot Function Iteration -------------------------------------------  

# Set default zoom parameters
zoom_factor = 1.0
max_iter = 100
resolution = 1000

# Define |z| limit 
z_limit = 2    

# Create array to store the number of iterations
iterations = np.zeros(complex_grid.shape, dtype=int)


# Iterate through complex grid points
for row in range(complex_grid.shape[0]):
    for col in range(complex_grid.shape[1]):

        c = complex_grid[row, col]

        # Placeholder values for z and iteration count
        z = 0 
        iter_num = 0
        
        while iter_num <= max_iter:
            z = z**2 + c    # Iterates through function 

            if abs(z) > z_limit:
                iterations[row, col] = iter_num
                break

            else:
                iterations[row, col] = max_iter
            
            iter_num += 1 # Tracks how many iterations it takes for abs(z) to exceed the limit


# ----------------------------------------------- Plot Mandelbrot Set ------------------------------------------------
fig = plt.figure(figsize=(20, 20))
plt.imshow(iterations, cmap='inferno', extent=[center_real - real_range/2, center_real + real_range/2,
                                               center_imag - imag_range/2, center_imag + imag_range/2])
plt.colorbar(label='Iterations to Divergence')
plt.title('Mandelbrot Set')
plt.xlabel('Real')
plt.ylabel('Imaginary')

st.pyplot(fig)


    

