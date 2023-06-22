import forca
import aula01

def escolhe_jogo():
    print("****************************")
    print("******escolhe o seu jogo!***")
    print("****************************")

    print("(1)Forca e (2) Adivinhação")

    jogo = int(input("Qual jogo?"))

    if(jogo==1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo==2):
        print("Jogando adivinhação")
        aula01.jogar()
if (__name__ == "__main__"):
    escolhe_jogo()