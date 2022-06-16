import unicodedata
from funcoes import limpa_Tela,desenha_forca,desenho_final,dormir,carregando,sonhador
limpa_Tela()
print('====================================================   ')
print('========== BEM VINDO(A) AO JOGO DA FORCA! ==========   ')
print('====================================================   ')
print("                     *\(^o^)/*                       \n")

print("Iniciando...")
dormir()

alfabeto = list("abcçdefghijklmnopqrstuvwxyzáàãâéèêíìîóòôõúùû")
maiusculas = list("ABCÇDEFGHIJKLMNOPQRSTUVWXYZÁÀÂÃÊÉÈÍÌÎÓÒÔÕÚÙÛ")
vitoria = False
chances = 5
carregamento = 0

if carregamento == 0:
    carregando()
    carregamento = carregamento + 1

while True:
    print("\n(1) Jogar")
    print("(2) Sair")
    comando = str(input("-> "))
    
    if comando == "1":
        limpa_Tela()
        desafiante = input("\nInsira o nome do desafiante: ")
        limpa_Tela()  
        competidor = input("\nInsira o nome do competidor: ")
        limpa_Tela()
        pSecreta = str(input("Informe a palavra Secreta: "))


        limpa_Tela()
        dicaA = input("Informe a Dica 1: ")
        limpa_Tela()
        dicaB = input("Informe a Dica 2: ")
        limpa_Tela()
        dicaC = input("Informe a Dica 3: ")
        limpa_Tela()

        dicas = [dicaA, dicaB, dicaC]
        dicasPedidas = 0

        tentativas = []

        def remove_acento(string: str) -> str:
            normalized = unicodedata.normalize('NFD', string)
            return normalized.encode('ascii', 'ignore').decode('utf8')
        
        while True:
            print("(1) Dica")
            print("(2) Sair\n")
            letras = str(input('Digite uma letra: ')) 
            limpa_Tela()
            try:
            
                if letras == "1":
                    if dicasPedidas < 3:
                        print(f"Dica {dicasPedidas+1}: {dicas[dicasPedidas]}\n")
                        dicasPedidas +=1
                    else:
                        print(f'Dica 1 = {dicaA}')
                        print(f'Dica 2 = {dicaB}')
                        print(f'Dica 3 = {dicaC}\n')
                        print("Suas dicas acabaram, hora do chute \n")
                    continue

                elif letras == "2":
                    print("Saindo do jogo atual...")
                    dormir()
                    limpa_Tela()
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
                    print(f'A palavra secreta não contem " {letras} " ')
            
                print(f'Você tem {chances} chances')
                print(f'Palavra secreta = {verificacao} ')
            
                desenha_forca(chances)
            except:
                print("Por favor digite uma letra")

            if verificacao == pSecreta or letras == pSecreta:

                limpa_Tela()
                ganhador = (f"A palavra era: {pSecreta} > Vencedor: Competidor {competidor}, Perdedor: Desafiante {desafiante}")
                print(f"PARABÉNS, {competidor} você venceu! \(^-^)/ ")
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
                print(f"Mais sorte na proxima {desafiante}")
                print()
                try:
                    print("\n")
                    arquivo = open('arquivo.txt','a')
                    arquivo.write(ganhador + "\n")
                    arquivo.close()

                    arquivo = open('arquivo.txt','r')
                    
                    print("Histórico de partidas:\n")
                    for linha in arquivo:
                        linha = linha.rstrip()
                        print (linha)
                    arquivo.close()
                    sonhador()
                   
                except:
                    arquivo = open('arquivo.txt','w')
                    arquivo.close()
                
                break
            
            desenho_final(chances)

            if chances == 0:
                ganhador = (f"A palavra era: {pSecreta} > Vencedor: Desafiante {desafiante}, Perdedor: Competidor {competidor}")
                print(f"Você foi enforcado {competidor} ¯\_('-')_/¯ ")
                print()
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
                print(f"Mais sorte da próxima vez {competidor} ('-')")
                print(f"Parabens {desafiante}")
                print()
                try:
                    print("\n")
                    arquivo = open('arquivo.txt','a')
                    arquivo.write(ganhador + "\n")
                    arquivo.close()

                    arquivo = open('arquivo.txt','r')
                    
                    print("Histórico de partidas:\n")
                    for linha in arquivo:
                        linha = linha.rstrip()                            
                        print (linha)
                    arquivo.close()
                    dormir()
                    
                except:
                    arquivo = open('arquivo.txt','w')                        
                    arquivo.close()
                    
                break
        
    elif(comando == "2"):
        print("Saindo...")
        dormir()
        limpa_Tela()
        break
    else:
        limpa_Tela()
        print("Escolha uma das opcões")
