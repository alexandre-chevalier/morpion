from joueurs import *
from grid import *
from placement import *
from winner import *

symbol = input("Veuillez rentrer le signe : ")
L  = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
        ]

def main():
    initialiser_joueurs()
    verif_case(L, symbol)
    create_grid(L)
    horizontal(L)
    verticale(L)
    diagonale(L)
    match_nul(horizontal, verticale, diagonale)

main()