print("Nhap chuoi:")
lines = []
while True:
	s = input()
	if s:
		lines.append(s.upper())
	else:
		break
for xline in lines:
	print(xline)