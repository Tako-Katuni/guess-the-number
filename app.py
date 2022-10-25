import random

print("Guess the number between 0 and 50. You have 10 guesses")
# Creating secret number
secret_number = random.randint(0, 50)

##Number of guesses
i = 0
while i < 10:
    guess = int(input(f'Guess number {i + 1}: '))
    i += 1
    if guess == secret_number:
        print(f'Congrats, good job. Guess count is {i+1}')
        break
    elif guess > secret_number:
        print("Nah, that's too high up")
    elif guess < secret_number:
        print("Now that's too low")

if i == 10:
    print(f'Off, what a loser. the number was {secret_number}')