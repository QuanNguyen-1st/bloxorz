import os
import pandas as pd
import subprocess
import time

algorithm = "mcts"
levels = []
time = []
memory = []
steps = []
virtual_steps = []
# path = "result/result_" + algorithm + ".xlsx"
# input = pd.read_excel(path)
for i in range (15,16):
    level = str(i)
    if len(level) < 2:
        level = "0" + level
    # cmd = string + " " + level + " " + algorithm
    x = subprocess.check_output(['python', 'testrun.py', level, algorithm])
    print(x)
    # holder, time_run, memory_run, steps_run, virtual_steps_run = x.decode().split(' ')
    # # print(float(time_run))
    # # print(float(memory_run))
    # levels.append(level)
    # time.append(float(time_run))
    # memory.append(float(memory_run))
    # steps.append(int(steps_run))
    # virtual_steps.append(int(virtual_steps_run))

# data = {
#     'level':levels,
#     'time(s)':time,
#     'memory(mb)':memory,
#     'steps':steps,
#     'virtual_steps':virtual_steps
# }
# df = pd.DataFrame(data)
# df = pd.concat([input, df])
# df.to_excel(path, index = False)
