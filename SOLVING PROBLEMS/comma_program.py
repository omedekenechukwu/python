spam = ['bird', 'cat', 'dog', 'sheep']
bee = ['dime']
giver = ['never', 'lack']

def main(set):
  if len(set) == 0: # this sets what happens if length of the list is 0
    return ''
  elif len(set) == 1: # this sets what happens if length of the list is 1
    result = set[0]
    return result # the return statement is quite important so that when the function is called, it knows what to return
  else:
    result = '' # see how we defined a variable named result so that we can save the items one by one in the result
    for i in range(len(set) - 2): # this happens for the first n-2 items in the list
      result += set[i] + ', ' # this will save the items of the list from the first one to the second to the last one separating them with a comma
    result += set[-2] + ' and ' + set[-1] # for the last two items, they are seperated by and
    return result 

print(main(spam))
print(main(bee))
print(main(giver))