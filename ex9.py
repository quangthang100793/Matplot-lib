import matplotlib.pyplot as plt

langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12] # so luong phan tu cua x va y phai bang nhau

# x co the la chu, nhung y phai la so 
plt.bar(langs,students)
plt.show()