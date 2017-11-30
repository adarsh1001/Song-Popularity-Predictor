import sys
import os
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.feature_selection import RFE
from sklearn import datasets
#dataset = datasets.load_iris()
inputfile = sys.argv[1]
temp=np.genfromtxt(inputfile,delimiter=",",dtype=float)
X=np.copy(temp[:,0:temp.shape[1]-1])
Y=np.copy(temp[:,temp.shape[1]-1])
svm = LinearSVC()
# create the RFE model for the svm classifier 
# and select attributes
rfe = RFE(svm, 82)
rfe = rfe.fit(X, Y)
# print summaries for the selection of attributes
print(rfe.support_)
print(rfe.ranking_)