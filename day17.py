import pandas as pd
import numpy as np
import datetime as dt
import re

def main():
  lines = []
  infile = 'inputs/day17.txt'
  with open(infile) as f:
    lines = [x.strip() for x in f.readlines()]
  
  clay = []
  p1 = 'x=(\d+), y=(\d+)..(\d+)'
  p2 = 'y=(\d+), x=(\d+)..(\d+)'
  for line in lines:
    squares = []
    x_first = True
    parsed = re.search(p1, line)
    if not parsed:
      x_first = False
      parsed = re.search(p2, line)
    a, b, c = [int(x) for x in parsed.groups()]
    for i in range(b, c+1):
      squares.append((a, i))

    if not x_first:
      squares = [(b,a) for a, b in squares]
    clay.extend(squares)
  clay = np.array(list(set(clay)))
  xmin, ymin = np.min(clay, axis=0)
  xmax, ymax = np.max(clay, axis=0)
  print(ymin, ymax, xmin, xmax)

  clay_map = np.zeros([ymax+5, xmax-xmin + 3])
  offset = xmin-1
  water_source = (0,500-offset)
  clay_map[water_source] = 9
  
  for el in clay:    
    y, x = el
    clay_map[(x,y-offset)] = 1
  
  print(clay_map)
 
  sources = [water_source]
  basins = []


if __name__ == '__main__':
  begin = dt.datetime.now()
  main()
  diff_time = dt.datetime.now() - begin
  print('That took {:.3f} seconds'.format(diff_time.seconds + 1e-6*diff_time.microseconds))
