import matplotlib.pyplot as plt
import numpy as np

# plt.clf()

# using some dummy data for this example
xs = np.arange(0,10,1)
ys = np.random.normal(loc=3, scale=2.0, size=10) # phan phoi theo xac suat normal

# 'bo-' means blue color, round points, solid lines
plt.plot(xs,ys,'bo-')
print(xs)
print(ys)
print(tuple(zip(xs,ys)))

# zip joins x and y coordinates in pairs, ghep doi thanh tung cap
for x,y in zip(xs,ys):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10),# distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xticks(np.arange(0,10,1)) #tao ra nhung toa do tren truc x ( tu 0 den 9)
plt.yticks(np.arange(0,7,0.5)) # tao nhung toa do tren truc y (tu 0 den 6.5)

plt.show()