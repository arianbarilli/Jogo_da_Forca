import os
import time
    
def carregando():
    contagem = 0
    limpa_Tela()
    if contagem == 0 :
        print("Carregando... \n█▒▒▒▒▒▒▒▒▒\n 10%")
        soneca()
        limpa_Tela()
        contagem = contagem + 1

    if contagem == 1 :
        print("Carregando... \n███▒▒▒▒▒▒▒\n 30%")
        soneca()
        limpa_Tela()
        contagem = contagem + 1
    
    if contagem == 2 :
        print("Carregando... \n█████▒▒▒▒▒\n 50%")
        soneca()
        limpa_Tela()
        contagem = contagem + 1

    if contagem == 3 :
        print("Carregando... \n██████████\n 100%")
        soneca()
        limpa_Tela()
        contagem = contagem + 1

def limpa_Tela():
    os.system("cls")

def sonhador():
    time.sleep(3)

def dormir():
    time.sleep(2)

def soneca():
    time.sleep(1)

def desenha_forca(chances):
    if chances == 5:
        print()
        print("|-----    ")
        print("|    |    ")
        print("|         ")
        print("|         ")
        print("|         ")
        print("|         ")
        print("_         ")
        print()
            
    elif chances == 4:
        print()
        print("|-----     ")
        print("|    |     ")
        print("|    O     ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("_          ")
        print()
            
    elif chances == 3:
        print()
        print("|-----     ")
        print("|    |     ")
        print("|    O     ")
        print("|    |     ")
        print("|    |     ")
        print("|          ")
        print("|          ")
        print("_          ")
        print()
            
    elif chances == 2:
        print()
        print("|-----     ")
        print("|    |     ")
        print("|    O     ")
        print("|   /|     ")
        print("|    |     ")
        print("|          ")
        print("|          ")
        print("_          ")
        print()
            
    elif chances == 1:
        print()
        print("|-----      ")
        print("|    |      ")
        print("|    O      ")
        print("|   /|\     ")
        print("|    |      ")
        print("|           ")
        print("|           ")
        print("_           ")
        print()

def desenho_final(chances):
    if chances == 0:
        limpa_Tela()
        print()
        print("|-----      ")
        print("|    O    Adeus Mundo Cruel  ")
        print("|   /|\     ")
        print("|    |      ")
        print("|   / \     ")
        print("|           ")
        print("_           ")
        sonhador()
        limpa_Tela()

        print()
        print("|-----      ")
        print("|    |      ")
        print("|    O      ")
        print("|   /|\     ")
        print("|    |      ")
        print("|   / \     ")
        print("|           ")
        print("_           ")
        soneca()
        limpa_Tela()
        
        print()
        print("|-----      ")
        print("|    |      ")
        print("|  \ O /    ")
        print("|    |      ")
        print("|    |      ")
        print("|   / \     ")
        print("|           ")
        print("_           ")
        soneca()
        limpa_Tela()
