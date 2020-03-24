values = [x for x in input("Nhap chuoi so: ").split(',') if(int(x) % 2 != 0)]
print(",".join(values))