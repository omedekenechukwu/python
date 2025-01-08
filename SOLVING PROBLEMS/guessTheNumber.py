# This is a guess the number game
import random # Imports the random module
print('I am thinking of a number between 1 and 20')
print('You have 6 chances to make the right guess')

secretNumber = random.randint(1, 20) # defines a variable within this range of values
for guessesTaken in range(1, 7): # This is a loop that only allows 6 entries into it
  print('Take a guess')
  guess = int(input())
  if guess > secretNumber:
    print('Your guess is too high')
  elif guess < secretNumber:
    print('Your guess is too low')
  else: # This means that the guess is right but why don't we write the condition in the else statement directly? Why break it and then write it seperately? Well, we need to do so because the loop needs to end once the right guess is made or once the maximum no of trials is reached if not the loop will keep going even when you've made the right guess. An example of such code is given below.
    break
if guess == secretNumber:
  print('You guessed right. You made the right guess in ' + str(guessesTaken) + ' tries.')
else: 
  print('No. Trials are over and you guessed wrong. I was thinking of the number '+ str(secretNumber))

'''
import random # Imports the random module
print('I am thinking of a number between 1 and 20')
print('You have 6 chances to make the right guess')

secretNumber = random.randint(1, 20) # defines a variable within this range of values
for guessesTaken in range(1, 7): # This is a loop that only allows 6 entries into it
  print('Take a guess')
  guess = int(input())
  if guess > secretNumber:
    print('Your guess is too high')
  elif guess < secretNumber:
    print('Your guess is too low')
  elif guess == secretNumber:
    print('You have made the right guess in ' + str(guessesTaken) + ' tries.')
  else: 
    print('No. Maximum no of trials reached and you guessed wrong. The number I was thinking of is ' + str(secretNumber))
'''