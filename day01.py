import datetime as dt

def main():
  in_file = open('inputs/day1.txt')
  shifts = []
  for line in in_file:
    shifts.append(int(line.strip()))
  print('The frequency shifts end at {}'.format(sum(shifts)))
  
  current_frequency = 0
  dupes = {}
  dupes[current_frequency] = 0
  dupe = False
  
  while not dupe:
    for shift in shifts:
      current_frequency += shift
      if current_frequency not in dupes:
        dupes[current_frequency] = 0
      else:
        dupe = True
        print('Found duplicated frequency at {}'.format(current_frequency))
        return

if __name__ == '__main__':
  begin = dt.datetime.now()
  main()
  diff_time = dt.datetime.now() - begin
  print('That took {:.3f} seconds'.format(diff_time.seconds + 1e-6*diff_time.microseconds))
