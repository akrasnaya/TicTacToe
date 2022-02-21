""" This program imitates tic-tac-toe game. Users should enter coordinates in 3x3 field
depending where they would like to place their character one by one starting from X"""





""" Function for cheking user's input"""

def check_input():
    while True:
        users_input = input('Enter the coordinates: ').split()
        if users_input[0].isalpha() == True or users_input[1].isalpha() == True:
            print('You should enter numbers!')
            continue
        elif int(users_input[0]) < 1 or int(users_input[0]) > 3 or int(users_input[1]) < 1 or int(users_input[1]) > 3:
            print('Coordinates should be from 1 to 3!')
            continue
        elif field[int(users_input[0]) - 1][int(users_input[1]) - 1] != "_":
            print('This cell is occupied! Choose another one!')
        elif field[int(users_input[0]) - 1][int(users_input[1]) - 1] == "_":
            return users_input



""" Analyzing the currrent state on the field, predicting outcomes """

def analyze_game(field: list):

    countX_total = 0
    countO_total = 0
    count_empty_total = 0

    winX_count = 0
    winO_count = 0

    diag = []
    rev_diag = [field[0][2], field[1][1], field[2][0]]

    for i in range(3):
        for j in range(3):
            if i == j:
                diag.append(field[i][j])

            if field[i][j] == 'X':
                countX_total += 1
            elif field[i][j] == 'O':
                countO_total += 1
            else:
                count_empty_total += 1

    # Cheking the winning on diagonals
    if (diag.count('X') == 3) or (rev_diag.count('X') == 3):
        winX_count += 1
    elif (diag.count('O') == 3) or (rev_diag.count('O') == 3):
        winO_count += 1

    # Cheking winnings on rows and columns
    for i in range(3):
        if field[i].count('X') == 3:
            winX_count += 1
        elif field[i].count('O') == 3:
            winO_count += 1
        countX = 0
        countO = 0
        count_empty = 0

        for j in range(3):

            if field[j][i] == 'X':
                countX += 1
            elif field[j][i] == 'O':
                countO += 1
            else:
                count_empty += 1

            if countX == 3:
                winX_count += 1
            elif countO == 3:
                winO_count += 1


    if (winX_count == 1) and (winO_count == 1):
        return 'Impossible'
    elif abs(countX_total - countO_total) >= 2:
        return 'Impossible'
    elif (count_empty_total != 0) and (winX_count == 0) and (winO_count == 0):
        return 'Game not finished'
    elif winX_count == 1:
        return 'X wins'
    elif winO_count == 1:
        return 'O wins'
    elif (count_empty_total == 0) and (winX_count == 0) and (winO_count == 0):
        return 'Draw'


""" Function for printing field in an appropriate way """
def print_field(field: list):
    print('---------')
    print('|', field[0][0], field[0][1], field[0][2], '|')
    print('|', field[1][0], field[1][1], field[1][2], '|')
    print('|', field[2][0], field[2][1], field[2][2], '|')
    print('---------')



""" Initializing empty field """

enter_cells = '_________'

field = [[enter_cells[0], enter_cells[1], enter_cells[2]],
         [enter_cells[3], enter_cells[4], enter_cells[5]],
         [enter_cells[6], enter_cells[7], enter_cells[8]]]

print_field(field)

""" Actual game loop """
while True:
    users_positionX = check_input()

    field[int(users_positionX[0]) - 1][ int(users_positionX[1]) - 1] = "X"
    print_field(field)
    if analyze_game(field) == 'X wins' or analyze_game(field) == 'Impossible' or analyze_game(field) == 'Draw':
        print(analyze_game(field))
        break

    users_positionO = check_input()

    field[int(users_positionO[0]) - 1][int(users_positionO[1]) - 1] = "O"
    print_field(field)
    if analyze_game(field) == 'O wins' or analyze_game(field) == 'Impossible' or analyze_game(field) == 'Draw':
        print(analyze_game(field))
        break




