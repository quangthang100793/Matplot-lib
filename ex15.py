import matplotlib.pyplot as plt
import numpy as np

plt.clf()

# using some dummy data for this example
xs = np.random.normal(loc=4, scale=2.0, size=10)
ys = np.random.normal(loc=2.0, scale=0.8, size=10) # list voi 10 gia tri ngau nhien, trung binh 2.0 và do lech 0.8

# plot the chart
plt.scatter(xs,ys,c=np.random.rand(len(xs),3), s=100 + np.random.rand(len(xs))*100)

# zip joins x and y coordinates in pairs
for x,y in zip(xs,ys):

    #label = "{:.2f}".format(y) # cach 1
    label = f"{y:.2f}" # cach 2 

    # this method is called for each point
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xticks(np.arange(0,10,1))
plt.yticks(np.arange(0,5,0.5))

plt.show()

