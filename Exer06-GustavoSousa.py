#Peça um numero abaixo de 50 e em seguida faça uma contagem regressiva de 50 ate esse numero, certificando-se de mostrar o numero que coloco na saída
n1 = int(input("Digite um numero ABAIXO DE 50 :"))
if n1 <50:
    for i in range(n1):
        aa = 50 - i
        print (aa)
        if aa == n1:
            break
else:
    print ("Numero muito alto")
