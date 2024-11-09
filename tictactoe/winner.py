
from placement import toto
#verification des cases horizontales
def horizontal(board):
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X" or \
board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        return true, print("victoire0")
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X" or \
board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        return true, print("victoire1")

    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X" or \
board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        return true, print("victoire2")
    
    else:
        return False

#verification des cases verticales
def verticale(board):
    if board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X" or \
board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        return true, print("victoire3")

    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X" or \
board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        return true, print("victoire4")

    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X" or \
player[0][2] == "O" and player[1][2] == "O" and player[2][2] == "O":
        return true, print("victoire5")
    
    else:
        return False

#verification des cases diagonales
def diagonale(board):
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X" or \
board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        return true, print("victoire6")

    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X" or \
board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        return true, print("victoire7")

    else:
        return False

#verification match nul
def match_nul(horizontal, verticale, diagonale):
    if horizontal(horizontal) == False and verticale(verticale) == False and \
diagonale(diagonale) == False:
        return print("match nul")
    else:
        print("nul")


