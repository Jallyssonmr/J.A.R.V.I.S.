from Posts import *
from MessageCoding import MessageCoding
from DecisionTree import *

def Run(request):
	postsCoding = []
	for post in postsRequest:
		messageCoding = MessageCoding(post)
		postsCoding.append(messageCoding)

	features = NormalizeSize(postsCoding)

	classifier = DecisionTree()
	classifier = TrainModel(classifier, features[1], postsResponse)

	message = MessageCoding(request)

	while (len(message) < features[0]):
		message.append(0)

	response = TestModel(classifier, message)

	return (response[-1])

def NormalizeSize(postsCoding):
	length = 0
	for post in postsCoding:
		if (len(post) > length):
			length = len(post)

	for i, post in enumerate(postsCoding):
		while (len(post) < length):
			post.append(0)
		postsCoding[i] = post

	return (length, postsCoding)