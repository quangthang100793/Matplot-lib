import numpy as np
import matplotlib.pyplot as plt

data = {'a': np.arange(50), # dung lay array tu 0 den 49, buoc nhay la 1
        'c': np.random.randint(0, 50, 50), # tao 50 so nguyen ngau nhien, tu 0 den 49
        'd': np.random.randn(50)} # tao ra 50 so thuc ngau nhien

print (data['a'])
print (data['c'])
print (data['d'])

data['b'] = data['a'] + 10 * np.random.randn(50) # lay ra phan tu array a roi cong voi so ngau nhien
# tu 0 den 49, nhan voi 10


data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()