from grid import create_grid

"""
Cet fonction permet de rentrer dans la table le signe selectionner 
par le joueur et de verifier si son emplacement est vide.

elle reçoit en parametr


je fais rentrer au joueur les coordonnées de l emplacement et je le stock 
dans une variables element

"""
def verif_case(table, symbol):
        row     = int(input("rentrez la ligne : "))
        column  = int(input("rentrez la colonne : "))
        element = table[row][column]
        symbol1 = " "


        if element == " ":
                if symbol1 == "X":
                        symbol1 = "O"
                        print("saloperie ",symbol1)
                elif symbol1 == "O":
                        symbol1 = "X"
                        print("enfoire", symbol1)
                else:
                        symbol1 = "X"
                        print("lalalalala", symbol1)

                table[row][column] = symbol1
                # table.insert(element, symbol)
                print(table)
                print("Au joueur suivant de jouer.")
                print(symbol1)                       
                return verif_case(table, symbol)                                

        else:
                print("Veuillez choisir une autre case : ")
                return verif_case(table, symbol)

                

                        



        

                        
def toto(L):
        for x in L:
                for ele in x:
                        verif_case(create_grid)