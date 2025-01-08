import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
 count.setdefault(character, 0) # this sets the default value to 0 and assigns it to the count variable
 count[character] += 1 # this piece ensures that even when the default is set to 0, it should count 1 because obviously the character exists in the message variable.
print(pprint.pformat(count))