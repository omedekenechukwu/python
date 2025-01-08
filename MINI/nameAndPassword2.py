for i in range(5):
  print('Who are you?')
  name = input()

  # This validates the name to ascertain whether Joe or Sarah
  if name == 'Joe' or name == 'Sarah':
    print('Welcome ' + name + '. Please input your password')
    password = input()

    # Validates password based on name
    if (name == 'Joe'and password == 'boy') or (name == 'Sarah' and password == 'girl'): 
      print('Access Granted, ' + name)
      print('Thank you!')

    else: 
      print('Access Denied. Wrong Password')
      continue # Restarts the loop for wrong password

  else:
    print('You are not the right person.')
    continue # Restarts the loop for wrong name

  break # Exits the loop when both name and password are correct
else: 
  print('Maximum Number of Trials Reached!')