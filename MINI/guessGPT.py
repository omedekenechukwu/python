secretNumber = 15
trials = 3

# This for loops runs to compare the secretNumber and guess of the user and display the right message. The number of times of this for loop runs is determined by the trials variable
for num in range(trials):
  guess = int(input('Take a guess: '))

  if guess == secretNumber:
    print('Congratualtions. You guessed the correct number.')
    break # Exits the loop if the condition is met

  elif num == trials - 1:
    print('You have failed the final attempt!')

  else:
    print('Wrong Guess. Try Again!')

# This code will only if the entire for loop runs without encountering a break  
else:
  print('You have run out of attempts. The secretNumber was ' + str(secretNumber))