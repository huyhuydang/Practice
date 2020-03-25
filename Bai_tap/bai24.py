import math
pos = [0,0]
while True:
	s = input()
	if not s:
		break
	th = s.split(' ')
	huong = th[0]
	buoc = int(th[1])
	if huong == "U":
		pos[1] += buoc
	if huong == "D":
		pos[1] -= buoc
	if huong == "L":
		pos[0] -= buoc
	if huong == "R":
		pos[0] += buoc
Kc = math.sqrt(pos[0]**2 + pos[1]**2)
print(round(Kc))	