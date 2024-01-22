from player import Player
from colorama import Fore, Style

class Board():
    def __init__(self, player1:Player, player2:Player):
        self.winner = None
        # It will create 3 slots for the outer list (y) and 3 slots for the inner list (x)
        self.positions = [[str(3 * y + x + 1) for x in range(3)] for y in range(3)]
        self.board = [['-' for x in range(3)] for y in range(3)]
        # This will get the color of the player, which is an attribute of the Player class
        self.color_player1 = player1.color
        self.color_player2 = player2.color
        self.player_1_wins = player1.win_record
        self.player_2_wins = player2.win_record
     

    def color_coding(self,row):
        if row[0] == "X":
            return self.color_player1
        elif row[0] == "O":
            return self.color_player2
        else:
            return Fore.WHITE
        


    def color_coding(self, row):
        if row[0] == "X":
            return self.color_player1
        elif row[0] == "O":
            return self.color_player2
        else:
            return Fore.WHITE

    def print_board(self):
        count=0
        print("\n-----------------------------------------------------------------------------------\n")
        print(self.color_player1 + "\tPlayer 1" + Style.RESET_ALL + " is " + self.color_player1 + "X" + Style.RESET_ALL + self.color_player1 + "\t\tPlayer 1" + Style.RESET_ALL + " win count:" + self.color_player1 + f" {self.player_1_wins}" + Style.RESET_ALL)
        print(self.color_player2 + "\tPlayer 2" + Style.RESET_ALL + " is " + self.color_player2 + "O" + Style.RESET_ALL + self.color_player2 + "\t\tPlayer 2" + Style.RESET_ALL + " win count:" + self.color_player2 + f" {self.player_2_wins}" + Style.RESET_ALL)
        print(Style.BRIGHT+"\n\tTic-Tac-Toe\t\tBoard Positions\n"+ Style.RESET_ALL)
        for row in self.board:
            # This will print the board with the player's move, and the available board positions. Count will be used to get the index of the position in the list. 
            print(f"\t {self.color_coding(row[0])}{row[0]}{Style.RESET_ALL} | {self.color_coding(row[1])}{row[1]}{Style.RESET_ALL} | {self.color_coding(row[2])}{row[2]}{Style.RESET_ALL}\t\t {self.positions[count][0]} | {self.positions[count][1]} | {self.positions[count][2]}")
            count+=1
            if count < 3:
                # This will print the line that separates the rows. The reason why we check if count is <3 is because we only want to print the line after the first and second row. We don't want to print the line after the third row.
                print("\t-----------\t\t-----------")

    def update_board(self, position:int ,player:Player ):
        '''This method will update the board with the player's move'''
        # The position is the number that the player will choose, and the player is either X or O. 
        #The position will be converted to an integer by the int() function and then subtracted by 1 to get the index of the position in the list. The position will be divided by 3 to get the row and the remainder will be the column. The player will be placed in the position of the board.
        if self.board[(position - 1) // 3][(position - 1) % 3] == "X" or self.board[(position - 1) // 3][(position - 1) % 3] == "O":
            print("This position is already taken")
            return False
        else:
            # The position is the number that the player will choose, and the player is either X or O.
            # The position will be converted to an integer by the int() function and then subtracted by 1 to get the index of the position in the list. The position will be divided by 3 to get the row and the remainder will be the column. The player will be placed in the position of the board.
            self.board[(position - 1) // 3][(position - 1) % 3] = player
            self.positions[(position - 1) // 3][(position - 1) % 3] = "-"
            return True

    def check_winner(self):
        '''This method will check if there is a winner'''
        # This will check if there is a winner in the rows
        for row in self.board:
            if row[0] == row[1] == row[2] != "-":
                if row[0] == "X":
                    self.winner = "X"
                else:
                    self.winner = "O"
                return True
        # This will check if there is a winner in the columns
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "-":
                if self.board[0][i] == "X":
                    self.winner = "X"
                else:
                    self.winner = "O"
                return True
        # This will check if there is a winner in the diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "-":
            if self.board[0][0] == "X":
                self.winner = "X"
            else:
                self.winner = "O"
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "-":
            if self.board[0][2] == "X":
                self.winner = "X"
            else:
                self.winner = "O"
            return (True, self.winner)
        return False
    
    def if_board_is_full(self):
        '''This method will check if the board is full'''
        # This will check if the board is full
        for row in self.board:
            for column in row:
                if column == "-":
                    return False
        return True
    

    def reset_board(self, player1_win_record, player2_win_record):
        '''This method will reset the board'''
        # This will reset the board
        self.board = [['-' for x in range(3)] for y in range(3)]
        self.positions = [[str(3 * y + x + 1) for x in range(3)] for y in range(3)]
        self.winner = None
        self.player_1_wins = player1_win_record
        self.player_2_wins = player2_win_record