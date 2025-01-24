import random

def random_number_game():
    print("Welcome to the Random Number Guessing Game!")
    print("I will think of a number between 1 and 20. Try to guess it!")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 20)
    
    attempts = 0
    
    while True:
        # Get user's guess
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        # Check the guess
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break

# Start the game
random_number_game()
