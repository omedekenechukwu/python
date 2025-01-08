def collatz(num):
  while num != 1:
    print(num)
    if num % 2 == 0:
      num = num // 2
    else:
      num = 3 * num + 1
  print(num)

number = int(input('Enter your number: '))
collatz(number)

'''
def divide_until_one(number):
    while number != 1:  # Keep dividing until the result is 1
        print(number)  # Print the current number
        number = number // 2  # Integer division by 2
    #print(number)  # Print the final result (1)

start_number = int(input("Enter a number: ")) 
divide_until_one(start_number)
'''
