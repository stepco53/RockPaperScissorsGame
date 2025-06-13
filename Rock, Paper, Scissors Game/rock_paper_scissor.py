# Rock, Paper, Scissors Game
# if user win. print "You win!"
# if user lose. print "You lose!"
# if tie. print "It's a tie!"
# after the user says no, print the probability of winning the game
import random


def play_game():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        return None

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "You lose!"


def main():
    total_games = 0
    wins = 0
    losses = 0
    ties = 0

    while True:
        result = play_game()
        if result is None:
            continue

        total_games += 1

        if result == "You win!":
            wins += 1
        elif result == "You lose!":
            losses += 1
        else:
            ties += 1

        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    if total_games > 0:
        win_probability = (wins / total_games) * 100
        print(f"Total games played: {total_games}")
        print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")
        print(f"Your winning probability is: {win_probability:.2f}%")
    else:
        print("No games played.")


if __name__ == "__main__":
    main()
