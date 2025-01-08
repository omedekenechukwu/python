play = {'top-L': '', 'top-M': '', 'top-R': '',
        'mid-L': '', 'mid-M': '', 'mid-R': '',
        'bot-L': '', 'bot-M': '', 'bot-R': ''}

def grid(play):
  print(play['top-L'] + ' |' + play['top-M'] + ' |' + play['top-R'])
  print('-+-+-')
  print(play['mid-L'] + ' |' + play['mid-M'] + ' |' + play['mid-R'])
  print('-+-+-')
  print(play['bot-L'] + ' |' + play['bot-M'] + ' |' + play['bot-R'])
  
grid(play)