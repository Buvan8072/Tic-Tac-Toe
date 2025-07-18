def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)              
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_draw(board):
    return ' ' not in board

def main():
    board = [' '] * 9
    current_player = "X"
    print("Welcome to Tic Tac Toe!\n")
    print_board([str(i+1) for i in range(9)]) 

    while True:
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] != ' ':
                print("That spot is already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number from 1 to 9.")
            continue

        board[move] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins! 🎉")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a draw! 🤝")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
