message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
 count.setdefault(character, 0) # this sets the default value to 0 and assigns it to the count variable
 count[character] += 1 # this piece ensures that even when the default is set to 0, it should count 1 because obviously the character exists in the message variable.
print(count) 



# The code below sets the default value of the character to 1 and then when the character occurs again, it will add 1 to the existing value
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
  if character in count:
    count[character] += 1
  else:
    count.setdefault(character, 1)
print(count) 