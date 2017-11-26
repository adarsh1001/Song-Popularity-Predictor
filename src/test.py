import numpy as np
import matplotlib.pyplot as plt

d = np.genfromtxt('../t_features.csv', delimiter=',')
x = []
for i in range(0, 30):
	x.append(i);

for i in range(0, len(d)):
	plt.plot(x, d[i]);

plt.show();