from sklearn import svm
from sklearn import preprocessing
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import accuracy_score
import numpy as np

from sklearn.manifold.t_sne import TSNE

import argparse, os, sys

def get_input_data(inputfile):
    dataset=np.genfromtxt(inputfile,delimiter=",",dtype=float)
    x = dataset[:,0:dataset.shape[1]-1];
    y = dataset[:, dataset.shape[1]-1];
    scaler  = preprocessing.StandardScaler()
    X = scaler.fit_transform(x)
    return X,y
def calculate_metrics(predictions, labels):
    return precision_recall_fscore_support(predictions, labels, average='macro')

    return precision, recall, f1

def calculate_accuracy(predictions, labels):
    return accuracy_score(labels, predictions)

def SVM(train_data,
        train_labels,
        test_data,
        test_labels,
        kernel='rbf'):
    clf  = svm.LinearSVC(penalty='l2',multi_class='ovr', C=0.01, random_state=None, tol =0.001)
    clf.fit(train_data, train_labels)
    train_predictions = clf.predict(test_data)
    train_accuracy = calculate_accuracy(train_predictions, test_labels)
    precision, recall, f1, support = calculate_metrics(train_predictions, test_labels)
    return train_accuracy, precision, recall, f1


if __name__ == '__main__':
    svm_kernel = 'poly2'
    filename=sys.argv[1]
    X_data, Y_data = get_input_data(filename)
    sss = StratifiedShuffleSplit(n_splits=5, test_size=0.125)   # Do not change this split size
    accumulated_metrics = []
    fold = 1
    for train_indices, test_indices in sss.split(X_data, Y_data):
        train_data, test_data = X_data[train_indices], X_data[test_indices]
        train_labels, test_labels = Y_data[train_indices], Y_data[test_indices]
        accumulated_metrics.append(
            SVM(train_data, train_labels, test_data, test_labels,
                svm_kernel))
        fold += 1

    accuracy_val = 0.
    precision_val = 0.
    recall_val=0.
    f_1_val=0.
    for metric in accumulated_metrics:
        accuracy_val+=metric[0]
        precision_val+=metric[1]
        recall_val+=metric[2]
        f_1_val+=metric[3]

    accuracy_val/=5.
    precision_val/=5.
    recall_val/=5.
    f_1_val/=5.


    print accuracy_val , precision_val, recall_val, f_1_val

