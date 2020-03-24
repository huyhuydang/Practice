s = input("Nhap vao chuoi: ")
check = {"DIGITS":0, "LETTERS":0}
for c in s:
	if c.isdigit():
		check["DIGITS"] += 1
	elif c.isalpha():
		check["LETTERS"] += 1
	else:
		pass
print("So chu cai trong chuoi '%s' la: %s"%(s, check["LETTERS"]))
print("So chu so trong chuoi '%s' la: %s"%(s, check["DIGITS"]))