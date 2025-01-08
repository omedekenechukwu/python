print('Enter your number: ')
for i in range(5): # This for loop works only for when the inputs of the user are invalid
  try: # This is to validate when the user types in a string rather than an integer
    num = int(input())

    if (num <= 0): # This dictates what happens when a negative integer is inputted
      if i == 4: 
        print('You have failed your last attempt.')
      else:
        print('Invalid Input. Please Try Again!')
    else:
      break 
  except ValueError: # This defines what happens when a string is inputted
    if i == 4: 
      print('You have failed your last attempt.')
  
    else:
      print('Invalid Input. Please Try Again.')  

if num > 0 :
  if num == 1:
    print('The number ' + str(num) + ' is not a prime number.')

  elif num > 10:
    if (num % 2 == 0) or (num % 3 == 0) or (num % 5 == 0) or (num % 7 == 0):
      print('The number ' + str(num) + ' is not a prime number.')

    else:
      print('The number ' + str(num) + ' is a prime number')

  else:
    if (num % 4 == 0) or (num % 6 == 0) or (num % 8 == 0) or (num % 9 == 0):
      print('The number ' + str(num) + ' is not a prime number.')

    else: 
      print('The number ' + str(num) + ' is a prime number.')


# Now to improve this code for better readability, you could work on the divisibility checks. You could define a list of 2, 3, 5, 7. Every number in divisible by either of these numbers if not, that number is a prime number. So write an if statement checking if the number - greater than or equal to 10, mind you - is divisible by any of them. If true, it prints the number is not a prime number else the number is a prime number. I'M SO PROUD OF HOW WE'VE COME SO FAR THOUGH!