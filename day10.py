import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
import re
import datetime as dt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(10,2))
ax.set_xlim((0,1))
ax.set_ylim((0,1))

chart, = ax.plot([], [], 'b.')

def animate(step, *fargs):
  df = fargs[0]
  update_df(df,step)
  x = np.array(df['x'])
  y = np.array(df['y'])
  chart.set_data(x,y)
  ax.set_xlim(np.min(x), np.max(x))
  ax.set_ylim(np.min(y), np.max(y))
  ax.set_title('step {}'.format(step))
  update_df(df, -step)
  return (chart,)


def get_bounding_box_area(df, step_count):
  update_df(df,step_count)
  area = (df.x.max() - df.x.min()) * (df.y.max()-df.y.min())
  update_df(df, -step_count)
  return area

def find_minimum_box_step(df):
  #simple assumptions, let's assume 
  # v = \frac{dx}{dt} => dt = \frac{dx}{v}
  # constant velocity, so dt = \delta t, dx = \delta x
  # so a first guess at how many steps it'll take is
  n_steps_x = (df['x'] / df['v_x']).mean()
  n_steps_y = (df['y'] / df['v_y']).mean()
  step_guess = np.abs(int(np.mean([n_steps_x, n_steps_y])))
  steps = [step_guess + x for x in range(-5,6)]
  areas = [get_bounding_box_area(df, step) for step in steps]
  if np.argmin(areas) not in [0, len(areas)]:
    #success!
    return steps[np.argmin(areas)]

def update_df(df, n_times =1):
  df['x'] = df['x'] + n_times*df['v_x']
  df['y'] = df['y'] + n_times*df['v_y']

def parse_coords(capture):
  position = [int(x) for x in capture[0].split(',')]
  velocity = [int(x) for x in capture[1].split(',')]
  return {'x':position[0], 'y':-position[1], 'v_x':velocity[0], 'v_y':-velocity[1]}


def main():
  coords = []
  with open('inputs/day10.txt') as f:
    for line in f:
      capture = re.search('position=<(.*)> velocity=<(.*)>', line.strip()).groups()
      coords.append(parse_coords(capture))
  df = pd.DataFrame(coords)
  step_guess = find_minimum_box_step(df)
  anim = FuncAnimation(fig, animate, fargs=[df], frames = np.arange(step_guess-5, step_guess+5), interval=2000)
  plt.show()
  #LRCXFXRP

if __name__ == '__main__':
  main()
