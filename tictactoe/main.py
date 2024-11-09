from joueurs import initialiser_joueurs
from joueurs import choisir_symboles
from grid import create_grid
from placement import verif_case
from placement import toto
from winner import horizontal
from winner import verticale
from winner import diagonale
from winner import match_nul

symbol = input("Veuillez rentrer le signe : ")
L  = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
        ]

def main():
    
    initialiser_joueurs(symbol)
    verif_case(L, symbol)
    horizontal(table)
    verticale(table)
    diagonale(table)
    match_nul(horizontal, verticale, diagonale)
    create_grid(L)

