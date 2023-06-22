import forca
import aula01
print("****************************")
print("******escolhe o seu jogo!***")
print("****************************")

print("(1)Forca e (2) Adivinhação")

jogo = int(input("Qual jogo?"))

if(jogo==1):
    print("Jogando forca")
elif(jogo==2):
    print("Jogando adivinhação")