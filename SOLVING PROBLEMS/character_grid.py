grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
'''        
while True:
  print(grid[0][0], end='')
  print(grid[1][0], end='')
  print(grid[2][0], end='')
  print(grid[3][0], end='')
  print(grid[4][0], end='')
  print(grid[5][0], end='')
  print(grid[6][0], end='')
  print(grid[7][0], end='')
  print(grid[8][0])
  break
while True:
  print(grid[0][1], end='')
  print(grid[1][1], end='')
  print(grid[2][1], end='')
  print(grid[3][1], end='')
  print(grid[4][1], end='')
  print(grid[5][1], end='')
  print(grid[6][1], end='')
  print(grid[7][1], end='')
  print(grid[8][1])
  break
while True:
  print(grid[0][2], end='')
  print(grid[1][2], end='')
  print(grid[2][2], end='')
  print(grid[3][2], end='')
  print(grid[4][2], end='')
  print(grid[5][2], end='')
  print(grid[6][2], end='')
  print(grid[7][2], end='')
  print(grid[8][2])
  break
while True:
  print(grid[0][3], end='')
  print(grid[1][3], end='')
  print(grid[2][3], end='')
  print(grid[3][3], end='')
  print(grid[4][3], end='')
  print(grid[5][3], end='')
  print(grid[6][3], end='')
  print(grid[7][3], end='')
  print(grid[8][3])
  break
while True:
  print(grid[0][4], end='')
  print(grid[1][4], end='')
  print(grid[2][4], end='')
  print(grid[3][4], end='')
  print(grid[4][4], end='')
  print(grid[5][4], end='')
  print(grid[6][4], end='')
  print(grid[7][4], end='')
  print(grid[8][4])
  break
while True:
  print(grid[0][5], end='')
  print(grid[1][5], end='')
  print(grid[2][5], end='')
  print(grid[3][5], end='')
  print(grid[4][5], end='')
  print(grid[5][5], end='')
  print(grid[6][5], end='')
  print(grid[7][5], end='')
  print(grid[8][5])
  break
'''

for x in range(len(grid[0])): # the main job of this for loop is to vary the value of x in the inner for loop from 0 to 5 (range of len(grid[0])). It handles the column to be processed x
  for y in range(len(grid)): # in this for loop, the value of y varies from 0 to 8(range of len(grid)) and the value of x remains constant until it moves to the next iteration which is what the outer for loop handles. It handles the row to be processed y
    print(grid[y][x], end='') # the end stops python from printing in a new line
  print() # tell python to print in a new line