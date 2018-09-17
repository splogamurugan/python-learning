import random

guessnum = random.randint(1,10)

print('Hi human!, please enter your name')
name=input()
print('Im guessing a number from 1 to 10. Could you find it')
number=input()
while int(number) != guessnum:
    if int(number) > guessnum:
        print('your guess is high')
    elif int(number) < guessnum:
        print('Your guess is low')
    print('guess again')
    number = input()
print('You found it!')
