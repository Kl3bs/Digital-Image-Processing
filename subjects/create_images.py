import numpy as np
import matplotlib.pyplot as plt


"""
(1) Create the image of a paraboloid with one axis scaled (like an oval paraboloid).
(2) Create the image of a rotated sin using rotation of coordinates.
(3) Create the image of a gaussian.
(4) Create a function that generates the image of a Gaussian optionally rotated by an angle \theta and with mx, my, sx, sy as input arguments.

Attention: Use numpy.linspace() and numpy.meshgrid() to generate the images.
"""
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


def paraboloid(x_values, y_values):

    X,Y = np.meshgrid(x_values, y_values)
    Z = np.power(X,2) + np.power(Y,2)

    ax.plot_surface(X, Y, Z)
    plt.show()
    return


def rotated_sin(x_values, y_values, theta):

    X,Y = np.meshgrid(x_values, y_values)
    Z = np.sin(theta * X) * np.sin(theta * Y)

    ax.plot_surface(X, Y, Z)
    plt.show()
    return


def gaussian(x_values, y_values, mx, my, sx, sy):
    X,Y = np.meshgrid(x_values, y_values)
    Z = np.exp(-((X - mx)**2 / (2 * sx**2) + (Y - my)**2 / (2 * sy**2)))

    ax.plot_surface(X, Y, Z)
    plt.show() 
    return 
 

def rotated_gaussian(x_values, y_values, mx, my, sx, sy, theta):
    X,Y = np.meshgrid(x_values, y_values)
    Z = np.exp(-((X*np.cos(theta) - mx)**2 / (2 * sx**2) + (Y*np.sin(theta) - my)**2 / (2 * sy**2)))

    ax.plot_surface(X, Y, Z)
    plt.show()
    return 


def __main__():
    x_values = np.linspace(0, 1, 40)
    y_values = np.linspace(0, 1, 40)

    paraboloid(x_values, y_values)
    # rotated_sin(x_values, y_values, 30)
    # gaussian(x_values, y_values, 5, 5, 1, 30)
    #rotated_gaussian(x_values, y_values, 5, 5, 1, 1, 30)

__main__()