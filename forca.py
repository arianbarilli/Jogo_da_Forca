import random
import os
os.system("cls")
print('====================================================   ')
print('========== BEM VINDO(A) AO JOGO DA FORCA! ==========   ')
print('====================================================   ')
print("                     *\(^o^)/*                       \n")

palavra = []
def carrega_palavras():
    arquivo = open("palavras.txt", "r", encoding = "utf-8")
    for pSecreta in arquivo.readlines():
        pSecreta = pSecreta.strip()
        if pSecreta != "":
            palavra.append(pSecreta)
    arquivo.close()
carrega_palavras()

pSecreta = palavra[random.randint(0, len(palavra)-1)]
tentativas = []
alfabeto = list("AÁÀÂÃaáàãâBbCcçÇDdEÊÉÈeéèêFfGgHhIÍÌÎiíìîJjKkLlMmNnOÓÒÔÕoóòôõPpQqRrSsTtUÚÙÛuúùûVvWwXxYyZz")
chances = 6

while True:

    letras = str(input("Digite uma letra ou 'exit' para sair: "))
    os.system("cls")

    if letras == "exit":
        break

    if letras in tentativas:
        print("Você já digitou essa letra, tente outra ")
        continue
    
    if len(letras)>1 and letras not in pSecreta:
        print("Só é possivel digitar uma letra, ou você digitou a palavra errada ")
        continue

    if letras not in alfabeto and letras not in pSecreta:
        print(f'ERRO, vovê digitou " {letras} " isso não é uma letra, tente novamente ')
        continue

    tentativas.append(letras)

    verificacao = ''
    for letra_secreta in pSecreta:
        if letra_secreta in tentativas:
            verificacao += letra_secreta 
        else:
            verificacao += '*'

    if letras in pSecreta:
        print(f'A palavra secreta contem " {letras} " ')

    if letras not in pSecreta:
        chances -= 1
        print(f'A palavra secreta não contem " {letras} " ou você digitou ela errada ')
       
    print(f'Você tem {chances} chances')
    print(f'Palavra secreta = {verificacao} ')
    
    if chances == 6:
        print()
        print("|----- ")
        print("|    | ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
            
    if chances == 5:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
            
    if chances == 4:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|    | ")
        print("|    | ")
        print("|      ")
        print("_      ")
        print()
            
    if chances == 3:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /| ")
        print("|    | ")
        print("|      ")
        print("_      ")
        print()
            
    if chances == 2:
        print()
        print("|-----  ")
        print("|    |  ")
        print("|    O  ")
        print("|   /|\ ")
        print("|    |  ")
        print("|       ")
        print("_       ")
        print()
            
    if chances == 1:
        print()
        print("|-----  ")
        print("|    |  ")
        print("|    O  ")
        print("|   /|\ ")
        print("|    |  ")
        print("|   /   ")
        print("_       ")
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
        break

    if chances == 0:
        os.system("cls")
        print(f'A palavra secreta era: {pSecreta} \n ')
        print("Você foi enforcado ¯\_('-')_/¯ ")
        print()
        print("|-----  ")
        print("|    |  ")
        print("|    O  ")
        print("|   /|\ ")
        print("|    |  ")
        print("|   / \ ")
        print("_       ")
        print()
        print("Mais sorte da próxima vez :)")
        break
