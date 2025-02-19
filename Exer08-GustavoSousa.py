#Defina uma variável chamada TOTAL como 0 .peça ao usuário para colocar 5 números
#e após cada entrada pergunte se ele deseja que esse numero seja incluído (S ou s),(N ou n).
#se ele desejar adicione ao total . se ele não quiser inclui-lo não adicione ao total. Depois de inserir 5 números exiba o total
total = 0
for i in range(5):
   num = int(input("Digite um numero :"))
   aa = str(input ("Deseja continuar s/n :"))
   soma =+num
   if aa == "n":
      break
print (soma)
dadwf