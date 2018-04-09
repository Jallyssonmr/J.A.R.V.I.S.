from Run import Run

def Parameters():
	print ("")
	print ("CAPPTA S.A.")
	print ("-----------")
	options = ["1 - todas as vendas", "2 - vendas canceladas", "3 - vendas stone"]
	print ("Diga algo..")
	print (options)

	while True:
		request = input("Eu: ")
		response = Run(request)
		print ("Bot: " + response)

Parameters()