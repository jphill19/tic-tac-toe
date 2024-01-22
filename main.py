from board import Board
from art import game_art
from player import Player
from colorama import Fore, Style


player1 = Player("X", 1)
player2= Player("O", 2)

board = Board(player1, player2)

1

def ensure_unique_position(player:Player):
    '''This function will ensure that the player chooses a unique position'''
    while True:
        player_input = player.player_input()
        validate = board.update_board(position=int(player_input), player=player.symbol)
        if validate == True:
            return

def checking_if_game_is_over():
    '''This function will check if the game is over'''
    game_is_over = board.check_winner()
    if game_is_over== True:
        board.print_board()
        print(f"{player1.color}Player 1 won!{Style.RESET_ALL}" if player1.symbol == board.winner else f"{player2.color}Player 2 won!{Style.RESET_ALL}")
        if player1.symbol == board.winner:
            player1.win_record += 1
        else:
            player2.win_record += 1
        return True
    elif board.if_board_is_full() == True:
        board.print_board()
        print("It's a tie!")
        return True
    else:
        return False

def play_game():
    print(game_art)
    while True:
        board.print_board()
        ensure_unique_position(player1)
        if checking_if_game_is_over() == True:
            break
        board.print_board()
        ensure_unique_position(player2) 
        if checking_if_game_is_over() == True:
            break       

def play_again():
    '''This function will ask the player if they want to play again'''
    while True:
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y":
            board.reset_board(player1.win_record, player2.win_record)
            play_game()
        elif play_again.lower() == "n":
            print("Thanks for playing!")
            break
        else:
            print("Please enter y or n")

def main():
    play_game()
    play_again()

if __name__ == "__main__":
    main()