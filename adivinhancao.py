import random

print("********************************")
print("Bem vindo no jogo de adivinhação!")
print("********************************")

numero_secreto = random.randrange(0, 101)  # 0.0 1.0
total_de_tentativas = 3

print("Qual nivel de Dificuldade?")
print("(1) facil (2) Medio (3) Dificil")

nivel = int(input("Defina o nivel: "))

if (nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2 ):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Voce deve digitar um numero entre 1 e 100")
        continue

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

print("Fim do jogo")