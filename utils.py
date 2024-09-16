import sys


def handle_user_input(user_input):
    if user_input == "/exit":
        sys.exit()


def delete_last_lines(number_of_lines: int = 1):
    for line in range(number_of_lines):
        sys.stdout.write('\033[F')  # Move cursor up one line
        sys.stdout.write('\033[K')  # Clear the line
        sys.stdout.flush()
