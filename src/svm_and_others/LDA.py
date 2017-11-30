import sys
import os
import numpy as np
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
#import pandas as pd
from sklearn import datasets
#import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
inputfile = sys.argv[1]
temp=np.genfromtxt(inputfile,delimiter=",",dtype=float)
#print temp.shape[0]
#print temp.shape[1]
#print temp[0:,temp.shape[1]-1]
train_start=0
train_end=temp.shape[0]/2-1;
test_start=temp.shape[0]/2;
test_end=temp.shape[0]-1
X_train=np.copy(temp[train_start:train_end,0:temp.shape[1]-1])
Y_train=np.copy(temp[train_start:train_end,temp.shape[1]-1])

X_test=np.copy(temp[test_start:test_end,0:temp.shape[1]-1])
Y_test=np.copy(temp[test_start:test_end,temp.shape[1]-1])
'''
print X_train.shape
print Y_train.shape
print X_test.shape
print Y_test.shape
'''

clf = LinearDiscriminantAnalysis()
clf.fit(X_train, Y_train)
LinearDiscriminantAnalysis(n_components=None, priors=None, shrinkage='auto',solver='lsqr',store_covariance=False,tol=0.01)
#print clf.predict(temp[temp.shape[0]/2:temp.shape[0],0:temp.shape[1]-1])
Y_predict=clf.predict(X_test)
#print Y_predict.shape
count=0

#print Y_test.shape[0]

for i in range(0,Y_test.shape[0]):
	if Y_predict[i]==Y_test[i]:
		count=count+1
print "Accuracy=",(count*100.)/Y_test.shape[0]
#print "accuracy=",count/(temp.shape[0]/2)

#for i in range(train_start,train_end):
#	print Y_predict[i]
#print temp.shape
#print X.shape
#print Y.shape
#print Y_predict.shape
'''
Y_exp=np.copy(Y[test_start:test_end])
for i in range(test_start,test_end-1):
	print Y_exp[i]
'''