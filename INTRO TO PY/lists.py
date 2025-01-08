catNames = [] # defines a variable with a empty list assigned to it.
while True: # an infinite loop initially
  print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
  name = input()
  if name == '':
    break # when this condition is met, the infinite loop breaks
  catNames = catNames + [name] # list concatenation - adds values being inputted to already existing list
print('The names of the cats are: ')
for name in catNames: # defines a for loop 
  print(' ' + name) # the ' ' is just give space to the LHS of the names

