definicoes = [["", ""], ["Computador", ""]]                          #Definições do jogador

linhas = 7
colunas = 6

  # ----------- Criação da tabela ------------
tabela = []
for i in range(linhas*colunas):                               #Criação da tabela com 42 elementos
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

  # ----------- Tabela completa e checagem de vitórias ------------

vitoria = False
turno = 0
pontuacaoPlayer = 0
pontuacaoComputador = 0
contX = 0
contO = 0
tratamentoErro = 1

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

  # ------------ Mudança de turnos + escolha das jogadas ------------
        if (turno == 0):
            if (tratamentoErro == 1):
                turno = 1
                pecaJogada = ( definicoes[0][1])
            else:
                turno = 0
                pecaJogada = ( definicoes[1][1])
            jogada = input("Faça sua jogada  %s :\n> "%(pecaJogada))
            
        elif (turno == 1):
            if( tratamentoErro == 1):
                turno = 0
                pecaJogada = ( definicoes[1][1])
            else:
                turno = 1
                pecaJogada = ( definicoes[0][1])
                

            jogada = input("Faça sua jogada %s :\n> "%(pecaJogada))
                
                
                
        escolhaColuna = True
        listaPossiveisEscolhas = ["0", "1", "2", "3", "4", "5", "6"]
        limiteMinimoFinal = 35
        salto = 7
        
        while(escolhaColuna):
            if (jogada in listaPossiveisEscolhas):
                limiteColuna =  limiteMinimoFinal+int(jogada)+1
                escolhaColuna = False
            elif (str.lower(jogada) == "sair"):
                print("Que pena...")
                exit()
            else:
                jogada = input("Valor inválido!. insira um valor de acordo com a tabela:\n> ")

  # ------------ Verificação de espaços preenchidos e vazios para adicionar as peças ------------        
        
        for i in range(int(jogada), limiteColuna, salto):
            if ((tabela[i] == " ") and (i + salto > limiteColuna)):
                tabela[i] = pecaJogada
                tratamentoErro = 1
                substituicao = True
            
                
            elif ((tabela[i] == " ") and (tabela[i + salto] != " ")):
                tabela[i] = pecaJogada
                tratamentoErro = 1
                substituicao = True
                    
                
      
        if(substituicao == False):
            print("Coluna já está preechida, tente outra.\n")
            tratamentoErro = 0
            
    #------ Checagem em horizontal -----------

        for i in range(len(tabela)):
            if ((i + salto) > limiteColuna):
                if (tabela[i] == "X" and tabela[i - 1] == "X" and tabela[i - 2] == "X" and tabela[i - 3] == "X"):
                    contX += 4
            else:
                if (tabela[i] == "X" and tabela[i + 1] == "X" and tabela[i +2] == "X" and tabela[i + 3] == "X"):
                    contX += 4

                        
            if ((i + salto) > limiteColuna):
                if (tabela[i] == "O" and tabela[i - 1] == "O" and tabela[i - 2] == "O" and tabela[i - 3] == "O"):
                    contO += 4
            else:
                if (tabela[i] == "O" and tabela[i + 1] == "O" and tabela[i + 2] == "O" and tabela[i + 3] == "O"):
                    contO += 4


   #------ Checagem em vertical --------------

        for i in range(len(listaPossiveisEscolhas)):

            if (tabela[i] == "X" and tabela[i + 7] == "X" and tabela[i + 14] == "X" and tabela[i + 21] == "X" or
                (tabela[i + 7] == "X" and tabela[i + 14] == "X" and tabela[i + 21] == "X" and tabela[i + 28] == "X" or
                (tabela[i + 14] == "X" and tabela[i + 21] == "X" and tabela[i + 28] == "X" and tabela[i + 35] == "X"))):
                contX += 4


            if (tabela[i] == "O" and tabela[i + 7] == "O" and tabela[i + 14] == "O" and tabela[i + 21] == "O" or
                (tabela[i + 7] == "O" and tabela[i + 14] == "O" and tabela[i + 21] == "O" and tabela[i + 28] == "O" or
                (tabela[i + 14] == "O" and tabela[i + 21] == "O" and tabela[i + 28] == "O" and tabela[i + 35] == "O"))):
                contO += 4

                    
   #------ Checagem em diagonal \ / --------------

        for i in range(len(listaPossiveisEscolhas)):
            for j in range(i, len(tabela), 7 + i):
                if ((j + (28 - i ) + 3  ) <= 41 ):
                    if ( tabela[j] == "X" and tabela[j + ( 7 - i ) + 1] == "X" and tabela[j + ( 14 - i) + 2] == "X" and tabela[j + (21 - i ) + 3] == "X" or
                         tabela[j + ( 7 - i )] == "X" and tabela[j + ( 14 - i ) + 1] == "X" and tabela[j + ( 21 - i ) + 2] == "X" and tabela[j + ( 28 - i ) + 3] == "X"):
                        contX += 4
                else:
                    if ( tabela[j] == "X" and tabela[j + 7 - (7 - i )] == "X" and tabela[j + 14 - (7 + 1 - i )] == "X" and tabela[j + 21 - (7 + 2- i )] == "X" or
                         tabela[j + 7 - (7 - i)] == "X" and tabela[j + 14 - (7 + 1 - i )] == "X" and tabela[j + 21 - (7 + 2 - i )] == "X" and tabela[j + 28 - (7 + 3 - i )] == "X"):
                        contX += 4



##                if ( tabela[j] == "O" and tabela[j + ( 7 - i ) + 1] == "O" and tabela[j + ( 14 - i) + 2] == "O" and tabela[j + (21 - i ) + 3] == "O" or
##                     tabela[j + ( 7 - i ) + 1] == "O" and tabela[j + ( 14 - i) + 2] == "O" and tabela[j + (21 - i ) + 3] == "O" and tabela[j + (28  - i) + 4] == "O"):
##                    contO += 4


                    





  # ----------- Checagem de vitoria final -----------                  
        if (contX >= 4):
            condicaoVitoria = "O jogador -- %s -- ganhou !! \n"%(definicoes[0][0])
            vitoria = True
        elif (contO >= 4):
            condicaoVitoria = "O jogador -- %s -- ganhou !! \n"%(definicoes[1][0])
            vitoria = True

  # ----------- Mostrar ao usuário quem ganhou -----------

if ( vitoria ):
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

            print(condicaoVitoria)
    
            



            

