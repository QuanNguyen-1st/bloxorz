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
for i in range (1, 34):
    level = str(i)
    if len(level) < 2:
        level = "0" + level
    # cmd = string + " " + level + " " + algorithm
    x = subprocess.check_output(['python', 'testrun.py', level, algorithm])
    holder, time_run, memory_run, steps_run, virtual_steps_run = x.decode().split(' ')
    # print(float(time_run))
    # print(float(memory_run))
    levels.append(level)
    time.append(float(time_run))
    memory.append(float(memory_run))
    steps.append(int(steps_run))
    virtual_steps.append(int(virtual_steps_run))

print(virtual_steps)

data = {
    'level':levels,
    'time(s)':time,
    'memory(mb)':memory,
    'steps':steps,
    'virtual_steps':virtual_steps
}
df = pd.DataFrame(data)
path = "result/result_" + algorithm + ".xlsx"
df.to_excel(path, index = False)
