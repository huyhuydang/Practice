class HinhChuNhat(object):
	def __init__(self,dai, rong):
		self.dai = dai
		self.rong = rong
	def area(self):
		print("Dien tich hinh chu nhat la:",self.dai*self.rong)

hcn1 = HinhChuNhat(3,5)
hcn1.area()

HinhChuNhat(2,5).area()