"""
rps.py

Redistributed and modified with permission from the
EECS Department at The University of Michigan, Ann Arbor

Name: Samantha Cambridge

CS 104: Project 2
FALL 2026

Description: This program plays a three round Rock, Paper, Scissors game between two players. It manages input, scoring, and winner announcements.
"""

# ***********************************************************************
# Constants. Global constants are fine. Global variables are not.
# Use these names in your code instead of typing the raw values.
# ***********************************************************************
COURSE_NAME = "CS 104"
MAX_ROUNDS = 3

ROCK = "r"
PAPER = "p"
SCISSORS = "s"
DEFAULT_MOVE = ROCK

PLAYER_1 = 1
PLAYER_2 = 2
DEFAULT_NAME_1 = "Rocky"
DEFAULT_NAME_2 = "Creed"

DRAW = 0

ERROR_NAME = 1
ERROR_MOVE = 2

PLAY_RPS = 1
PLAY_RPSLS = 2
QUIT_CHOICE = 3

def get_name(player_number):
    """Prompt for a name; use default if empty."""
    name = input(f"Player {player_number}, enter your name: ")

    if name == "":
        print_error_message(ERROR_NAME)
        if player_number == PLAYER_1:
            return DEFAULT_NAME_1
        else:
            return DEFAULT_NAME_2

    return name


def get_menu_choice():
    """Print menu, ask until valid choice (1–3)."""
    while True:
        print_menu()
        choice_str = input("Choice --> ")

        # Validate string first
        if choice_str.isdigit():
            choice = int(choice_str)
            if choice in (PLAY_RPS, PLAY_RPSLS, QUIT_CHOICE):
                return choice

        print("Invalid menu choice")


def is_move_good(move):
    """Return True only if move is r/p/s (any case)."""
    if not isinstance(move, str) or len(move) != 1:
        return False

    return move.lower() in (ROCK, PAPER, SCISSORS)


def get_move(player_name):
    """Prompt for move; return default rock if invalid."""
    move = input(f"{player_name}, enter your move: ")

    if is_move_good(move):
        return move.lower()

    print_error_message(ERROR_MOVE)
    return DEFAULT_MOVE


def is_round_winner(move, opponent_move):
    """Return True if move beats opponent_move."""
    move = move.lower()
    opponent_move = opponent_move.lower()

    if move == ROCK and opponent_move == SCISSORS:
        return True
    if move == SCISSORS and opponent_move == PAPER:
        return True
    if move == PAPER and opponent_move == ROCK:
        return True

    return False


def announce_round_winner(winner_name):
    """Print round result."""
    if winner_name == "":
        print("This round is a draw!")
    else:
        print(f"{winner_name} wins the round!")


def do_round(p1_name, p2_name):
    """Play one round and return DRAW, PLAYER_1, or PLAYER_2."""
    p1_move = get_move(p1_name)
    p2_move = get_move(p2_name)

    if p1_move == p2_move:
        return DRAW

    if is_round_winner(p1_move, p2_move):
        return PLAYER_1

    if is_round_winner(p2_move, p1_move):
        return PLAYER_2

    return DRAW


def announce_winner(winner_name):
    """Print final game result."""
    if winner_name == "":
        print("No winner!")
    else:
        print(f"Congratulations {winner_name}!")
        print(f"You won {COURSE_NAME} Rock, Paper, Scissors!")


def do_game(p1_name, p2_name, game_type):
    """Play MAX_ROUNDS rounds; return winner name or empty string."""
    if game_type == PLAY_RPSLS:
        print("Under Construction")
        print("No winner!")
        return ""

    p1_wins = 0
    p2_wins = 0

    for _ in range(MAX_ROUNDS):
        result = do_round(p1_name, p2_name)

        if result == PLAYER_1:
            p1_wins += 1
            announce_round_winner(p1_name)
        elif result == PLAYER_2:
            p2_wins += 1
            announce_round_winner(p2_name)
        else:
            announce_round_winner("")

    if p1_wins > p2_wins:
        winner = p1_name
    elif p2_wins > p1_wins:
        winner = p2_name
    else:
        winner = ""

    announce_winner(winner)
    return winner


def rps():
    """Run the full program."""
    print_initial_header()

    p1_name = get_name(PLAYER_1)
    p2_name = get_name(PLAYER_2)

    while True:
        choice = get_menu_choice()

        if choice == QUIT_CHOICE:
            break
        elif choice == PLAY_RPS:
            do_game(p1_name, p2_name, PLAY_RPS)
        elif choice == PLAY_RPSLS:
            do_game(p1_name, p2_name, PLAY_RPSLS)

    print_closer()


# ***********************************************************************
# DO NOT MODIFY THESE FUNCTIONS
# ***********************************************************************

def print_initial_header():
    print("----------------------------------------")
    print("                CS 104")
    print("          Rock, Paper, Scissors")
    print("----------------------------------------")


def print_menu():
    print()
    print("Menu Options")
    print("------------")
    print("1) Play rock, paper, scissors")
    print("2) Play rock, paper, scissors, lizard, spock")
    print("3) Quit")
    print()


def print_error_message(error_number):
    if error_number == ERROR_NAME:
        print()
        print("ERROR: Illegal name given, using default")
        print()
    elif error_number == ERROR_MOVE:
        print()
        print("ERROR: Illegal move given, using default")
    else:
        print("This should never print!")


def print_closer():
    print()
    print("----------------------------------------")
    print("           Thanks for playing")
    print("          Rock, Paper, Scissors!")
    print("----------------------------------------")
