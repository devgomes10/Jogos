import random


def jogar():
    print("----------------------------------")
    print("Bem vindo ao jogo de Adivinhação!!!")
    print("----------------------------------")

    numero_secreto = round(random.randrange(1, 101))
    total_de_tentativas = 0
    pontos = 1000

    print("Qual seu nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) difícil")

    nivel = int(input("Digite seu nível: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodadas in range(1, total_de_tentativas + 1):
        print("tentativa {} de {}".format(rodadas, total_de_tentativas))
        chute = int(input("digite um número entre 1 e 100: "))
        print("Você digitou", chute)

        if chute < 1 or chute > 100:
            print("você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if acertou:
            print("você acertou o número e fez {} pontos".format(pontos))
            break
        else:
            if menor:
                print("você chutou um número menor!")
            elif maior:
                print("você digitou um número maior")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if __name__== "__main__":
    jogar()
