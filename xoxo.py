
class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choice_name(self):
        self.name = input("Enter your name (letters only): ")
        if not self.name.isalpha():
            print("Invalid name. Please use letters only.")
            self.choice_name()

    def choice_symbol(self):
        self.symbol = input("Enter your symbol: ")
        if len(self.symbol) != 1 or not self.symbol.isalpha():
            print("Invalid symbol. Please enter a single letter.")
            self.choice_symbol()
        else:
            self.symbol = self.symbol.upper()


class Menu:
    def display_menu(self):
        print("1. Start Game")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")
        return choice

    def display_end(self):
        print("Game over!")
        print("1. Restart")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")
        return choice


class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self):
        for i in range(0, 9, 3):
            print(" | ".join(self.board[i:i + 3]))
            if i < 6:
                print("-" * 5)

    def update_board(self, choice, symbol):
        if self.validate_choice(choice):
            self.board[choice - 1] = symbol
            return True
        return False

    def validate_choice(self, choice):
        return self.board[choice - 1].isdigit()

    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]


class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.display_menu()
        if choice == '1':
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for player in self.players:
            player.choice_name()
            player.choice_symbol()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def play_game(self):
        self.board.reset_board()
        while True:
            self.board.display_board()
            current_player = self.players[self.current_player_index]
            print(f"{current_player.name}'s turn ({current_player.symbol})")
            
            try:
                choice = int(input("Enter a position (1-9): "))
            except ValueError:
                print("Invalid input! Enter a number between 1-9.")
                continue

            if choice < 1 or choice > 9:
                print("Choice must be between 1-9.")
                continue

            if self.board.update_board(choice, current_player.symbol):
                if self.check_winner(current_player.symbol):
                    self.board.display_board()
                    print(f"🎉 {current_player.name} wins!")
                    break
                elif all(not cell.isdigit() for cell in self.board.board):
                    self.board.display_board()
                    print("It's a draw!")
                    break
                else:
                    self.switch_player()
            else:
                print("That position is already taken. Try again!")

        end_choice = self.menu.display_end()
        if end_choice == '1':
            self.play_game()
        else:
            self.quit_game()

    def check_winner(self, symbol):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Cols
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        return any(all(self.board.board[i] == symbol for i in combo) for combo in win_combinations)

    def quit_game(self):
        print("Thank you for playing!")


# Run the game
game = Game()
game.start_game()
