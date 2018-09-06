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
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

print "GaussianNB : "
from sklearn.naive_bayes import GaussianNB
GNB = GaussianNB()
t0= time()
GNB.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
print GNB.score(features_test,labels_test)
print

print "rbf Classifier, C = 10000.0"
from sklearn.svm import SVC
SVM = SVC(kernel="rbf",C = 10.0)
print "start training"
t0= time()
SVM.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
print SVM.score(features_test,labels_test)
print

print "DecisionTreeClassifier"
from sklearn import tree
dt = tree.DecisionTreeClassifier( min_samples_split=2 )
t0=time()
dt.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
print dt.score(features_test,labels_test)
print

print "KNN"
from sklearn import neighbors
knn = neighbors.KNeighborsClassifier()
t0=time()
knn.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
print knn.score(features_test,labels_test)
print

from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier, VotingClassifier


#Random Forest - Ensemble of Descision Trees

print "RandomForestClassifier"
rf = RandomForestClassifier(n_estimators=20)
t0=time()
rf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"

print rf.score(features_test,labels_test)
print

#Boosting - Ada Boost
print "AdaBoostClassifier"
t0=time()
adb = AdaBoostClassifier(tree.DecisionTreeClassifier(),n_estimators = 5, learning_rate = 1)
print "training time:", round(time()-t0, 3), "s"
adb.fit(features_train,labels_train)

print adb.score(features_test,labels_test)
print
try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
