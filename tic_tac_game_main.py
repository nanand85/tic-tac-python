# Data Processing
# Import libraries
import numpy as np
#import sys

game_board = np.array([['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']])

#check whether the game is over or not
def check_game_over (player_name, ch):
    #check rows
    for row in range(0, 3):
        for col in range(0, 3):
            if (game_board[row][col] != ch):
                break;
            elif (col == 2):
                print(player_name +": YOU HAVE WON THE GAME!!!")
                return(True)
                
    #check columns
    for col in range(0, 3):
        for row in range(0, 3):
            if (game_board[row][col] != ch):
                break;
            elif (row == 2):
                print(player_name +": YOU WON!!!")
                return(True)
                
    #check diagnonal            
    if (game_board[0][0] == game_board[1][1] == game_board[2][2] == ch):
        print(player_name +": YOU WON!!!")
        return(True)           
    elif (game_board[2][0] == game_board[1][1] == game_board[0][2] == ch):
        print(player_name +": YOU WON!!!")
        return(True)
           
    return(False)

#Get input position from specififed player       
def get_player_input (player_name, ch):
    while (1):
        inval = int(input(player_name + ", " + "enter position (0 - 8)"))
        row = inval // 3
        col = inval % 3
        if (game_board[row][col] != str(inval)):
            print("Invalid Input: re-enter")
        else:
            game_board[row][col] = ch
            break
            
               
#Play the game
def tic_tac_play(player1, player2):
    i = 0
    print(np.matrix(game_board))
    while(i < 9):
        #process the input from first player
        get_player_input(player1, 'X')
        print(np.matrix(game_board))        
        if (check_game_over(player1, 'X') == True):
            return;
        else:
            i+=1
            if (i >= 9):
                break
        #process the input from second player
        get_player_input(player2, 'O')
        print(np.matrix(game_board))        
        if (check_game_over(player2, 'O') == True):
            return;
        else:
            i+=1
    print("!!!  MATCH DRAW  !!!")    
        
#main function
def main():
    user1 = input("Enter the name of player1:")
    user2 = input("Enter the name of plater2:")
    tic_tac_play(user1.upper(), user2.upper())
    
if __name__ == '__main__':
    main()