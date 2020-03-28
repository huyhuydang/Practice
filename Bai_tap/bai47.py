li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
li1 = filter( lambda x: x % 2 == 0, li)
SquareOfEvenNumbers = list( map( lambda x: x ** 2, list(li1)))
print(SquareOfEvenNumbers)