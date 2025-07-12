import random

number = random.randint(1, 10)
attempts = 0

while attempts < 3:
    guess = int(input("🎯 Guess a number between 1 and 10: "))
    if guess == number:
        print("🎉 Congratulations! You guessed the number!")
        break
    else:
        print("❌ Wrong guess. Try again.")
        attempts += 1

if attempts == 3 and guess != number:
    print(f"😢 No more attempts. The correct number was {number}.")
