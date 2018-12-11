import numpy as np
import datetime as dt

def get_power(x,y, serial):
  rackId = x + 10
  power = rackId * y + serial
  power *= rackId
  if power > 100:
    power = int(str(power)[-3])
  else:
    power = 0
  power -= 5
  return power

def main():
  begin = dt.datetime.now()
  serial = 7511
  grid = np.zeros([300,300])
  for x in range(300):
    for y in range(300):
      grid[x,y] += get_power(x+1,y+1, serial)

  max_power = 0
  x_max = 0
  y_max = 0
  gs_max = 0
  for grid_size in range(3, 300):
    for x in range(300-grid_size+1):
      for y in range(300-grid_size+1):
        power = np.sum(grid[x:x+grid_size,y:y+grid_size])
        if power > max_power:
          x_max = x+1
          y_max = y+1
          max_power = power
          gs_max = grid_size
    if grid_size == 3:
      print('For size grid = 3, max_power = {}, x_max = {}, y_max = {}'.format(max_power, x_max, y_max))
      d = dt.datetime.now() - begin
      print('And that took {:.3f} seconds'.format(d.seconds + 1e-6*d.microseconds))
  d = dt.datetime.now() - begin
  print('Max Power was found with a value of {} at x={}, y={}, with a grid size of {}'.format(max_power, x_max, y_max, gs_max))
  print('And the whole thing took {:.3f} seconds'.format(d.seconds + 1e-6*d.microseconds))

if __name__ == '__main__':
  main()
