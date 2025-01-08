account = {'Joe': 'boy', 'Sarah': 'girl', 'John': 'male', 'Mary': 'female'} # DATABASE

while True: # Creates an infinite loop
  print('Who are you?')
  name = input()
  if name not in account.keys():
    print('You don\'t have an account with us.')
    password = input('Enter your password to create an account with us: ')
    account.setdefault(name, password) # account[name] = password. That's another way of writing this line of code
    print('Your data has been saved.')

  else: 
    print('Welcome ' + name + '. Please input your password:')
    password = input()
    if password == account.get(name):
      print('Access Granted.')
    else:
      print('Access Denied.')
      break

#You can always modify this code and to include the features that are in nameAndPassword2.py