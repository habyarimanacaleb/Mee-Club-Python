import random

class Person:
    def __init__(self, name):
        self.name = name
        self.calculation_history = []
        self.game_history = []

    def add_calculation(self, calculation):
        self.calculation_history.append(calculation)

    def add_game_result(self, result):
        self.game_history.append(result)

    def view_calculation_history(self):
        if not self.calculation_history:
            print(f"{self.name} has no calculations yet.")
        else:
            print(f"\n*** Calculation History for {self.name} ***")
            for calculation in self.calculation_history:
                print(calculation)
            print("***************************************\n")

    def view_game_history(self):
        if not self.game_history:
            print(f"{self.name} has no game history yet.")
        else:
            print(f"\n*** Game History for {self.name} ***")
            for result in self.game_history:
                print(result)
            print("***********************************\n")


def perform_calculation(person):
    try:
        num1 = float(input(f"{person.name}, enter first number: "))
        operation = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero")
                return
            result = num1 / num2
        else:
            print("Invalid operation")
            return

        calculation = f"{num1} {operation} {num2} = {result}"
        person.add_calculation(calculation)
        print("\n*** Calculation Result ***")
        print(f"Result: {result}")
        print("**************************\n")
    except ValueError:
        print("Invalid input, please enter numeric values.")

def play_rock_paper_scissors(player1, player2):
    choices = ['rock', 'paper', 'scissors']
    p1_choice = input(f"{player1.name}, enter rock, paper, or scissors: ").lower()

    if player2 == 'computer':
        p2_choice = random.choice(choices)
        print(f"Computer chose {p2_choice}")
    else:
        p2_choice = input(f"{player2.name}, enter rock, paper, or scissors: ").lower()

    if p1_choice not in choices or p2_choice not in choices:
        print("Invalid choice. Choose rock, paper, or scissors.")
        return

    if p1_choice == p2_choice:
        result = "It's a tie!"
    elif (p1_choice == 'rock' and p2_choice == 'scissors') or \
         (p1_choice == 'paper' and p2_choice == 'rock') or \
         (p1_choice == 'scissors' and p2_choice == 'paper'):
        result = f"{player1.name} wins!"
    else:
        result = f"{player2.name} wins!"

    print("\n*** Game Result ***")
    print(result)
    print("*******************\n")
    player1.add_game_result(result)
    if isinstance(player2, Person):
        player2.add_game_result(result)

def main():
    print("Welcome to the Rock, Paper, Scissors and Calculator Program!")
    player1_name = input("Enter name of Player 1: ")

    while True:
        player2_name = input("Enter name of Player 2: ")
        if player2_name.strip() == "":
            print("Player 2's name cannot be empty. Please enter a valid name.")
        elif player2_name == player1_name:
            print("Player 2's name must be different from Player 1's name. Please enter a different name.")
        else:
            break

    player1 = Person(player1_name)
    player2 = Person(player2_name)

    while True:
        print("\nOptions:")
        print("1. Perform Calculation")
        print("2. View Calculation History")
        print("3. Play Rock, Paper, Scissors")
        print("4. View Game History")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            user = input(f"Who will use the calculator? {player1.name} or {player2.name}: ")
            if user == player1.name:
                perform_calculation(player1)
            elif user == player2.name:
                perform_calculation(player2)
            else:
                print("Invalid user.")

        elif choice == '2':
            user = input(f"Whose calculation history do you want to see? {player1.name} or {player2.name}: ")
            if user == player1.name:
                player1.view_calculation_history()
            elif user == player2.name:
                player2.view_calculation_history()
            else:
                print("Invalid user.")

        elif choice == '3':
            user = input(f"Who is going to play? {player1.name}, {player2.name}, or computer: ")
            if user == player1.name:
                play_rock_paper_scissors(player1, player2)
            elif user == player2.name:
                play_rock_paper_scissors(player2, player1)
            elif user.lower() == "computer":
                play_rock_paper_scissors(player1, 'computer')
            else:
                print("Invalid user.")

        elif choice == '4':
            user = input(f"Whose game history do you want to see? {player1.name} or {player2.name}: ")
            if user == player1.name:
                player1.view_game_history()
            elif user == player2.name:
                player2.view_game_history()
            else:
                print("Invalid user.")

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()
