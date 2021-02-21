import numpy as np
import matplotlib.pyplot as plt

# from sklearn.decomposition import PCA
# Visualizing 3-D numeric data with Scatter Plots
# length, breadth and depth

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

data = np.random.rand(600, 3) # tao mot array 2 chieu voi 600 diem voi 3 toa do

xs = data[:,0] # lay ra chieu thu 1, lay het tat ca cac gia tri
ys = data[:,1]
zs = data[:,2]

# print(data)
# print(xs)
# print(ys)
print(zs)
ax.scatter(xs, ys, zs, s=zs*300, alpha=0.6, edgecolors='w', c=data)

ax.set_xlabel('Residual Sugar')
ax.set_ylabel('Fixed Acidity')
ax.set_zlabel('Alcohol')
# ax.set_axis_off()
# ax.grid(False)
plt.show()

