#Library calls
from random import random
from numpy import array
from numpy import cumsum
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import TimeDistributed
from keras.layers import Bidirectional
from keras.utils import np_utils


#Read concatenated input arrays 

##################################

#Assign the no. of columns in array input 
n_timesteps = 100

# reshape input and output data to be suitable for LSTMs.
# i.e. (no. of samples, no. of timesteps, no. os features per timestep)
X = X.reshape(1, n_timesteps, 1)

y = np_utils.to_categorical(y)
num_classes = y.shape[1]

#Define the LSTM model

model = Sequential()
model.add(Bidirectional(LSTM(100)))
model.add(Dense(num_classes, activation='softmax'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train LSTM
model.fit(X, y, epochs=50, batch_size=32, verbose=1)


# evaluate LSTM

yhat = model.predict_classes(X, verbose=0)
for i in range(n_timesteps):
	print('Expected:', y[0, i], 'Predicted', yhat[0, i])

