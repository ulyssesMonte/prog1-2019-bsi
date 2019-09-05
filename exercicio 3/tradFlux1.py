#-1
k=1
x=1
y=1
z=1
a=int(input("A: "))
b=int(input("B: "))
if (a > 15):
  x = x * 4
  if (b < 10):
    k = k + 1
  x = x * 5
  if (b == 10):
    k = k + 2
else:
  y = y + 1
  if (a>10):
    y = y + 2
    if (a > 5):
      x = x * 2
    else:
      x = 0
    z = z + 3
  else:
    x = x * 3
  z = z + 4
z = z + 5
print(x,y,z,k)



