#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]
#########################################################
### your code goes here ###
print "\n\nFROM HERE...\n" 
from sklearn.svm import SVC

# print "Linear Classifier"
# clf = SVC(kernel="linear")
# print "start training"
# t0= time()
# clf.fit(features_train,labels_train)
# print "training time:", round(time()-t0, 3), "s"

# print clf.score(features_test,labels_test)
# print

# print "rbf Classifier"
# clf = SVC(kernel="rbf")
# print "start training"
# t0= time()
# clf.fit(features_train,labels_train)
# print "training time:", round(time()-t0, 3), "s"

# print clf.score(features_test,labels_test)
# print

# print "rbf Classifier, C = 10."
# clf = SVC(kernel="rbf",C = 10.0)
# print "start training"
# t0= time()
# clf.fit(features_train,labels_train)
# print "training time:", round(time()-t0, 3), "s"

# print clf.score(features_test,labels_test)
# print

# print "rbf Classifier, C = 100.0"
# clf = SVC(kernel="rbf",C = 100.0)
# print "start training"
# t0= time()
# clf.fit(features_train,labels_train)
# print "training time:", round(time()-t0, 3), "s"

# print clf.score(features_test,labels_test)
# print

# print "rbf Classifier, C = 1000.0"
# clf = SVC(kernel="rbf",C = 1000.0)
# print "start training"
# t0= time()
# clf.fit(features_train,labels_train)
# print "training time:", round(time()-t0, 3), "s"

# print clf.score(features_test,labels_test)
# print

print "rbf Classifier, C = 10000.0"
clf = SVC(kernel="rbf",C = 10000.0)
print "start training"
t0= time()
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"

print clf.predict([[10]])

print clf.score(features_test,labels_test)
print
