import string

numbers = []
for i in range(10):
	numbers.append(str(i))

portugueseAlphabet = list(string.ascii_lowercase)
portugueseAlphabet.extend(numbers)
representation = [0 for i in range(len(portugueseAlphabet))]

def MessageCoding(message):
	message = list(message)
	messageCoding = []
	for character in message:
		if (character != ' '):
			index = portugueseAlphabet.index(character)
			characterCoding = list(representation)
			characterCoding[index] = 1
			messageCoding.extend(characterCoding)

	return (messageCoding)