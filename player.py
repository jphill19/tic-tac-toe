from colorama import Fore, Style

class Player:
    '''This class will create a player with a symbol and a player number'''
    def __init__(self, symbol:str,player_number:int):
        self.symbol = symbol
        self.player_number = player_number
        # This will get set the color of the player, which will be used to identify the player's move on the board and when their input is needed.
        self.color = Fore.RED if symbol == "X" else Fore.BLUE
        self.win_record = 0

    

    def player_input(self):
        '''This method will ask the player to choose a position and return the position'''
        while True:
            player_input = input(self.color + f"\nPlayer {self.player_number}, choose a position: " + Style.RESET_ALL)
            if player_input.isdigit():
                if int(player_input) in range(1, 10):
                    return int(player_input)
                else:
                    print(self.color + "Please enter a number between 1 and 9" + Style.RESET_ALL)
            else:
                print(self.color +"Please enter a number between 1 and 9" + Style.RESET_ALL)

    def __str__(self) -> str:
        return self.symbol  # This will return the symbol of the player