from mpl_toolkits import plot3dm
import numpy as np
import matplotlib as plt
fig = plt.figure()
# syntax for 3-D projection
ax = plt.axes(projection ='3d* ')
#defining all 3 axes
z = np. linspace(0, 1, 100)
x = z * np.sin(25 * z)
V = z* np.COS(25 * z)
 # plotting
ax.plot3D(x, y, z, 'purple' )
ax.set_title('3D line plot')
plt.show()
