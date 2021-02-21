import matplotlib.pyplot as plt
import numpy as np

langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12] # so luong phan tu cua x va y phai bang nhau

# x co the la chu, nhung y phai la so
print(np.random.rand(len(langs),3))
plt.bar(langs,students,color =np.random.rand(len(langs),3),width=.5)
#
plt.show()

