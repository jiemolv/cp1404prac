import random

def determine_score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score > 90:
            return "Excellent"
        elif score > 50:
            return "Passable"
        else:
            return "Bad"

def get_valid_score():
    while True:
        try:
            score = float(input("Enter a valid score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def print_result(score):
    status = determine_score_status(score)
    print(f"The status of the score is: {status}")

def show_stars(score):
    print("Stars: " + "*" * int(score))

def main_menu():
    print("\nMain Menu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")
    choice = input("Select an option: ").strip().upper()
    return choice

def main():
    score = get_valid_score()
    while True:
        choice = main_menu()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Farewell!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
