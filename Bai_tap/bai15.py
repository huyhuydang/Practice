values = []
for x in range(1000,3001):
	s = str(x)
	a = int(s[0])
	b = int(s[1])
	c = int(s[2])
	d = int(s[3])
	if (a % 2 == 0) and (b % 2 == 0) and (c % 2 == 0) and (d % 2 == 0):
		values.append(s)

print(",".join(values))