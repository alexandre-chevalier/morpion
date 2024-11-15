from grid import create_grid

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
                print(table)
                print("Au joueur suivant de jouer.")
                print(symbol)

                if symbol == "X":
                        symbol = "O"
                        print("hello ",symbol)
                elif symbol == "O":
                        symbol = "X"
                        print("world", symbol)

                return verif_case(table, symbol)                                

        else:
                print("Veuillez choisir une autre case : ")
                return verif_case(table, symbol)        

                        
def toto(L):
        for x in L:
                for ele in x:
                        verif_case(create_grid)