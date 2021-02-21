import matplotlib.pyplot as plt
import numpy as np

x = np.arange(50) # tao ra 50 so nguyen lien tiep tu 0 den 49
y = np.random.randint(1, 100, 50) # tao ra 50 so nguyen nhien tu 1 den 99


plt.scatter(x, y, color='r')

x = np.arange(10, 40, 1)
y = np.random.randint(1, 100, 30)
plt.scatter(x, y, color ='g', s=y)

plt.show()