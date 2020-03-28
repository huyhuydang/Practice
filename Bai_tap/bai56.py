def throws():
	return 5/0
# Bài Python 56, Code by Quantrimang.com
	try:
		throws()
	except ZeroDivisionError:
		print ("Chia một số cho 0!")
	except Exception as problem:
		print ('Bắt được một exception')
	finally:
		print ('Phép tính bị hủy')