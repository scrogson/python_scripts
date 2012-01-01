import random

guesses_taken = 0

print('Hello! What is your name?')
name = input()

number = random.randint(1, 20)
print('Well, ' + name + ', I am thinking of a number between 1 and 20.')

while guesses_taken < 6:
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    guesses_taken = guesses_taken + 1

    if guess < number:
        print('Your guess is too low.')
    
    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break
if guess == number:
    print('Good job, ' + name + '! You guessed my number in ' + str(guesses_taken) + ' guesses!')

if guess != number:
    print('Nope. The number I was thinking was ' + str(number))
