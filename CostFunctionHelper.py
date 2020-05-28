from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# x = np.outer(np.linspace(-2, 2, 30), np.ones(30))
x = y = np.linspace(-2,2,1000)

# y = x.copy().T # transpose
x, y = np.meshgrid(x, y)

a = 1
b = 100
#z = np.cos(x ** 2 + y ** 2)
z = (a-x)**2 + b*(y-x**2)**2


fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(x, y, z,cmap='viridis', edgecolor='none')
ax.set_title('Surface plot')
# plt.contourf(x,y,z)
plt.show()
