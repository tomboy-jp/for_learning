import numpy as np
import matplotlib.pyplot as plt
import datetime

data = np.random.rand(5)
num = np.arange(len(data))
# num = [x for x in range(len(data))]

now = datetime.datetime.now()
date_label = []

for i in range(len(data)):
    date_label.append((now - datetime.timedelta(days=i)).strftime("%Y/%m/%d"))

date_label.reverse()

plt.plot(num, data)
plt.xticks(num, date_label)

plt.pause(5)
