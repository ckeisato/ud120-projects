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
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 

clf = SVC(C=10000, kernel='rbf')
clf.fit(features_train, labels_train)
result = clf.predict(features_test)
# accuracy = accuracy_score(result, labels_test)
# print(result[10])
# print(result[26])
# print(result[50])

chris = 0
for item in result:
	if item == 1:
		chris +=1

print(chris)

#########################################################
### your code goes here ###

#########################################################


