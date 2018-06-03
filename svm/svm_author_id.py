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



from sklearn.svm import SVC
clf = SVC(kernel="rbf",C=10000)


#### now your job is to fit the classifier
#### using the training features/labels, and to
#### make a set of predictions on the test data
t0 = time()
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"



#### store your predictions in a list named pred
t0 = time()
preds = clf.predict(features_test)
print "predicting time:", round(time()-t0, 3), "s"
print preds[10]
print preds[26]
print preds[50]


counter=0


"""count of chris predictions"""
for pred in preds:
	if pred==1:
		counter=counter+1


print counter


from sklearn.metrics import accuracy_score
acc = accuracy_score(preds, labels_test)

print(acc)


