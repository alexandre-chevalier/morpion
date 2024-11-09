from grid import create_grid

"""
Cet fonction permet de rentrer dans la table le signe selectionner 
par le joueur et de verifier si son emplacement est vide.

elle reçoit en parametr


je fais rentrer au joueur les coordonnées de l emplacement et je le stock 
dans une variables element

"""
def verif_case(table, symbol, L):
        row     = int(input("rentrez la ligne : "))
        column  = int(input("rentrez la colonne : "))
        element = table[row][column]

        if symbol == "X" or symbol == "x" or symbol == "O" or symbol == "o":
                if element == "":
                        table[row][column] = symbol
                        # table.insert(element, symbol)
                        print(table)
                        print("Au joueur suivant de jouer.")
                        return table
                else:
                        print("Veuillez choisir une autre case : ")
                        return verif_case(table, symbol)
        else:
                print("Veuillez choisir entre l")

                        
def toto(L):
        for x in L:
                for ele in x:
                        verif_case(create_grid, symbol)

#vérifier le merge
