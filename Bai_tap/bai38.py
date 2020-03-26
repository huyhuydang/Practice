def printList():
	li = list()
	for x in range(1,21):
		li.append(x**2)
	print(li[-5:])
printList()