from jogo_da_velha import criarBoard, fazMovimento, getImputValido, \
                          printBoard, verifiGanhador, verificaMovimento 
                          
jogador = 0 # jogador 1
board = criarBoard()                    
ganhador = verifiGanhador(board)
while(not ganhador):
    printBoard(board)
    i = getImputValido("Digite a linha: ")
    j = getImputValido("Digite a coluna: ")

if(verificaMovimento(board, i, j)):
    fazMovimento(board, i, j, jogador)
    jogador = (jogador + 1)%2
else:
    print("A posicao informada ja esta ocupada")
    
ganhador = verifiGanhador(board)

print("==================")
print(board)
print("Ganhador = ", ganhador)
print("===================")