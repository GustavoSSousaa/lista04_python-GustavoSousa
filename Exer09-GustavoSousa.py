#- Faça um programa que pergunte em qual direção o usuário deseja contar “C ou c” se ele selecionar para cima , peça um numero superior e conte ate esse numero 
#“A ou a” se ele selecionar para baixar peça para inserir abaixo de 20 e em seguida faça a contagem regressiva de 20 ate esse numero
# Se ele inserir algo diferente diga a mensagem “direção invalida”.
print ("")
di = str(input("Digite a Direção que voce quer :"))
if di == "C" or "c":
    n1 = int(input("Digite um numero :"))
    for i in range(n1):
     print(i)
elif di == "A" or "a":
    n1 = int(input("Digite um numero :"))
    for i in range(n1):
        aa = 50 - i
        print (aa)
        if aa == n1:
            break
else:
    print ("Direção invalida")
#acabei