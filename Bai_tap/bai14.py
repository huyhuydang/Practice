values = [x for x in input("Nhap day so nhi phan: ").split(',') ]

for item in values:
	if int(item, 2) % 5 == 0:
		print("%s --> %s"%(item,int(item, 2)))