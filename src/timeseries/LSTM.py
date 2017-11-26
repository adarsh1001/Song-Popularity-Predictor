#Library calls
from random import random
from numpy import array
from numpy import cumsum
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import TimeDistributed
from keras.layers import Bidirectional
from keras.utils import np_utils
from keras.layers import Embedding
from keras.optimizers import SGD
from keras.layers import Conv1D
from keras.layers import MaxPooling1D
import sys
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
	X = np.genfromtxt(sys.argv[1], delimiter=',')
	X = X.astype(int)
	print X.shape
	#X = np.reshape(X, (889,30,1))
	print "Features extraction done";

	y_init  = np.genfromtxt(sys.argv[2])

	y = np_utils.to_categorical(y_init)
	num_classes = y.shape[1]
	#Define the LSTM model

	####Input length is the length of the sequences.
	####20000 is the no. of input classes, modify accordingly.
	####128 is the embedding dimension.
	#http://www.developintelligence.com/blog/2017/06/practical-neural-networks-keras-classifying-yelp-reviews/
	model = Sequential()
	model.add(Embedding(16, 128, input_length=30))
	

	
	#model.add(Embedding(300, 128, input_length=30))
	model.add(LSTM(128))
	model.add(Dropout(0.2))
	#model.add(LSTM(256))
	#model.add(Dropout(0.2))
	model.add(Dense(num_classes, activation='softmax'))
	opt = SGD(lr=0.0001)
	model.compile(loss='categorical_crossentropy', optimizer='nadam', metrics=['accuracy'])

	# Train LSTM
	model.fit(X, y,validation_split=0.1, epochs=100, batch_size=32, verbose=1)


	# evaluate LSTM
	X_test = np.genfromtxt(sys.argv[3], delimiter=',')
	X_test = X_test.astype(int)
	y_test = np.genfromtxt(sys.argv[4]);
	y_test = np_utils.to_categorical(y_test);

	yhat = model.predict(X_test)
	print yhat[0]
	acc = 0.
	count = 0
	for i in range(len(yhat)):
		print('Expected:', np.argmax(y_test[i]), 'Predicted', np.argmax(yhat[i]))

		if (int(np.argmax(y_test[i])) == int(np.argmax(yhat[i]))):
			count+=1
	acc = float(count) / len(yhat)

	print ("Accuracy: ", acc*100, " %")
