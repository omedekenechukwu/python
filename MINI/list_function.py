def main(result):
  if len(result) == 0:
    print('The list is empty.')
  elif len(result) == 1:
    print(result[0])
  else:
    print(', '.join(result[:-2]) + ' and ' + result[-1])

names = ['James', 'Bennie', 'Victor', 'Kenechukwu', 'Nduoma', 'Osokam', 'Daniel', 'Kelikume']
ready = []
nice = ['good']
main(names)