# This is the Collatz Sequence
def collatz(num): # defines the function for the Collatz sequence
  while num != 1: # begins the while loop for the condition that num is not equal to 1. 1 which is our final destination
    print(num) # this prints the current number
    if num % 2 == 0:
      num = num // 2
    else:
      num = 3 * num + 1
  print(num) # this prints the number 1. This is because the while loop ends when the while condition becomes false that is when num = 1; the loops breaks but that doesn't change the value of num(1) so all we need do is ask for it using the print function.
  
try: # this is used for input validation to make sure that the user puts the right type of input and when they don't, the except ValueError message will be displayed rather than the long stuff VSCode will bring up. It would also help to not terminate the code completely but allow for other parts of the code to run-if there were any which there aren't
  number = int(input('Enter your number: '))
  collatz(number)
except ValueError:
    print('Error. You have entered an invalid integer')