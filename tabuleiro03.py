definicoes = [["", ""], ["Computador", ""]]                          #Definições do jogador

linhas = 7
colunas = 6

tabela = []
for i in range(linhas*colunas):                               #Criação da tabela com 42 elementos
    tabela.append(" ")

escolhaInicio = True
while (escolhaInicio):                                             #Menu principal, sem instrução
    opcao = str.lower(input("[1]Iniciar Jogo\n" +
                            "[2]Sair\n" +
                            "[3]Instruções\n\n" +
                            "Digite uma opção:\n> "))
    if (opcao == "1"):
        escolhaInicio = False
    elif ( opcao == "2"):
        exit()
    elif ( opcao == "3"):
        print("------- REGRAS DO JOGO ---------\n")
        
        print("- O Jogador deverá escolher uma das peças(X ou O).\n" +
              "- O jogador deverá tentar posicionar suas peças de modo que 4 delas fiquem unidas formando \n" +
              "uma linha, uma coluna ou uma diagonal.\n" +
              "- Sempre que o jogador conseguir posicionar três de suas peças unidas, ele ganhará 200 pontos.\n" +
              "         \n" +
              "- O jogo termina: \n" +
              "- quando um dos jogadores unir quatro de suas peças. Esse jogador será o vencedor.\n" +
              "- a qualquer momento, caso um dos jogadores deseje sair. Nesse caso, vencerá o jogador que \n" +
              "tiver acumulado mais pontos. Caso a pontuação seja igual, será decretado um empate.\n" +
              "- no caso de desejar sair, o jogador deverá digitar 'sair' no momento da sua jogada.\n" +
              "- quando não houver mais casas livres no tabuleiro. Nesse caso, vencerá o jogador que tiver \n" +
              "acumulado mais pontos. Caso a pontuação seja igual, será decretado um empate.\n")
        print("Agora que você sabe as intruções, escolha uma opções disponiveis.\n")
    else:
        print("Opção inválida.\n")
        

nomeJogador = str.capitalize(input("Insira o seu nome:\n> "))                       #Nome do jogador, player 1

player = ""
computador = ""
ListaSimbolos = ["X", "O"]
opcaoPeca = True

while (opcaoPeca):
    opcaoPeca = str.lower(input("[1]X\n" +
                                "[2]O\n" +
                                "Escolha uma peça:\n> "))
    if (opcaoPeca == "1"):
        player = ListaSimbolos[0]
        computador = ListaSimbolos[1]
        opcaoPeca = False
        
    elif ( opcaoPeca == "2"):
        player = ListaSimbolos[1]
        computador = ListaSimbolos[0]
        opcaoPeca = False


definicoes[0][0] = nomeJogador
definicoes[0][1] = player
definicoes[1][1] = computador

vitoria = False
turno = 0
pontuacaoPlayer = 0
pontuacaoComputador = 0

while ( vitoria == False):
    substituicao = False
    while ( substituicao == False):
        print("  0   1   2   3   4   5   6 \n"+
              "╔═══╦═══╦═══╦═══╦═══╦═══╦═══╗\n"+
              "║",tabela[0],"║",tabela[1],"║",tabela[2],"║",tabela[3],"║",tabela[4],"║",tabela[5],"║",tabela[6],"║\n"+
              "╠═══╬═══╬═══╬═══╬═══╬═══╬═══╣\n"+
              "║",tabela[7],"║",tabela[8],"║",tabela[9],"║",tabela[10],"║",tabela[11],"║",tabela[12],"║",tabela[13],"║\n"+
              "╠═══╬═══╬═══╬═══╬═══╬═══╬═══╣\n"+
              "║",tabela[14],"║",tabela[15],"║",tabela[16],"║",tabela[17],"║",tabela[18],"║",tabela[19],"║",tabela[20],"║\n"+
              "╠═══╬═══╬═══╬═══╬═══╬═══╬═══╣\n"+
              "║",tabela[21],"║",tabela[22],"║",tabela[23],"║",tabela[24],"║",tabela[25],"║",tabela[26],"║",tabela[27],"║\n"+
              "╠═══╬═══╬═══╬═══╬═══╬═══╬═══╣\n"+
              "║",tabela[28],"║",tabela[29],"║",tabela[30],"║",tabela[31],"║",tabela[32],"║",tabela[33],"║",tabela[34],"║\n"+
              "╠═══╬═══╬═══╬═══╬═══╬═══╬═══╣\n"+
              "║",tabela[35],"║",tabela[36],"║",tabela[37],"║",tabela[38],"║",tabela[39],"║",tabela[40],"║",tabela[41],"║\n"+
              "╚═══╩═══╩═══╩═══╩═══╩═══╩═══╝\n")
        if (turno == 0):
            jogada = input("Faça sua jogada:\n> ")
            pecaJogada = ( definicoes[0][1])
            turno = 1
        elif ( turno == 1 ):
            jogada = input("Faça sua jogada:\n> ")
            pecaJogada = ( definicoes[1][1])
            turno = 0

        escolhaColuna = True
        listaPossiveisEscolhas = ["0", "1", "2", "3", "4", "5", "6"]
        limiteMinimoFinal = 35
        salto = 7
        contX  = 1
        
        while(escolhaColuna):
            if(jogada in listaPossiveisEscolhas):
                limiteColuna =  limiteMinimoFinal+int(jogada)+1
                escolhaColuna = False
            elif(str.lower(jogada) == "sair"):
                print("Que pena...")
                exit()
            else:
                jogada = input("Valor inválido!. insira um valor de acordo com a tabela:\n> ")
            
        
        
        for i in range(int(jogada), limiteColuna, salto):
            if ((tabela[i] == " ") and (i + salto > limiteColuna)):
                tabela[i] = pecaJogada
                substituicao = True
            
                
            elif ((tabela[i] == " ") and (tabela[i+salto] != " ")):
                tabela[i] = pecaJogada
                substituicao = True
                    
                
      
            if(substituicao == False):
                print("Coluna já está preechida, tente outra.\n")

            for i  in range(len(tabela), 42, 1):
                if ((tabela[i] == "X") and (tabela[i + 1])):
                    contX += 1

            if (contX == 4):
                print("O jogador X ganhou.")
                substituicao = True
                        

            
            



            

