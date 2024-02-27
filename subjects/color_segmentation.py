# %%
import numpy as np
import matplotlib.pyplot as plt
import cv2
from mpl_toolkits.mplot3d import Axes3D


# %%
IMG_PATH = '../images/baboon.png'
img = cv2.imread(IMG_PATH, cv2.IMREAD_COLOR)
#change 
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)



# # %%
# plt.imshow(rgb_img)

# # %% [markdown]
# # <h3>3D points cloud<h3>

# # %%
# #Splitting the RGB channels into variables

# r,g,b = cv2.split(img)

# #plotting with scatter
# plt.figure(figsize=(10,10))
# plt.scatter(r.ravel(),g.ravel(),c=b.ravel())
# plt.show()

# # %%
# #Plotting 3D scatter plot
# ax = plt.subplot(111, projection='3d')
# ax.scatter(r, g, b, c=b, cmap=plt.cm.jet)
# plt.show()

# # %%
# #I need to plot each pixel as a 3d cube where each axis is the color channel.
 


# # %%
# # Convertendo a imagem para um array numpy
# data = np.array(rgb_img)

# # Obtendo as dimensões da imagem
# height, width, _ = data.shape

# # Preparando os dados para plotagem
# r, g, b = data[:,:,0].flatten(), data[:,:,1].flatten(), data[:,:,2].flatten()

# # Criando a figura e o subplot 3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Plotando os pontos
# ax.scatter(r, g, b, c='g', marker='o')

# # Definindo os rótulos dos eixos
# ax.set_xlabel('Red')
# ax.set_ylabel('Green')
# ax.set_zlabel('Blue')

# # Exibindo o gráfico
# plt.show()


# # %%
# # Convertendo a imagem para um array numpy
# data = np.array(rgb_img)

# # Obtendo as dimensões da imagem
# height, width, _ = data.shape

# # Preparando os dados para plotagem
# r, g, b = data[:,:,0].flatten(), data[:,:,1].flatten(), data[:,:,2].flatten()

# # Criando a figura e o subplot 3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Plotando os pontos
# ax.scatter(r, g, b, c=data.reshape(-1, 3)/255.0, marker='o')

# # Definindo os rótulos dos eixos
# ax.set_xlabel('Red')
# ax.set_ylabel('Green')
# ax.set_zlabel('Blue')

# # Exibindo o gráfico
# plt.show()

# %%
from mpl_toolkits.mplot3d import axes3d
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Grab some example data and plot a basic wireframe.
X, Y, Z = axes3d.get_test_data(0.05)
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

# Set the axis labels
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Rotate the axes and update
for angle in range(0, 360*4 + 1):
    # Normalize the angle to the range [-180, 180] for display
    angle_norm = (angle + 180) % 360 - 180

    # Cycle through a full rotation of elevation, then azimuth, roll, and all
    elev = azim = roll = 0
    if angle <= 360:
        elev = angle_norm
    elif angle <= 360*2:
        azim = angle_norm
    elif angle <= 360*3:
        roll = angle_norm
    else:
        elev = azim = roll = angle_norm

    # Update the axis view and title
    ax.view_init(elev, azim, roll)
    plt.title('Elevation: %d°, Azimuth: %d°, Roll: %d°' % (elev, azim, roll))

    plt.draw()
    plt.pause(.001)


