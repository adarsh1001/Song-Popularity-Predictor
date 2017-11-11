from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
import numpy as np 

np.random.seed(7);

dataset = np.genfromtxt('MSD_DATASET.txt', delimiter=',')[:,:-1]
x = dataset[:2800,0:82];
y = dataset[:2800, 82];

y = np_utils.to_categorical(y)
num_classes = y.shape[1]

model = Sequential();
model.add(Dense(50, init='uniform', input_dim=82, activation='relu'));
model.add(Dense(25, activation='relu', init='uniform'));
model.add(Dense(10, activation='sigmoid', init='uniform'));
model.add(Dense(5, activation='relu', init='uniform'));
model.add(Dense(num_classes, activation='softmax', init='uniform'));

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy']);
model.fit(x, y, epochs=130, batch_size=32);

x_test = dataset[2801:3054, 0:82];
y_test = dataset[2801:3054, 82];
y_test = np_utils.to_categorical(y_test)

scores = model.evaluate(x_test, y_test);
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100));
