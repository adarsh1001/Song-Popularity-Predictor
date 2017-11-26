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


if __name__ == '__main__':
	#Read concatenated input arrays 

	##################################
	#Leave this right now
	#Assign the no. of columns in array input 
	#n_timesteps = 100
	# reshape input and output data to be suitable for LSTMs.
	# i.e. (no. of samples, no. of timesteps, no. os features per timestep)
	#X = X.reshape(1, n_timesteps, 1)
	#@###################################

	#Input in this format:

	'''
	array([[1, 1, 4, 2],
	       [0, 0, 1, 3],
	       [0, 3, 1, 2],
	       [0, 0, 1, 2]], dtype=int32)
	'''

	print "Features extraction done";

	y = np_utils.to_categorical(y)
	num_classes = y.shape[1]
	#Define the LSTM model

	####Input length is the length of the sequences.
	####20000 is the no. of input classes, modify accordingly.
	####128 is the embedding dimension.
	#http://www.developintelligence.com/blog/2017/06/practical-neural-networks-keras-classifying-yelp-reviews/
	model = Sequential()
	model.add(Embedding(20000, 128, input_length=300))
	model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
	model.add(Dense(num_classes, activation='softmax'))
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

	# Train LSTM
	model.fit(X, y, epochs=50, batch_size=32, verbose=1)


	# evaluate LSTM

	yhat = model.predict_classes(X, verbose=0)

	for i in range(n_timesteps):
		print('Expected:', y[0, i], 'Predicted', yhat[0, i])
