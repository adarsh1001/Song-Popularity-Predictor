# Logistic Regression
import sys
import os
import numpy as np
from sklearn import datasets
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
#Remove comment from here


inputfile = sys.argv[1]
#x=np.genfromtxt(traindir,delimiter=",",dtype=int)
#test=np.genfromtxt(testdir,delimiter=",",dtype=int)
temp=np.genfromtxt(inputfile,delimiter=",",dtype=float)

x_train=np.copy(temp[0:2700,0:81])
y_train=np.copy(temp[0:2700,82])
x_test=np.copy(temp[2701:,0:81])
y_test=np.copy(temp[2701:,82])


# load the iris datasets
#dataset = datasets.load_iris()
# fit a logistic regression model to the data
#model = LogisticRegression()
#model.fit(x_train,y_train)
mul_model =LogisticRegression(multi_class='multinomial', solver='newton-cg').fit(x_train,y_train)
#print(model)
# make predictions
print "Multinomial Logistic regression Train Accuracy :: ", metrics.accuracy_score(y_train, mul_model.predict(x_train))
print "Multinomial Logistic regression Test Accuracy :: ", metrics.accuracy_score(y_test, mul_model.predict(x_test))
print mul_model.predict(x_test)
#model.predict(x_test)
#expected = y_test
#predicted = model.predict(x_test)
# summarize the fit of the model
#print(metrics.classification_report(expected, predicted))
#print(metrics.confusion_matrix(expected, predicted))
#print "Multinomial Logistic regression Test Accuracy :: ", metrics.accuracy_score(test_y, mul_lr.predict(test_x))