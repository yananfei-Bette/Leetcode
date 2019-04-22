x = 2437
y = 875

while x != y:
	if x > y:
		x -= y
	if x < y:
		y -= x
print (x, y)