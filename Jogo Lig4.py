from random import randint

#criação da tabela com 42 espaços

linhas = 6
colunas = 7
tabela = []

for i in range(linhas*colunas):
    tabela.append(" ")

  # ------------ MENU PRINCIPAL ------------

escolhaInicio = True
while (escolhaInicio):                                             
    opcao = str.lower(input("[1]Iniciar Jogo\n" +
                            "[2]Instruções\n" +
                            "[3]Sair\n\n" +
                            "Digite uma opção:\n> "))
    if (opcao == "1"):
        escolhaInicio = False
    elif ( opcao == "3"):
        exit()
    elif ( opcao == "2"):
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
        
  # ------------ Definições de cada jogador ( incluindo o pc como um deles ) ------------
  
nomeJogador = str.capitalize(input("Insira o seu nome:\n> "))                       #Nome do jogador, player 1

player = ""
computador = ""
ListaSimbolos = ["X", "O"]
opcaoPeca = True
escolhaJogar = True
        
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
    else:
        print("Opção inválida!\n")

definicoes = [["", ""], ["Computador", ""]]
definicoes[0][0] = nomeJogador
definicoes[0][1] = player
definicoes[1][1] = computador

  # ----------- Tabela completa e checagem de vitórias ------------


vitoria = False
pontuacaoPlayer = 0
pontuacaoComputador = 0
cont = 0
turno = 0
tratamentoErro = 1
checagemPontuacao = 0

while (vitoria == False):
    substituicao = False
    pontosVitoria = 0
    while (substituicao == False):
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
            jogada = input("Vez de %s :\n> "%(definicoes[0][0]))
        elif (turno == 1):
            jogada = randint(int(listaPossiveisEscolhas[0]) , int(listaPossiveisEscolhas[6]))
            print("Vez de %s .\n> "%(definicoes[1][0]))
            jogada = str(jogada)
              
        escolhaColuna = True
        listaPossiveisEscolhas = ["0", "1", "2", "3", "4", "5", "6"]
        limiteMinimoFinal = 36
        salto = 7
        
        while(escolhaColuna):
            if (jogada in listaPossiveisEscolhas):
                limiteColuna =  limiteMinimoFinal+int(jogada)
                escolhaColuna = False
                
            elif (str.lower(jogada) == "sair"):
                print("Que pena...")
                if ( pontuacaoPlayer > pontuacaoComputador):
                    vitoriaCond = definicoes[0][0]
                elif ( pontuacaoPlayer == pontuacaoComputador):
                    print("Ambos o jogadores empataram !! ")

                else:
                    vitoriaCond = definicoes[1][0]
                print("O jogador %s ganhou por ter feito mais pontos."%(vitoriaCond))
                exit()
                
            else:
                jogada = input("Valor inválido!. insira um valor de acordo com a tabela:\n> ")

    # ------------ Verificação de espaços preenchidos e vazios para adicionar as peças ------------        
        
        for i in range(int(jogada), limiteColuna, salto):
            if ((tabela[i] == " ") and (i + salto > limiteColuna)):
                tabela[i] = definicoes[turno][1]
                substituicao = True
                tratamentoErro = 1
                
            elif ((tabela[i] == " ") and (tabela[i + salto] != " ")):
                tabela[i] = definicoes[turno][1]
                substituicao = True
                tratamentoErro = 1
                
        if(substituicao == False):
            print("Coluna já está preechida, tente outra.\n")
            tratamentoErro = 0

    #------ Checagem em horizontal -----------

        limiteMinimoFinal = 36
        colunas = 7
        cont = 0
        for i in range(0, limiteMinimoFinal ,7):
            for u in range(i, colunas, 1):
                if(tabela[u] == definicoes[turno][1]):
                    cont += 1
                else:
                    cont = 0
                    
                if ( cont == 3):
                    if ( turno == 1):
                        pontuacaoComputador += 200
                    else:
                        pontuacaoPlayer += 200
                elif (cont >= 4):
                    vitoria = True

            colunas += 7

    #------ Checagem em vertical --------------
        limiteMinimoFinal = 36
        colunas = 7
        cont = 0
        for i in range(0, colunas, 1):
            for u in range(i , limiteMinimoFinal, 7):
                if(tabela[u] == definicoes[turno][1]):
                    cont += 1
                else:
                    cont = 0

                if ( cont == 3):
                    if ( turno == 1):
                        pontuacaoComputador += 200
                    else:
                        pontuacaoPlayer += 200
                elif(cont >= 4):
                    vitoria = True
                    
            limiteMinimoFinal += 1
           
                    
    #------ Mudança de turno e vitória --------------   
        if (vitoria == True):
            print("Pontos do  jogador %s : %d"%(definicoes[0][0], pontuacaoPlayer), "    Pontos do computador: %d"%(pontuacaoComputador),"\n")  
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

            print("O jogador %s ganhou !! \n"%(definicoes[turno][0]))
            
                        
        if (turno == 0):
            if (tratamentoErro == 1):
                turno = 1
            else:
                turno = 0
            
        else:
            if( tratamentoErro == 1):
                turno = 0
            else:
                turno = 1
                
                
