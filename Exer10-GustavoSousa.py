#Faça um programa que pergunte quantas pessoas o usuário deseja convidar para uma festa.
#Se ele digitar um número abaixo de 10, peça os nomes e após cada nome exiba a mensagem: "[nome] está convidado para a festa".
#Se ele inserir um número 10 ou superior, exiba a mensagem "Muitas pessoas"
n1 = int(input("Digite o numero de pessoas que vai : "))
nomes = []
if n1<10:
    for i in range(n1):
        nome = str(input("Digite o nome do convidado : "))
        print ("")
        nomes.append(nome)
print("\nOs convidados sao :")
for nome in nomes:
    print (nome)
if n1 >= 10:
    print ("Numero de pessoas muito alto")
else:
    print ("Valor invalido")