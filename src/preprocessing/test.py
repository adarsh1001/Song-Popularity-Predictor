import numpy as np
import matplotlib.pyplot as plt

d = np.genfromtxt('../dataset/MSD_DATASET_LSTM.txt', delimiter=',')
x = []
for i in range(0, 51):
	x.append(i);

for i in range(0, len(d)):
	d[i][-1] = 0;
	plt.plot(x, d[i]);

plt.show();