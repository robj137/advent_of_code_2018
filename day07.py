import re
import string
import copy
import datetime as dt

def main():
  instructions = []
  with open('inputs/day7.txt') as f:
    for line in f:
      instructions.append(re.search('Step (\w) must be finished before step (\w) can begin', line.strip()).groups())

  dependency_dict = {x:[] for x in string.ascii_uppercase}
  for instruction in instructions:
    req = instruction[0]
    dep = instruction[1]
    dependency_dict[dep].append(req)
  time1 = process(copy.deepcopy(dependency_dict), 1)
  time2 = process(copy.deepcopy(dependency_dict), 5)
  print('Part a: It takes {} seconds to process with {} worker(s)'.format(time1, 1))
  print('Part b: It takes {} seconds to process with {} worker(s)'.format(time2, 5))

def get_thread():
  thread = {}
  thread['time_left'] = 0
  thread['processing'] = None
  return thread

def process_dict(dependency_dict, queue, finished):
  for step in finished:
    for key in sorted(dependency_dict.keys()):
      if step in dependency_dict[key]:
        dependency_dict[key].pop(dependency_dict[key].index(step))
  for key in sorted(dependency_dict.keys()):
    if len(dependency_dict[key]) == 0:
      queue.append(key)
      del dependency_dict[key]
  queue.sort()
  queue.reverse()

def process(dependency_dict, n_threads = 1):
  threads = [get_thread() for x in range(n_threads)]
  queue = []
  finished = []

  time = 0
  while len(finished) < 26:
    time += 1
    for thread in threads:
      if thread['time_left'] == 1:
        finished.append(thread['processing'])
        thread['processing'] = None
      if thread['time_left'] > 0:
        thread['time_left'] -= 1
    process_dict(dependency_dict, queue, finished)
    for thread in threads:
      if not thread['processing']:
        if queue:
          step = queue.pop()
          thread['processing'] = step
          thread['time_left'] = 60 + ord(step) - 64
    # check for worker availability (and decrement their time as needed)
    # as lettesr get finished, adjust the dependency dict and add any newly opened letters to the
    # queue
  return time-1

if __name__ == '__main__':
  begin = dt.datetime.now()
  main()
  diff_time = dt.datetime.now() - begin
  print('That took {:.3f} seconds'.format(diff_time.seconds + 1e-6*diff_time.microseconds))
