def q1():
   x=int(input("digite um número "))
   if x > 20 :
      print(x," é maior que 20")
def q2():
   x=int(input("digite um número "))
   if (x % 2) == 0 :
      print("PAR")
def q3():
   x=int(input("digite um número "))
   if (x % 2) != 0 :
      print("IMPAR")
def q4():
   x=int(input("digite um número "))
   if x < 0 :
      print(x," é um número negativo")
def q5():
   x1=int(input("digite um número "))
   x2=int(input("digite outro número "))
   x3= x1+x2
   if x3 > 10 :
      print(x1," + ",x2," é igual a ",x3,". e ",x3," é maior que 10")
def q6():
   x1=int(input("digite um número"))
   x2=int(input("digite outro número"))
   if x1==x2:
      print(x1," é igual a ",x2)
   elif x1 > x2 :
      print(x1," é maior que ",x2)
   else:
      print(x2," é maior que ",x1)
def q7():
   x1=int(input("digite um número"))
   x2=int(input("digite outro número"))
   if x1>x2:
      print(x1," - ", x2)
   else:
      print(x2," - ", x1)
def q8():
   print(" olá, vamos verificar se você pode pegar um empréstimo \n Por favor digite seu salário bruto: ")
   x1=float(input())
   x2=float(input("Digite o valor da prestação: "))
   if (x1/4) < x2 :
    print("empréstimo não aprovado")
   else: 
      print("empréstimo aprovado")
def q9():
   x1=int(input("Digite sua 1° nota: "))
   x2=int(input("Digite sua 2° nota: "))
   x3=int(input("Digite sua 3° nota: "))
   m=(x1+x2+x3)/3
   if  m>=60:
      print("Aprovado! ;)")
   else:
      print("Reprovado :/")
def q10():
   x1=int(input("digite um número"))
   x2=int(input ("digite outro número"))
   if x1 > x2:
      x3=x1/x2
      if type(x3) == 'int':
         print ("os números são múltiplos")
      else:
         print(" os números não são múltiplos")
   else:
      x3=x2/x1
      if type(x3) == 'int':
         print ("os números são múltiplos")
      else:
         print(" os números não são múltiplos")

while True:
  print("menu:\ndigite o número do problema que deseja resolver\n1-para descobrir se um número é maior do que 20\n2-para descobrir se um número é par\n3-para descobrir se um número é ímpar\n4-para descobrir se um número é negativo\n5-para somar dois números e descobrir se é maior que 10\n6-para descobrir qual é o maior número\n7-para por dois números em ordem crescente\n8-para consultar  se é um empréstimo é aprovado para você\n8-para calcular a média de suas notas\n10-descobrir se dois números são multiplos um do outro")
  menu=int(input())
  if menu == 1:
    q1()

  elif menu == 2:
    q2()
  elif menu == 3:
    q3()
  elif menu == 4:
    q4()
  elif menu == 5:
    q5()
  elif menu == 6:
    q6()
  elif menu == 7:
    q7()
  elif menu == 8:
    q8()
  elif menu == 9:
    q9()
  elif menu == 10:
    q10()