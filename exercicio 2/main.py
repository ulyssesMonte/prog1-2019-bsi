while True:
  x1=int(input("1° num: "))
  x2=int(input("2° num: "))
  print("selecione a operação\n 1-( + )adição\n2-( - ) subtração\n3-( X ) multiplicação\n4-( : ) divisão\n5-( √ ) raiz quadrada\n6-( ^ ) exponenciação")
  menu=int(input())
  if menu == 1:
    print(x1+x2)
  elif menu == 2:
    print(x1-x2)
  elif menu == 3:
    print(x1*x2)
  elif menu == 4:
    print(x1/x2)
  elif menu == 5:
    print(x1**(1/x2))
  elif menu == 6:
    print(x1**x2)