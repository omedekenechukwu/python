import sys
def collatz(num): # Defines the function 
  if num % 2 == 0:
    num = num // 2
  else:
    num = 3 * num + 1
  return num # The function returns a number

while True: # This loop ensures that the user neither enters a string or a negative integer. Note though that using while True in this case means the user has an unlimited amount to tries to enter a positive integer
  try:
    number = int(input('Enter your number: ')) # Provides an input for the user to enter a number
    if number <= 0:
      print('You have entered a negative integer. Please enter a positive integer.')
    else:
      break # Exits the loop and moves on to the next piece of code
  except ValueError:
    print('Invalid input. Enter a positive integer')

while number != 1:
  number = collatz(number) # This calls the collatz function on the number and stores the new number
  print(number) # This prints the new number

# JUST IN CASE: The reason I imported a sys module here is because I wanted to deal with the error message that kept on showing up on the terminal as regards the except statement even after displaying the error message: Invalid input. Enter a positive integer. It seemed like with the code I wrote at that time, as far as the number was not equal to 1 (number !=1), it wanted to access the while loop. So I called the sys.exit() so that it completely terminates after the user enters the wrong input(a string). I should add that at that time, I didn't take negative integers into account. But the code above handles all.