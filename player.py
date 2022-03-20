import math
import random

class Player:
    def __init__(self, letter):
        #letter es x or o
        self.letter = letter

    #Queremos que los jugadores puedan elegir su jugada
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            #vamos a checar si es una movida valida
            #si es un integro, si no, la movida no es valida
            #Si el cuadro esta ocupado en el tablero, tambien decimos que es invalido
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True 
            except ValueError:
                print('Cuadro no valido, prueba de nuevo crack')

        return val
