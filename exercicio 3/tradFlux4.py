#-4
D=0
M=0
A=0
Resto=0
D=int(input("D:"))
M=int(input("M:"))
A=int(input("A:"))
if M==2:
  Resto=A%4
  if Resto==1:
    if (D>0)and(D<30):
      print("VÁLIDA")
    else:
      print("INVÁLIDA")
  else:
    if (D>0)and(D<29):
      print("VÁLIDA")
    else:
      print("INVÁLIDA")
else:
  if (M==4)or(M==9)or(M==11):
    if(D>0)and(D<31):
      print("VÁLIDA")
    else:
      print("INVÁLIDA")
  else:
    if (D<32)and(D>0):
      print("VÁLIDA")
    else:
      print("INVÁLIDO")