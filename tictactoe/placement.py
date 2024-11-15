from grid import create_grid
from winner import *

def symbol(symbol):
        symbol = symbol[0]
        return symbol


def verif_case(table, symbol):
        row     = int(input("rentrez la ligne : "))
        column  = int(input("rentrez la colonne : "))
        element = table[row][column]

        if element == " ":
                table[row][column] = symbol
                # table.insert(element, symbol)
                print("Au joueur suivant de jouer.")
                print(symbol)

                if symbol == "X":
                        symbol = "O"
                        print("hello ",symbol)
                elif symbol == "O":
                        symbol = "X"
                        print("world", symbol)
                return create_grid(table), verif_case(table, symbol)                                

        else:
                print("Veuillez choisir une autre case : ")
                return verif_case(table, symbol)        

                        
