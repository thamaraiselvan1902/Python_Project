import sys 

player_1_choice = 'X'
player_2_choice = 'O'
game_draw = 'DRAW'

grid = [cell for cell in range (9)]

def display_grid():

    print(f"{grid[0]} {grid[1]} {grid[2]}") 
    print(f"{grid[3]} {grid[4]} {grid[5]}")
    print(f"{grid[6]} {grid[7]} {grid[8]}")

display_grid()

def check_winner():

    if grid[0] == grid[1] == grid[2]:
        return grid[0]
    elif grid[3] == grid[4] == grid[5]:
        return grid[3]
    elif grid[6] == grid[7] == grid[8]:
        return grid[6]
    elif grid[0] == grid[3] == grid[6]:
        return grid[0]
    elif grid[1] == grid[4] == grid[7]:
        return grid[1]
    elif grid[2] == grid[5] == grid[8]:
        return grid[2]   

    elif grid[2] == grid[4] == grid[6]:
        return grid[2]
    elif grid[0] == grid[4] == grid[8]:
        return grid[2] 

    else:
        for cell in grid:
            if isinstance(cell, int):
                return

        return game_draw

def game():

    winner = check_winner()

    if winner == 'X':
        print("X: is the winner")
        display_grid()
        sys.exit()

    elif winner == 'O':
        print("O: is the winner")
        display_grid()
        sys.exit()

    elif winner == game_draw:
        print("Game is draw")
        sys.exit        


def update_grid(choice, location):
    if location < 0 or location > 9:
        raise ValueError("Not a valid location")

    if grid[location] == 'X' or grid[location] == 'o':
        raise ValueError("Location already filled with", grid[location])

    else:
        grid[location] = choice

def main():
    player_1_location = int(input("player [X] Enter your choice from ( 0 to 8) ="))

    update_grid(player_1_choice, player_1_location)
    game()

    player_1_location = int(input("player [O] Enter your choice from ( 0 to 8) ="))

    update_grid(player_2_choice, player_1_location)
    game()
    display_grid()

while True:
    main()