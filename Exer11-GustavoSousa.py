#Você é um desenvolvedor de sistemas trabalhando em um projeto colaborativo com sua equipe.
#Para garantir que todas as tarefas do projeto sejam concluídas dentro do prazo, você decide criar um pequeno programa para controlar o status das tarefas.
#O programa deve permitir que você insira o nome de cada tarefa e indique se ela está concluída ou não.
#No final, o programa deve apresentar um resumo com o total de tarefas, quantas estão concluídas e quantas ainda estão pendentes.

#Desenvolva um programa em Python que:
    # 1.	Solicite ao usuário o número de tarefas a serem inseridas.
    # 2.	Para cada tarefa, solicite o nome da tarefa e se ela está concluída (aceitando "sim", "s", "não" ou "n").
    # 3.	Conte e exiba o número de tarefas concluídas e não concluídas.

n1 = int(input("Digite o numero de tarefas : "))
nao_con = 0
sim_con = 0
for i in range(n1):
    nome = str(input("Digite o nome da tarefa : "))
    con = str(input("Digite se foi concluida com sim/s ou nao/n : "))
    if con == "s" or con == "S":
        nao_con += 1
    else:
        sim_con += 1
print ("Tarefas concluidas",sim_con)
print ("Tarefas não concluidas",nao_con)
#Erro na digitaçao
