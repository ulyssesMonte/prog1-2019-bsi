#-2
a=int(input("A: "))
b=int(input("B: "))
c=int(input("C: "))
if a==0:
  print("não é uma equação de segundo grau")
else:
    d=b*b-4*a*c
    if d<0:
      print("não existem raizes reais")
    else:
      r1=-(b+d**(1/2)/(1/2))
      r2=-(b-d**(1/2)/(1/2))
      print(r1,r2)
