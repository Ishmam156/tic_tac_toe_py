# Tic Tac Toe Game v2

# Import sleep
from time import sleep

# Global Player Stats

pl_1_wins = 0
pl_2_wins = 0

# Main game loop
while True:

    # Define Tictactoe and all main functions
    g_m = ["", "", "", "", "", "", "", "", "", ""]
    
    def tictactoe():
        print()
        print(f" 		 |	 	 |	 	 ")
        print(f" 	{g_m[7]}	 |	 {g_m[8]}	 |	 {g_m[9]}	 ")
        print(f" 		 |	 	 |	 	 ")
        print("---------------------------------------------------")
        print(f" 		 |	 	 |	 	 ")
        print(f" 	{g_m[4]}	 |	 {g_m[5]}	 |	 {g_m[6]}	 ")
        print(f" 		 |	 	 |	 	 ")
        print("---------------------------------------------------")
        print(f" 		 |	 	 |	 	 ")
        print(f" 	{g_m[1]}	 |	 {g_m[2]}	 |	 {g_m[3]}	 ")
        print(f" 		 |	 	 |	 	 ")
        print()

    # Define player 1 moves
    def p1_play(move_1):
        # Check for integer only use
        while True:
            try:
                move_1 = int(move_1)
                break
            except ValueError:
                move_1 = input("Input can only be numbers between (1 - 9):\n")

        # Check for within range integer use        
        while move_1 not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("Input can only be numbers between (1 - 9):")
            move_1 = int(
                input("Player 1: Which move do you want to make? (1 - 9):\n"))

        # Check whether slot is already occupied    
        while g_m[move_1] != '':
            print("That is already occupied!")
            print()
            move_1 = int(
                input("Player 1: Which move do you want to make? (1 - 9):\n"))
        
        # Accept input with all check completed    
        g_m[move_1] = player_1

    # Define player 2 moves
    def p2_play(move_2):
        # Check for integer only use
        while True:
            try:
                move_2 = int(move_2)
                break
            except ValueError:
                move_2 = input("Input can only be numbers between (1 - 9):\n")

        # Check for within range integer use          
        while move_2 not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("Input can only be numbers between (1 - 9):")
            move_2 = int(
                input("Player 2: Which move do you want to make? (1 - 9):\n"))

        # Check whether slot is already occupied      
        while g_m[move_2] != '':
            print("That is already occupied!")
            print()
            move_2 = int(
                input("Player 2: Which move do you want to make? (1 - 9):\n"))
        
        # Accept input with all check completed    
        g_m[move_2] = player_2

    # Define win check for all possible variation, list reference can be checked with board above
    def win_check():

        check_list = [g_m[1], g_m[2], g_m[3]]
        if check_list.count('X') == 3:
            return 'X'
        if check_list.count('O') == 3:
            return 'O'

        check_list = [g_m[4], g_m[5], g_m[6]]
        if check_list.count('X') == 3:
            return 'X'
        if check_list.count('O') == 3:
            return 'O'

        check_list = [g_m[7], g_m[8], g_m[9]]
        if check_list.count('X') == 3:
            return 'X'
        if check_list.count('O') == 3:
            return 'O'

        check_list = [g_m[1], g_m[4], g_m[7]]
        if check_list.count('X') == 3:
            return 'X'
        if check_list.count('O') == 3:
            return 'O'

        check_list = [g_m[2], g_m[5], g_m[8]]
        if check_list.count('X') == 3:
            return 'X'
        if check_list.count('O') == 3:
            return 'O'

        check_list = [g_m[3], g_m[6], g_m[9]]
        if check_list.count('X') == 3:
            return 'X'
        if check_list.count('O') == 3:
            return 'O'

        check_list = [g_m[1], g_m[5], g_m[9]]
        if check_list.count('X') == 3:
            return 'X'
        if check_list.count('O') == 3:
            return 'O'

        check_list = [g_m[3], g_m[5], g_m[7]]
        if check_list.count('X') == 3:
            return 'X'
        if check_list.count('O') == 3:
            return 'O'

    # Define winner check
    def winner_check():
        global pl_1_wins
        global pl_2_wins
        if check == 'X':
            if player_1 == 'X':
                print("Player 1 Wins!")
                pl_1_wins += 1
                return True
            else:
                print("Player 2 Wins!")
                pl_2_wins += 1
                return True
        elif check == 'O':
            if player_1 == 'O':
                print("Player 1 Wins!")
                pl_1_wins += 1
                return True
            else:
                print("Player 2 Wins!")
                pl_2_wins += 1
                return True

    # Game starter            
    while True:
        print()
        print("Welcome to the wonderful game of Tic Tac Toe!")
        print()
        player_1 = input("Player 1: Which icon do you want to play with? ( X / O ):\n")
        print()

        # Icon check
        while player_1 != 'X' and player_1 != 'O':
            print("You can only chose between the following: X / O")
            player_1 = input(
                "Which icon do you want to play with? ( X / O ):\n")

        # Icon assignment
        if player_1 == 'X':
            player_2 = 'O'
        else:
            player_2 = 'X'

        # Player 2 informed about icon    
        print()
        print(f"Great! Player 2 will be: {player_2}")    

        # Game demo
        print()
        print("Let us begin the game!")
        print()
        print("Current win tally!")
        sleep(.5)
        print()
        print(f"Player 1: {pl_1_wins}")
        print(f"Player 2: {pl_2_wins}")
        print()
        sleep(1)
        print("The game format is as below:")
        print()

        # Game rules
        print(" 7 | 8 | 9 ")
        print("-----------")
        print(" 4 | 5 | 6 ")
        print("-----------")
        print(" 1 | 2 | 3 ")

        sleep(2)
        print()

        # Game start
        print("Startin with a blank board!")

        tictactoe()

        move_count = 1

        # Game loop start

        while True:
            print(f"Count: {move_count}")
            move_1 = input("Player 1: Which move do you want to make? (1 - 9):\n") 
            p1_play(move_1)
            move_count += 1
            tictactoe()
            print()
            check = win_check()
            winner = winner_check()
            if winner:
                break
            if move_count == 10:
                break    
            move_count += 1
            print(f"Count: {move_count}")
            move_2 = input("Player 2: Which move do you want to make? (1 - 9):\n")
            p2_play(move_2)
            tictactoe()
            print()
            check = win_check()
            winner = winner_check()
            if winner:
                break

        # Break out of loop               
        if winner:
            break

        # Break if tie    
        if move_count == 10:    
            print()
            print("It's a tie!")
            break                                    

    # Game restart prompt
    retry = input("Do you want to play again? (input n to exit):\n")
    if retry == 'n':
        print()
        print("Final win tally!")
        sleep(.5)
        print()
        print(f"Player 1: {pl_1_wins}")
        print(f"Player 2: {pl_2_wins}")
        print()
        if pl_1_wins > pl_2_wins:
            print("Player 1 is the Champion!")
        elif pl_2_wins > pl_1_wins:
            print("Player 2 is the Champion!")
        else:
            print("Tournament is tied!")
        break        