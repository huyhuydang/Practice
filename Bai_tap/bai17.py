s = input("Nhap chuoi: ")
check = {"UPPERS": 0, "LOWER": 0}
for x in s:
	if x.isupper():
		check['UPPERS'] += 1
	elif x.islower():
		check["LOWER"] += 1
	else:
		pass
print("So chu cai in hoa:",check['UPPERS'])
print("So chu cai in thuong:",check['LOWER'])