from joueurs import *
from grid import *
from placement import *
from winner import *



L  = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
        ]

player1 =  input("Entrez le nom de player1 : ")
player2 = input("Entrez le nom de player2 : ")

def main():
    initialiser_joueurs(player1,player2)
    #choisir_symboles()
   
    verif_case(L, symbol(choisir_symboles()))    
    horizontal(L)
    verticale(L)
    diagonale(L)
    match_nul(horizontal(L), verticale(L), diagonale(L))

main()