'''
print('Hello World!')
print('What is your name?') 
myName = input() #This asks to input a name. I think the input always treats whatever is written as a string as shown in lines 6 and 9
print('It is nice meeting you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')
myAge = input()
print('That is good. You will be ' + str(int(myAge) + 1) + ' in a year.') 
'''

'''
IF AND ELSE COMBINATIONS
yourName = input()
if yourName == 'Alice' :
  print('Hello Alice')
else:
  print('Hello stranger')

'''

'''
name = 'Michael'
if name == 'Alice':
  print('Hi, Alice')
else: 
  print('Hi, ' + name)
'''

'''
IF, ELIF AND ELSE COMBINATIONS
name = input()
age = input()
age = int(age)

if name == 'Alice':
  print('Welcome Alice')
elif age < 12:
  print('You are a little kid')
elif age > 2000: 
  print('You are a vampire')
elif age > 100:
  print('You are a grannie')
else:
  print('Hmm, you are a stranger')

'''
'''
WHILE LOOP
spam = 0
while spam < 5:
  print('Hello World')
  spam = spam + 1

name = ''
while name != 'your name':
  print('Please enter your name')
  name = input()
print('Thank you!')
'''

'''
WHILE LOOP USING THE BREAK AND CONTINUE STATEMENTS
name = ''
while True:
  print('Who are you?')
  name = input('Enter your name: ')
  if name != 'Joe':
    continue
  print('Hello Joe, please enter the password')
  password = input('Input Password: ')
  if password == 'swordfish':
    break
print('Access Granted')
'''

'''
FOR LOOP AND RANGE() FUNCTION
print('My name is')
for name in range(5):
  print('Jimmy Five Times (' + str(name) + ')')

FINDING THE SUM OF NUMBERS FROM 0-100
total = 0
for num in range(101):
  total = total + num
print(total)

USING A WHILE LOOP TO CREATE A FOR LOOP
print('My name is')
num = 0
while num < 5:
  print('Jimmy Five Times (' + str(num) + ')')
  num += 1

THE STARTING, STOPPING AND STEPPING ARGUMENTS OF A RANGE FUNCTION
for num in range(30,50,2):
  print(num)

import sys

while True:
  print('Type exit to exit')
  response = input()
  if response == 'exit':
    sys.exit()
'''
def spam(eggs):
  print(eggs)
spam(45)