

---

## **High-Low Game Explanation**

### **Objective:**
The goal of the High-Low Game is to guess if your number is higher or lower than the computer's number. You get a point for each correct guess, and the game is played over multiple rounds.

---

### **Milestone #1: Generate Random Numbers**

**Objective:**  
In this milestone, we will generate two random numbers using Python's `random` module.

**Code Explanation:**
```python
import random

# Generate two random numbers
player_number = random.randint(1, 100)
computer_number = random.randint(1, 100)

# Print both numbers for testing
print("Player's number:", player_number)
print("Computer's number:", computer_number)
```

- `random.randint(1, 100)` generates a random integer between 1 and 100 (inclusive).
- We generate two random numbers: one for the player and one for the computer.
- Both numbers are printed to verify the correctness of the random number generation (this step will be removed later in the final game).

---

### **Milestone #2: Get the User Choice**

**Objective:**  
This milestone focuses on getting the player's guess (whether their number is higher or lower than the computer’s number).

**Code Explanation:**
```python
# Ask the player to guess if their number is higher or lower than the computer's
guess = input(f"Your number is {player_number}. Do you think your number is higher or lower than the computer's? (Type 'higher' or 'lower'): ").lower()

# Display the player's guess
print("You guessed:", guess)
```

- We use `input()` to ask the user whether they think their number is "higher" or "lower" than the computer's number.
- The `.lower()` method is used to ensure that the input is case-insensitive.
- The guess is displayed for confirmation.

---

### **Milestone #3: Write the Game Logic**

**Objective:**  
We need to compare the player’s guess with the actual comparison between the player’s number and the computer’s number.

**Code Explanation:**
```python
# Check if the guess matches the actual comparison
if (guess == "higher" and player_number > computer_number) or (guess == "lower" and player_number < computer_number):
    print(f"You were right! The computer's number was {computer_number}.")
    correct_guess = True
else:
    print(f"Aww, that's incorrect. The computer's number was {computer_number}.")
    correct_guess = False
```

- If the player's guess is correct (i.e., they guessed "higher" and their number is indeed higher than the computer's, or they guessed "lower" and their number is lower), they are awarded a point.
- If the guess is incorrect, we inform the player and reveal the correct answer.

---

### **Milestone #4: Play Multiple Rounds**

**Objective:**  
This milestone involves playing the game over multiple rounds. We will repeat the process for a specified number of rounds, generating new numbers each time.

**Code Explanation:**
```python
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
```

- We set `NUM_ROUNDS` to 5, meaning the game will be played for 5 rounds.
- In each round, we generate new random numbers for the player and the computer.
- After each guess, the score is updated based on whether the guess was correct or not.

---

### **Milestone #5: Adding a Points System**

**Objective:**  
Keep track of the score and display it after each round.

**Code Explanation:**
- A `score` variable is initialized before the game starts, and it is incremented each time the player makes a correct guess.
- At the end of each round, the score is displayed to the player.

---

### **Extension #1: Safeguard User Input**

**Objective:**  
Handle invalid user input, ensuring that the player enters "higher" or "lower" as their guess.

**Code Explanation:**
```python
# Loop to ensure the user enters a valid guess
while guess not in ["higher", "lower"]:
    guess = input("Invalid input! Please type 'higher' or 'lower': ").lower()
```

- If the player enters an invalid guess, we repeatedly prompt them to enter a valid choice.

---

### **Extension #2: Conditional Ending Messages**

**Objective:**  
Provide feedback to the player based on their performance at the end of the game.

**Code Explanation:**
```python
# Conditional messages based on score
if score == NUM_ROUNDS:
    print("\nExcellent! You got a perfect score!")
elif score > NUM_ROUNDS / 2:
    print("\nGood job! You did well.")
else:
    print("\nBetter luck next time!")
```

- At the end of the game, the player receives a performance message based on their score:
  - Perfect score: "Excellent!"
  - More than half correct: "Good job!"
  - Less than half correct: "Better luck next time!"

---

### **Final Complete Code:**
```python
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
```

---


