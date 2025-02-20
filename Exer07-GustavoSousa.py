#Peça ao usuário para colocar o seu nome e um numero .se o numero for menor que 10 exiba o nome dele esse numero de vezes
#caso contrario exiba a mensagem “numero muito alto” 3 vezes 
nome = str(input("Digite seu nome : "))
n1 = int(input("Digite um numero : "))
print ("")
if n1<10:
    for i in range(n1):
        print (nome)
else :
    for i in range(3):
        print ("NUMERO MUITO ALTO")
#acabei