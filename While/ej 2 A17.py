d = 0
r = 13
s = r / 2
while s > 2 or r % 2 == 0 :
     d += 1
     r -= 2
     s -= 2

print(str(d) + " " + str(r) + " " + str(s))