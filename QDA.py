import sys
import os
import numpy as np
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
inputfile = sys.argv[1]
temp=np.genfromtxt(inputfile,delimiter=",",dtype=float)
train_start=0
train_end=temp.shape[0]/2-1;
test_start=temp.shape[0]/2;
test_end=temp.shape[0]-1
X_train=np.copy(temp[train_start:train_end,0:temp.shape[1]-1])
Y_train=np.copy(temp[train_start:train_end,temp.shape[1]-1])

X_test=np.copy(temp[test_start:test_end,0:temp.shape[1]-1])
Y_test=np.copy(temp[test_start:test_end,temp.shape[1]-1])
clf = QuadraticDiscriminantAnalysis()
clf.fit(X_train,Y_train)
QuadraticDiscriminantAnalysis(priors=None, reg_param=0.0,store_covariance=False,store_covariances=None, tol=0.0001)
Y_predict_train=clf.predict(X_train)

Y_predict_test=clf.predict(X_test)
count=0

for i in range(0,Y_test.shape[0]):
	if Y_predict_test[i]==Y_test[i]:
		count=count+1
print "test Accuracy",(count*100.)/Y_test.shape[0]


for i in range(0,Y_train.shape[0]):
	if Y_predict_train[i]==Y_train[i]:
		count=count+1
print "train acc",(count*100.)/Y_test.shape[0]
