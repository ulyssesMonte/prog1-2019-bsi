#-3
a=int(input("A: "))
resto4=a%4
resto100=a%100
resto400=a%400
if resto4==0:
  if resto100==0:
    if resto400==0:
      print("bissexto")
    else:
      print("não é bissexto")
  else:
    print("bissexto")
else:
  print("não é bissexto")