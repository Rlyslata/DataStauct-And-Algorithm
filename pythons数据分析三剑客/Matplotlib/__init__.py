import numpy as np
import matplotlib.pyplot as plt
labels = ['Mon','Tue','wed','Thu','Fri','Sat','Sun']

data = np.random.rand(7)*100
plt.pie(data,labels=labels,autopct='%1.lf%%')
plt.axis('equal')
plt.legend()
plt.show()
