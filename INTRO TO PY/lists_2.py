'''

spam = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']

while True:
  name = input('Enter a color: ')
  if name in spam:
    print('You are right. ' + name + ' is in the list')
    break
  else:
    print('This is not correct. ' + name + ' is not in the list.')
    continue
  '''

spam = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']
name = input('Enter a color: ')

if name in spam:
  print('You are right. ' + name + ' is in the list')
else:
  print('This is not correct. ' + name + ' is not in the list.')

# The difference between both sets of code is: the first code uses a while loop and the second does not. And what does this mean practically. It means that in the first code, if you input a right color, the loop breaks and stop execution but if you input a wrong color, it prints the required stuff and gives another opportunity to try again until you get it right. While in the second code, there is no opportunity to try again if you get it wrong at first try. Once you make an whether right or wrong, it prints the right statement and stops executing.