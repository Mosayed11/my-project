class player:
    def __init__(self):
        self.name = ""
        self.symbol = ""
def choice_name(self):
    self.name = input("Enter your name(litters only): ")
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
class menu:
    def display_mnue(self):
        print("1. Start Game")
        print("2. Exit")

    
        choice = input("Enter your choice(1 or 2) ")
        return choice
    def display_end(self):
       menu_text = ""
       print("Game over!")
       print("1. Restart")
       print("2. Exit")
       choice = input("Enter your choice(1 or 2): ")
       return choice
class board:
    def __init__(self):
        self.board = [str(i) for i in range(0,10)]
    def display_board(self):
        for i in range(0,9,3):
            print(" | ".join(self.board[i:i+3]))
            if i < 6:
                print("-" * 5)

def update_board(self, choice, symbol):
    if self.validate_choice(choice):
        self.board[choice-1] = symbol
        return True
    return False

def validate_choice(self, choice):
    return self.board[choice-1].isdigit 

def reset_board(self):
    self.board = [str(i) for i in range(0,10)]

class game:
    def __init__(self):
        self.players = [player(), player()]
        self.board = board()
        self.menu = menu()
        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.display_mnue()
        if choice == '1':
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for player in self.players:
            player.choice_name()
            player.choice_symbol()

    def play_game(self):
        # TODO: Implement the game logic here
        pass

    def quit_game(self):
        print("Thank you for playing!")

game = game()
game.start_game()



