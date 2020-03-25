import re
while True:
	s = input("Nhap mk: ")
	if len(s) < 6 or len(s) > 12:
		continue
	else:
		pass
	if not re.search("[a-z]",s):
		continue
	elif not re.search("[A-Z]",s):
		continue
	elif not re.search("[0-9]",s):
		continue
	elif not re.search("[$#@]",s):
		continue
	elif re.search("\\s",s):
		continue
	else:
		pass
	print("tm")
	break