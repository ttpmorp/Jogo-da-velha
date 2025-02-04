def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def check_winner(board, player):
    # Verifica linhas, colunas e diagonais
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Verifica linhas
            return True
        if all([board[j][i] == player for j in range(3)]):  # Verifica colunas
            return True
    if all([board[i][i] == player for i in range(3)]):  # Verifica diagonal principal
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # Verifica diagonal secundária
        return True
    return False

def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]

    # Escolha dos nomes dos jogadores
    player_x = input("Digite o nome do jogador X: ")
    player_o = input("Digite o nome do jogador O: ")

    # Dicionário para mapear símbolos aos nomes dos jogadores
    players = {"X": player_x, "O": player_o}
    current_player = "X"

    while True:
        print_board(board)
        print(f"Vez do jogador {players[current_player]} ({current_player})")

        try:
            row = int(input("Escolha a linha (1, 2, 3): ")) - 1  # Ajusta para índice 0
            col = int(input("Escolha a coluna (1, 2, 3): ")) - 1  # Ajusta para índice 0

            if row not in range(3) or col not in range(3):  # Verifica se a escolha está dentro do intervalo
                print("Escolha inválida! As linhas e colunas devem ser 1, 2 ou 3. Tente novamente.")
                continue

            if board[row][col] != " ":
                print("Posição já ocupada! Tente novamente.")
                continue

        except ValueError:  # Captura erros de entrada não numérica
            print("Entrada inválida! Digite apenas números. Tente novamente.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Parabéns, {players[current_player]} ({current_player}) venceu!")
            break

        if is_board_full(board):
            print_board(board)
            print("Empate!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()