import advinhacao
import forca


def escolher_jogo():
    print("----------------------------------")
    print("--------Escolha o seu Jogo!-------")
    print("----------------------------------")

    print("(1) Forca // (2) Advinhação")

    jogo = int(input("Digite o número do jogo que você deseja jogar: "))

    if jogo == 1:
        print("Você escolheu o jogo da Forca!")
        forca.jogar()
    elif jogo == 2:
        print("Você escolheu o jogo da Advinhação!")
        advinhacao.jogar()

if __name__ == "__main__":
    escolher_jogo()