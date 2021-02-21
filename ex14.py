import matplotlib.pyplot as plt
import numpy as np

# using some dummy data for this example
xs = np.arange(0,10,1)
print(xs)
ys = np.random.normal(loc=3, scale=0.4, size=10)
colors = np.random.rand(10,3) # tao array 2 chieu voi 10 mau, va 3 mau co ban phoi voi nhau

plt.bar(xs,ys,color=colors)

# zip joins x and y coordinates in pairs
for x,y in zip(xs,ys):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xticks(np.arange(0,10,1))
plt.yticks(np.arange(0,5,0.5))

plt.show()