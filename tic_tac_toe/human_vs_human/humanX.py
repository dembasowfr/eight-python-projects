from player import Player

#Human player that inherits the player class
class HumanX(Player):
    def __init__(self, letter):
        super().__init__(letter)
    

    def get_move(self, board):

        valid_spot = False

        value = None

        while not valid_spot:
            spot = input(self.letter + '\'s turn. Pick a move(0-8): ')
            try:
                value = int(spot)
                if value not in board.available_spots():
                    raise ValueError
                valid_spot = True
            except ValueError:
                print('Invalid spot! Try again.')
        
        return value

