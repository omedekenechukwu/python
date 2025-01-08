def spam(divideby):
  try:
    return 42/divideby #remember when a function has a return value, we have to call it with a 'print' to get an output
  except ZeroDivisionError:
    print('Error: Invalid Divideby')

print(spam(2)) 
print(spam(12))
print(spam(0))
print(spam(1))