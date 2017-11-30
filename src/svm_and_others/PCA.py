import sys
import os
import numpy as np
from sklearn.decomposition import PCA
#import pandas as pd
from sklearn import datasets
#import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
#matplotlib inline

#Load data set
#X = datasets.load_iris()
#print X
#inputfile = sys.argv[1]
#temp=np.genfromtxt(inputfile,delimiter=",",dtype=float)
#x1=np.copy(temp[0:150,0])
#print x1
'''
x2=np.copy(temp[0:150,0:2])
x3=np.copy(temp[0:150,2])
x4=np.copy(temp[0:150,3])
con=np.append(x2,x3,axis=1)
print con.shape
'''
#print X
#Winputfile = sys.argv[1]
#temp=np.genfromtxt(inputfile,delimiter=",",dtype=float)
#X=np.copy(temp[0:2700,0:81])

#X = scale(X)
#pca = PCA(n_components=4)
#pca.fit(X)
#var= pca.explained_variance_ratio_
#print np.around(var, decimals=3)
'''
pca = PCA().fit(X)
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('number of components')
plt.ylabel('cumulative explained variance');
'''



#data = pd.read_csv(inputfile)

#convert it to numpy arrays
#X=data.values

#Scaling the values
'''
inputfile = sys.argv[1]
temp=np.genfromtxt(inputfile,delimiter=" ",dtype=float)
X=np.copy(temp[0:,0:temp.shape[1]])
X = scale(X)
compNo=temp.shape[1]
pca = PCA(n_components=compNo-1)

pca.fit(X)

#The amount of variance that each PC explains
var= pca.explained_variance_ratio_
#print np.around(var, decimals=3)
varianceMatrix= np.around(var, decimals=3)
ind = np.argpartition(varianceMatrix, -4)[-4:]
print ind
'''
#print var
#Cumulative Variance explains
#var1=np.cumsum(np.round(pca.explained_variance_ratio_, decimals=4)*100)

#print var1

#plt.plot(var1)


#Looking at above plot I'm taking 30 variables

##########################################################

inputfile = sys.argv[1]
temp=np.genfromtxt(inputfile,delimiter=",",dtype=float)
X=np.copy(temp[0:,0:temp.shape[1]])
X = scale(X)
compNo=temp.shape[1]
pca = PCA(n_components=compNo-1)

#pca = PCA(n_components=470)
pca.fit(X)
var= pca.explained_variance_ratio_
a= np.around(var, decimals=3)
X1=pca.fit_transform(a)
np.savetxt('tt.txt', X1)
##########################################################


#print X1
