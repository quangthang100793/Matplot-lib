import matplotlib.pyplot as plt
import numpy as np

labels = ['Q1', 'Q2', 'Q3', 'Q4']
Hanoi = np.array([20, 34, 30, 35]) # chuyen thanh numpy array
SaiGon = np.array([25, 32, 34, 20])
DaNang = np.array([5, 10, 15, 20])
tb = (Hanoi+SaiGon+DaNang)/3

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars


fig, ax = plt.subplots()
rects1 = ax.bar(x - width, Hanoi, width, label='Hanoi', color='r')
rects2 = ax.bar(x, SaiGon, width, label='SaiGon', color='g')
rects3 = ax.bar(x + width, DaNang, width, label='DaNang', color=['b','y','k','brown']) # mau ngau nhien
#color=np.random.rand(4,3)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Turnover')
ax.set_title('Turnover by group and location')
ax.set_xticks(x)
ax.set_xticklabels(labels) #cach thay doi ten nhãn cho trục x
ax.legend() # in chu thich, lay lable de in


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.plot(x,tb,'ko-')

fig.tight_layout() # dieu chinh kich thuoc bieu do de cho thay tron ven bieu do tren o kich thuoc

plt.show()