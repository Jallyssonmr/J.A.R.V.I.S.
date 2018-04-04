from sklearn import tree

def DecisionTree():
	classifier = tree.DecisionTreeClassifier()
	return (classifier)

def TrainModel(classifier, features, labels):
	classifier.fit(features, labels)
	return (classifier)

def TestModel(classifier, features):
	result = classifier.predict([features])
	return (result)