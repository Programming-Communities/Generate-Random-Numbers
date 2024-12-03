import random

# Define the number of rounds to play
NUM_ROUNDS = 5

# Initialize the score
score = 0

# Play the game for multiple rounds
for round_num in range(1, NUM_ROUNDS + 1):
    print(f"\nRound {round_num}")
    
    # Generate random numbers for this round
    player_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)

    # Ask the player for their guess
    guess = input(f"Your number is {player_number}. Do you think your number is higher or lower than the computer's? (Type 'higher' or 'lower'): ").lower()

    # Ensure valid input
    while guess not in ["higher", "lower"]:
        guess = input("Invalid input! Please type 'higher' or 'lower': ").lower()

    # Check if the guess is correct
    if (guess == "higher" and player_number > computer_number) or (guess == "lower" and player_number < computer_number):
        print(f"You were right! The computer's number was {computer_number}.")
        score += 1  # Increment the score
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}.")
    
    # Display the score after each round
    print(f"Your score is now {score}")

# Final message based on score
if score == NUM_ROUNDS:
    print("\nExcellent! You got a perfect score!")
elif score > NUM_ROUNDS / 2:
    print("\nGood job! You did well.")
else:
    print("\nBetter luck next time!")
