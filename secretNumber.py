import random

number = random.randint(1,10)
youTry = 0
print('Guess the number between 1 and 10. You have only 3 tries.')

while youTry < 3:
    guess = (int(input('Take a guess: ')))
    youTry += 1
    if guess == number:
        print('Congratulations! You guessed the number in ' + str(youTry) + ' tries.')
        break
    elif guess > number:
        print('Your guess is too high.')
    elif guess < number:
        print('Your guess is too low.')
if guess != number:
    print('You failed. The number I was thinking of was ' + str(number) + '.')