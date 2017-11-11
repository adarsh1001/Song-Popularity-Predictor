
from sklearn import svm
from sklearn import preprocessing
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.manifold.t_sne import TSNE

import argparse, os, sys

def get_input_data(filename):
    """
    Function to read the input data from the letter recognition data file.

    Parameters
    ----------
    filename: The path to input data file

    Returns
    -------
    X: The input for the SVM classifier of the shape [n_samples, n_features].
       n_samples is the number of data points (or samples) that are to be loaded.
       n_features is the length of feature vector for each data point (or sample).
    Y: The labels for each of the input data point (or sample). Shape is [n_samples,].

    """

    dataset = np.genfromtxt(filename, delimiter=',')[:,:-1]
    x = dataset[:,0:82];
    y = dataset[:, 82];


    """
    An important part is missing here. Corresponding to point (1) in "Remember".
    ===========================================================================
    """

    # YOUR CODE GOES HERE
    scaler  = preprocessing.StandardScaler()
    X = scaler.fit_transform(x)

    """
    ===========================================================================
    """

    return X, y

def calculate_metrics(predictions, labels):
    """
    Function to calculate the precision, recall and F-1 score.

    Parameters
    ----------
    predictions: The predictions obtained as output from the SVM classifier
    labels: The true label values corresponding to the entries in predictions

    Returns
    -------
    precision: true_positives / (true_positives + false_positives)
    recall: true_positives / (true_positives + false_negatives)
    f1: 2 * (precision * recall) / (precision + recall)
    ===========================================================================
    """

    # YOUR CODE GOES HERE
    return precision_recall_fscore_support(predictions, labels, average='macro')

    """
    ===========================================================================
    """

    return precision, recall, f1

def calculate_accuracy(predictions, labels):
    """
    Function to calculate the accuracy for a given set of predictions and
    corresponding labels.

    Parameters
    ----------
    predictions: The predictions obtained as output from the SVM classifier
    labels: The true label values corresponding to the entries in predictions

    Returns
    -------
    accuracy: Fraction of total samples that have correct predictions (same as
    true label)

    """
    return accuracy_score(labels, predictions)

def SVM(train_data,
        train_labels,
        test_data,
        test_labels,
        kernel='rbf'):
    """
    Function to create, train and test the one-vs-all SVM using scikit-learn.

    Parameters
    ----------
    train_data: Numpy ndarray of shape [n_train_samples, n_features]
    train_labels: Numpy ndarray of shape [n_train_samples,]
    test_data: Numpy ndarray of shape [n_test_samples, n_features]
    test_labels: Numpy ndarray of shape [n_test_samples,]
    kernel: linear (default)
            Which kernel to use for the SVM

    Returns
    -------
    accuracy: Accuracy of the model on the test data
    top_predictions: Top predictions for each test sample
    precision: The precision score for the test data
    recall: The recall score for the test data
    f1: The F1-score for the test data

    """

    """
    Create an SVM instance with the required parameters and train it.
    For details on how to do this in scikit-learn, refer:
        http://scikit-learn.org/stable/modules/svm.html
    ==========================================================================
    """

    # YOUR CODE GOES HERE
    clf  = svm.SVC(kernel=kernel, C=100.0, gamma = 0.1,coef0=0.0, random_state=None, tol =0.001)
    clf.fit(train_data, train_labels)
    train_predictions = clf.predict(test_data)

    #print train_labels


    #print "TRAIN DATA SHAPE", train_data.shape
    #print "TEST LABELS SHAPE" , train_labels.shape

    """
    ==========================================================================
    """

    """
    Calculates training accuracy. Replace predictions and labels with your
    respective variable names.
    """
    train_accuracy = calculate_accuracy(train_predictions, test_labels)
    #print "Training Accuracy: %.4f" % (train_accuracy)

    """
    Use the trained model to perform testing. Using the output of the testing
    prodecure, get the top prediction for each sample and calculate the accuracy
    on test data using the function given (as shown above for train accuracy).

    Also, complete the function given above for metrics using scikit-learn and
    return their values in this function.
    ==========================================================================
    """

    # YOUR CODE GOES HERE

    precision, recall, f1, support = calculate_metrics(train_predictions, test_labels)


    """
    ==========================================================================
    """

    return train_accuracy, precision, recall, f1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', default=None,
            help='path to the directory containing the dataset file')

    args = parser.parse_args()
    if args.data_dir is None:
        #print "Usage: python letter_classification_svm.py --data_dir='<dataset dir path>'"
        sys.exit()
    else:
        filename = os.path.join(args.data_dir, 'MSD_DATASET.txt')
        try:
            if os.path.exists(filename):
                pass
                #print "Using %s as the dataset file" % filename
        except:
            #print "%s not present in %s. Please enter the correct dataset directory" % (filename, args.data_dir)
            sys.exit()

    # Set the value for svm_kernel as required.
    svm_kernel = 'rbf'

    """
    Get the input data using the provided function. Store the X and Y returned
    as X_data and Y_data. Use filename found above as the input to the function.
    ==========================================================================
    """

    # YOUR CODE GOES HERE
    X_data, Y_data = get_input_data(filename)
    

    """
    ==========================================================================
    """

    """
    We use 5-fold cross validation for reporting the final scores and metrics.
    Code to generate the 5-folds (You can change the split function to something
    else that you like as well) and then calling the SVM to classify the present
    split.
    ==========================================================================
    """
    sss = StratifiedShuffleSplit(n_splits=5, test_size=0.125)   # Do not change this split size
    accumulated_metrics = []
    fold = 1
    for train_indices, test_indices in sss.split(X_data, Y_data):
        #print "Fold%d -> Number of training samples: %d | Number of testing "\
#    "samples: %d" % (fold, len(train_indices), len(test_indices))
        train_data, test_data = X_data[train_indices], X_data[test_indices]
        train_labels, test_labels = Y_data[train_indices], Y_data[test_indices]
        accumulated_metrics.append(
            SVM(train_data, train_labels, test_data, test_labels,
                svm_kernel))
        fold += 1

    """
    Print out the accumulated metrics in a good format.
    ==========================================================================
    """
    accuracy_val = 0.
    precision_val = 0.
    recall_val=0.
    f_1_val=0.
    #print "Accumulated metrics:"
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

    # YOUR CODE GOES HERE

    """
    ==========================================================================
    """
