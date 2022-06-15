import random
import os
import unicodedata
import time
os.system("cls")
print('====================================================   ')
print('========== BEM VINDO(A) AO JOGO DA FORCA! ==========   ')
print('====================================================   ')
print("                     *\(^o^)/*                       \n")

print("======================Iniciando======================")
time.sleep(1)

print("======================Carregando======================")
contagem = 0

if contagem == 0 :
    print("█▒▒▒▒▒▒▒▒▒\n 10%")
    time.sleep(2)
    os.system("cls")
    contagem = contagem + 1

if contagem == 1 :
    print("███▒▒▒▒▒▒▒\n 30%")
    time.sleep(1)
    os.system("cls")
    contagem = contagem + 1
    
if contagem == 2 :
    print("█████▒▒▒▒▒\n 50%")
    time.sleep(1)
    os.system("cls")
    contagem = contagem + 1

if contagem == 3 :
    print("███████▒▒▒\n 100%")
    time.sleep(1)
    os.system("cls")
    contagem = contagem + 1

palavra = []
def carrega_palavras():
    arquivo = open("palavras.txt", "r", encoding = "utf-8")
    for pSecreta in arquivo.readlines():
        pSecreta = pSecreta.strip().lower()
        if pSecreta != "":
            palavra.append(pSecreta)
    arquivo.close()
carrega_palavras()

pSecreta = palavra[random.randint(0, len(palavra)-1)]
tentativas = []
alfabeto = list("abcçdefghijklmnopqrstuvwxyzáàãâéèêíìîóòôõúùû")
maiusculas = list("ABCÇDEFGHIJKLMNOPQRSTUVWXYZÁÀÂÃÊÉÈÍÌÎÓÒÔÕÚÙÛ")
chances = 6

def remove_acento(string: str) -> str:
    normalized = unicodedata.normalize('NFD', string)
    return normalized.encode('ascii', 'ignore').decode('utf8')

while True:

    letras = str(input("Digite uma letra minúscula ou 'exit' para sair: ")) 
    os.system("cls")

    if letras == "exit":
        break

    elif letras in tentativas:
        print("Você já digitou essa letra, tente outra ")
        continue
    
    elif len(letras)>1 and letras != pSecreta:
        print("Só é possivel digitar uma letra, ou você digitou a palavra errada, verifique a escrita e acentuação ")
        continue

    elif letras in maiusculas:
        print("Digite Apenas letras minúsculas")
        continue

    elif letras not in alfabeto and letras not in pSecreta:
        print(f'ERRO, vovê digitou " {letras} " isso não é uma letra, tente novamente ')
        continue

    tentativas.append(letras)

    sem_acento = remove_acento(pSecreta)

    verificacao = ''
    for posicao, letra_secreta in enumerate(sem_acento):
        if letra_secreta in tentativas:
            verificacao += pSecreta[posicao] 
        else:
            verificacao += '*' 

    if letras in pSecreta:
        print(f'A palavra secreta contem " {letras} " ')

    elif letras not in sem_acento:
        chances -= 1
        print(f'A palavra secreta não contem " {letras} " ou você digitou ela errada ')
       
    print(f'Você tem {chances} chances')
    print(f'Palavra secreta = {verificacao} ')
    
    if chances == 6:
        print()
        print("|----- ")
        print("|    |    ")
        print("|         ")
        print("|         ")
        print("|         ")
        print("|         ")
        print("_         ")
        print()
            
    elif chances == 5:
        print()
        print("|-----     ")
        print("|    |     ")
        print("|    O     ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|           ")
        print("_          ")
        print()
            
    elif chances == 4:
        print()
        print("|-----     ")
        print("|    |     ")
        print("|    O     ")
        print("|    |     ")
        print("|    |     ")
        print("|          ")
        print("|           ")
        print("_          ")
        print()
            
    elif chances == 3:
        print()
        print("|-----     ")
        print("|    |     ")
        print("|    O     ")
        print("|   /|     ")
        print("|    |     ")
        print("|          ")
        print("|           ")
        print("_          ")
        print()
            
    elif chances == 2:
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
            
    elif chances == 1:
        print()
        print("|-----      ")
        print("|    |      ")
        print("|    O      ")
        print("|   /|\     ")
        print("|    |      ")
        print("|   /       ")
        print("|           ")
        print("_           ")
        print()

    if verificacao == pSecreta or letras == pSecreta:
        os.system("cls")
        print(f'A palavra secreta era: {pSecreta} \n ')
        print("PARABÉNS, você venceu! \(^-^)/ ")
        print("     ___________      ")
        print("    '._==_==_=_.'     ")
        print("    .-\:      /-.     ")
        print("   | (|:.     |) |    ")
        print("    '-|:.     |-'     ")
        print("      \::.    /       ")
        print("       '::. .'        ")
        print("         ) (          ")
        print("       _.' '._        ")
        print('       """""""        ')
        print()
        print()
        break

    if chances == 0:
        os.system("cls")
        print(f'A palavra secreta era: {pSecreta} \n ')
        print()
        print("|-----      ")
        print("|    O      ")
        print("|   /|\     ")
        print("|    |      ")
        print("|   / \     ")
        print("|           ")
        print("_           ")
        time.sleep(3)
        os.system("cls")
        print("|-----      ")
        print("|    |      ")
        print("|    O      ")
        print("|   /|\     ")
        print("|    |      ")
        print("|   / \     ")
        print("|           ")
        print("_           ")
        time.sleep(1)
        os.system("cls")
        print("|-----      ")
        print("|    |      ")
        print("|  \ O /    ")
        print("|    |      ")
        print("|    |      ")
        print("|   / \     ")
        print("|           ")
        print("_           ")
        time.sleep(1)
        os.system("cls")
        print("Você foi enforcado ¯\_('-')_/¯ ")
        print("|-----      ")
        print("|    |      ")
        print("|    |      ")
        print("|    O      ")
        print("|   /|\     ")
        print("|    |      ")
        print("|   / \     ")
        print("|           ")
        print("_           ")
        print()
        print("Mais sorte da próxima vez ('-')")
        print()
        print()
        time.sleep(2)
        break
    