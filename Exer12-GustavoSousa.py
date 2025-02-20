#Desenvolva um programa em Python que:
    #1.	Solicite à dona do salão para inserir os horários disponíveis na agenda.
    #2.	Exiba os horários disponíveis para a cliente.
    #3.	Permita que a cliente escolha um horário para agendamento.
    #4.	Atualize a agenda marcando o horário escolhido como ocupado.
    #5.	Pergunte se deseja agendar mais um horário e continue até que todos os horários estejam preenchidos ou a dona do salão decida parar.

n = int(input("Digite quantos horarios voce quer colocar : "))
horarios = []

for i in range(n):
    horario = int(input("Digite os horarios :"))
    horarios.append(horario)
print (horario)

