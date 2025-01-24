import random


random_number1 = random.randint(1,20)
random_number2 = random.randint(1,20)
random_number3 = random.randint(1,20)

while True:

        guess = int(input("Guess 1 number from 1 to 20:"))
        if guess < 1 or guess > 20:
            print("You entered wrong value")
            continue

            if random_number1 == guess or random_number2 == guess or random_number3 == guess:
                print(f"Nice! You guessed it right. The number was {random_number1,random_number2,random_number3}.")
            else:
                print(f"Sorry, you guessed it wrong. The number was {random_number1,random_number2,random_number3}.")


            next_game = input("Do you want to play again (yes/no): ")
            if next_game != "yes":
                print("Thanks for playing")
                break
            else:
                print("Let's Continue")
       
            
