from matplotlib import pyplot as plt

langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12]
plt.pie(students, labels = langs,autopct='%1.2f%%')# dinh dang so trong bieu do, %n% la hien so phan tram len
plt.show()