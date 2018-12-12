import numpy as np
import datetime as dt

def get_power(p, serial):
  rackId = p[:,0] + 10
  power = rackId * p[:,1] + serial
  power *= rackId
  power = ((power/100)%10).astype(int)
  power -= 5
  return power

def get_subgrid(p, grid_size, power_grid):
  return power_grid[p[:,0]:p[:,0]+grid_size, p[:,1]:p[:,1]+grid_size]

def get_grid_power(p, grid_size, power_grid):

def main():
  # so part a takes less than a second
  # and part b takes less than 3 minutes :P
  begin = dt.datetime.now()
  serial = 7511
  grid_points = np.array([(x,y) for x in range(1,301) for y in range(1,301)])
  power_grid = np.reshape(get_power(grid_points, serial), (300,300))

  max_power = x_max = y_max = gs_max = 0

  for grid_size in range(3, 300):
    z = [(x,y) for x in range(300 - grid_size + 1) for y in range(300 - grid_size + 1)]
    for x, y in z:
      power = np.sum(power_grid[x:x+grid_size,y:y+grid_size])
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
