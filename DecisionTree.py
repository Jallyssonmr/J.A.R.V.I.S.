from sklearn import tree
from sklearn.svm import SVC

def DecisionTree():
	classifier = tree.DecisionTreeClassifier()
	clf = SVC()
	return (classifier)

def TrainModel(classifier, features, labels):
	classifier.fit(features, labels)
	return (classifier)

def TestModel(classifier, features):
	result = classifier.predict([features])
	return (result)