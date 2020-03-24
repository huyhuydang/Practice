import math
c = 50
h = 30
arr = []
items = [x for x in input("Nhap vao chuoi: ").split(',')]
print(items)
for d in items:
	kq = math.sqrt((2*c*float(d))/h)
	arr.append(round(kq))
print(arr)