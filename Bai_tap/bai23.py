def putNumber(n):
	i = 0
	while i < n:
		j = i
		i += 1
		if j % 7 == 0:
			yield j
for x in putNumber(50):
	print(x)
print(putNumber(10))