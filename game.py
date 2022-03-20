import time
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #Se usara un tablero de 3x3
        self.current_winner = None #Checa quien gano

    def print_board(self):
        #Esto solo obtiene las filas
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
 
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 (nos dice a que numero corresponde cada cajita)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        #moves = []
        # for (i, spot) in enumerate(self.board):
        #     # ['x', 'x', 'o'] --> [(o, 'x'), (1, 'x'), (2, 'o')]
        #     if spot == ' ': 
        #           mvoes.append(i)
        #return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        #si el movimiento es valido, realiza la movida al tablero y returna True
        #Si el movimiento es invalido, returna False
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        #Definimos la manera de ganar en tictactoe
        #primero vamos a checar la fila
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        #checamos la columna
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #Checa las diagonales
        #Solo si el cuadro es un numero par (0, 2, 4, 6, 8)
        #Esos son los unicos movimientos posibles para ganar en diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True 
            diagonal2 = [self.board[i] for i in [2, 4, 6]] #diagonal de izq a derecha
            if all([spot == letter for spot in diagonal2]):
                return True

        # si todo esto Falla regresa False
        return False  

def play(game, x_player, o_player, print_game=True):
    #Regresa el ganador del juego o None si es empate
    if print_game:
        game.print_board_nums()

    letter = 'X' #letra de inicio
    #Sigue mientras el tablero tenga espacios
    #El juego nos avisara cuando tengamos un ganador y rompera el loop
    while game.empty_squares():
        #Hace el movimiento del jugador indicado
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        #Funcion para realizar una movida
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' realizaste un movimiento al cuadro {square}')
                game.print_board()
                print('') #linea vacia

            if game.current_winner:
                if print_game:
                    print(letter + ' Ganaaaaaste crack!')
                return letter

            #Despues de realizar una movida, se tienen que alternar las letras O - X
            letter = 'O' if letter == 'X' else 'X' #Cambia a los jugadores
            #if letter == 'X':
            #     letter = 'O'
            #else:
            #     letter = 'X'

        #Da un break para realizar la siguiente movida para que se mas facil de leer
        time.sleep(0.8)

    if print_game:
            print('Empate Cracks!')

if __name__  == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
