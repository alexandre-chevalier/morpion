def initialiser_joueurs(player1, player2):    
    print(f"player1 est {player1}.")
    print(f"player2 est {player2}.")
    return player1, player2

def choisir_symboles():
    while True:
        symbol1 = input("player1, choisissez votre symbole (X ou O) : ").upper()
        symbol2 = " "
        if symbol1 == "X":
            symbol2="O"
            print(f"player1 est {symbol1}.")
            print(f"player2 est {symbol2}.")
            return symbol1, symbol2

        elif symbol1 == "O":
            symbol2 = "X"
            print(f"player1 est {symbol1}.")
            print(f"player2 est {symbol2}.")
            return symbol1, symbol2