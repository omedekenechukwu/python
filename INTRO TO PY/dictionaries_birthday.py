birthdays = {'Daddy': 'Sep 3', 'Mommy': 'Sep 1', 'Kene': 'Sep 17', 'Ndu': 'May 17', 'Osokam': 'Oct 26', 'Keli': 'Jun 12'}

while True:
  print('Enter the name: (Or enter blank to quit)')
  name = input()

  if name == '':
    break
  elif name in birthdays:
    print(birthdays[name] + ' is the birthday of ' + name)
  else:
    print('I do not have the birthday information of ' + name)
    bday = input('Enter information: ')
    birthdays[name] = bday  # this line is particularly important in that it helps to add (1) and store(2) new information for keys which are not available in the dictionary. for example : birthdays['Mary'] = Apr 8
    print('Birthday database has been updated')
