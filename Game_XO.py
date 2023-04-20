import random

game_field = [" "]*9

def output_field():
    print(" " + game_field[0] + " | " + game_field[1] + " | " + game_field[2] + " ")
    print("---|---|---")
    print(" " + game_field[3] + " | " + game_field[4] + " | " + game_field[5] + " ")
    print("---|---|---")
    print(" " + game_field[6] + " | " + game_field[7] + " | " + game_field[8] + " ")

def player_input():
    marker = ""
    while marker != "X" and marker != "O":
        marker = input("Игрок 1, выбери фигуру для игры- X или O: ").upper()

    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")

def place_marker(game_field, marker, position):
    game_field[position] = marker

def win_check(game_field, mark):
    return ((game_field[0] == game_field[1] == game_field[2] == mark) or
    (game_field[3] == game_field[4] == game_field[5] == mark) or
    (game_field[6] == game_field[7] == game_field[8] == mark) or
    (game_field[0] == game_field[3] == game_field[6] == mark) or
    (game_field[1] == game_field[4] == game_field[7] == mark) or
    (game_field[2] == game_field[5] == game_field[8] == mark) or
    (game_field[0] == game_field[4] == game_field[8] == mark) or
    (game_field[2] == game_field[4] == game_field[6] == mark))

def choose_first():
    if random.randint(0, 1) == 0:
        return "Игрок 2"
    else:
        return "Игрок 1"

def space_check(game_field, position):
    return game_field[position] == " "

def full_game_field_check(board):
    for i in range(0, 9):
        if space_check(board, i):
            return False
    return True

def player_choice(game_field):
    position = " "
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] or not space_check(game_field, int(position)-1):
        position = input("Ходит " + turn + ". Выберите поле для следующего хода (цифры от 1 до 9): ")
    return int(position) - 1

def replay():
    return input("Хотите играть ещё раз? Введите Yes или No: ").lower().startswith("y")

print("Добро пожаловать в игру!")

while True:
    game_field = [" "]*9
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + " делает первый ход.")

    while True:
        if turn == "Игрок 1":
            output_field()
            position = player_choice(game_field)
            place_marker(game_field, player1_marker, position)
            if win_check(game_field, player1_marker):
                output_field()
                print("Поздравляю! Игрок 1 Вы выиграли!")
                break
            else:
                if full_game_field_check(game_field):
                    output_field()
                    print("Ничья!")
                    break
                else:
                    turn = "Игрок 2"

        else:
            output_field()
            position = player_choice(game_field)
            place_marker(game_field, player2_marker, position)
            if win_check(game_field, player2_marker):
                output_field()
                print("Поздравляю! Игрок 2 Вы выиграли!")
                break
            else:
                if full_game_field_check(game_field):
                    output_field()
                    print("Ничья!")
                    break
                else:
                    turn = "Игрок 1"

    if not replay():
        break
