import math
g = 9.81
pi = math.pi
print('L    T')
for i in range(1, 21, 2):
	L=i / 10
	T = 2 * pi * math.sqrt(L / g)
	print(f'{L:.1f}m {T:.4f}c')