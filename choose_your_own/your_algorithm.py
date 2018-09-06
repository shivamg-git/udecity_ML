#!/usr/bin/python
import sys
from time import time
import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
# plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

print "GaussianNB : "
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
t0= time()
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
print clf.score(features_test,labels_test)
print

print "rbf Classifier, C = 10000.0"
from sklearn.svm import SVC
clf = SVC(kernel="rbf",C = 10.0)
print "start training"
t0= time()
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
print clf.score(features_test,labels_test)
print

print "DecisionTreeClassifier"
from sklearn import tree
clf = tree.DecisionTreeClassifier( min_samples_split=2 )
t0=time()
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
print clf.score(features_test,labels_test)
print

print "KNN"
from sklearn import neighbors
clf = neighbors.KNeighborsClassifier()
t0=time()
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
print clf.score(features_test,labels_test)
print

print "ADABoost"




try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
