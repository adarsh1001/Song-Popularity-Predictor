from keras.models import Sequential
from keras.layers import Dense
import numpy as np 

np.random.seed(7);

dataset = np.loadtxt('data.csv', delimiter=',');
x = dataset[:,0:8];
y = dataset[:, 8];

model = Sequential();
model.add(Dense(12, input_dim=8, activation='relu'));
model.add(Dense(8, activation='relu'));
model.add(Dense(3, activation='softmax'));

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy']);
model.fit(x, y, epochs=150, batch_size=10);

scores = model.evaluate(x, y);
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100));