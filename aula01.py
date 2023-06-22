import random

print("****************************")
print("Bem vindo ao curso da Alura")
print("****************************")


numero_secreto= random.randrange(1,101)
total_de_tentivas=0
pontos = 1000

print("Qual o nivel de dificuldade?")
print("(1)facil,(2)medio,(3)dificil")
nivel = int(input("Define o nivel: "))
if (nivel ==1):
    total_de_tentivas=20
elif(nivel==2):
    total_de_tentivas=10
else:
    total_de_tentivas=5
rodada = 1
for rodada in range(1, total_de_tentivas +1):
    print("Tentativa {}de{}".format(rodada, total_de_tentivas))
    chute_str = input("Digite o seu chute: ")
    print("Você digitou",chute_str)
    chute= int(chute_str)
    if(chute<1 or chute>100):
        print("Voce deve digitar um numero 1 a 100!")
        continue
    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto


    if(acertou):
        print("Você acertou e fez {}!".format(pontos))
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o numero secreto")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o numero secreto")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
    rodada = rodada+1
print("Fim de jogo")