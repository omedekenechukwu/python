attempts = 0
while attempts < 5:
  print('Who are you?')
  name = input()
  attempts += 1

  # This validates the name to ascertain whether Joe or Sarah
  if name == 'Joe' or name == 'Sarah':
    print('Welcome ' + name + '. Please input your password')
    password = input()

    # Validates password based on name
    if (name == 'Joe'and password == 'boy') or (name == 'Sarah' and password == 'girl'): 
      print('Access Granted, ' + name)

    else: 
      print('Access Denied. Wrong Password')
      continue # Restarts the loop for wrong password

  else:
    print('You are not the right person.')
    continue # Restarts the loop for wrong name

  break # Exits the loop when both name and password are correct

if attempts == 5: # This tells the program what to print when the user enters incorrect names 5 times
    print('Maximum Number of Trials Reached!')
    
if attempts < 5: # This will only run if the user is able to enter the right name and password before the reaching the maximum no of tries
  print('Thank you!')