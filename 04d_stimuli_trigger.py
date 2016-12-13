"""
name: 04d_stimuli_trigger.py
type: script

How acquire (and write) data with OpenBCI.

Two processes
 * parent (main) - SSVEP stimulus display
 * child (subprocess) - data acquisition and writing

Present the stimulus and clear it after a couple of seconds.
Information about when the stimulus was present on the screen
will be passed to the child process and written to file with
the data.

"""

import numpy as np
import multiprocessing as mp
from psychopy import visual, core

import pyseeg.modules.board_simple as bs


############################################
#
#  Child process
#  Acquire and write data with OpenBCI
#

channel = 0
board = bs.BoardManager(port='/dev/ttyUSB0')

# File to write data to.
filename = '/tmp/openbci_example_data.txt'

def data_acquisition():
    stim = '0'
    while not quit_program.is_set():
        sample = board.get_sample(channel=channel)
        number = str(sample.id)
        data = str(sample.channel_data[0])
        if stimuli_present.is_set():
            stim = '1'
        else:
            stim = '0'

        # print('%.3d ::: %.6f ::: %s' % (sample.id,
                                         # sampe.channel_data[0],
                                         # stim))

        open(filename, 'a').write(','.join([number,
                                            data,
                                            stim])+'\n')

# Multiprocessing event is a flag (a trigger).
quit_program = mp.Event()
stimuli_present = mp.Event()

# Define a process.
proc_acq = mp.Process(
    name='acquisition_',
    target=data_acquisition,
    args=()
    )

# Start defined process.
proc_acq.start()
print('A subprocess (child porcess) started')

def switch_state(mp_event):
    if mp_event.is_set() != True:
        mp_event.set()
    else:
        mp_event.clear()


############################################
#
#  Parent process
#  SSVEP stimuli (sinusoid controlled)
#

# Create a window.
# For configuring and debugging the code turn off full screen.
fullscr = True
win = visual.Window(
    [1200,1000],
    monitor="testMonitor",
    units="deg",
    fullscr=fullscr
    )
win.setMouseVisible(False)

# Sinusoidal control frequency.
freq = 8
# Color of the rectangle.
color = 'red'
# Position of the rectange, default 0,0 (middle of the screen).
pos = (0, 0)

start = core.getTime()
prev_time = start
cnt = 0
stim_range = (4, 8)
stim_start, stim_end = stim_range

quit_second = 10

win.flip()

while True:
    time_in_seconds = core.getTime() - start
    sin_val = 0.5+0.5*np.sin(2 * np.pi * time_in_seconds * float(freq))

    # If you remove or comment this print, it sould work faster
    #  print('sec: %.4f; sin: %.4f' % (time_in_seconds, sin_val))
    
    rect = visual.Rect(
        win=win,
        lineColor=color, 
        fillColor=color,
        size=20,
        opacity=sin_val,
        pos=pos
        )

    # When to refresh stimuli.
    if time_in_seconds >= stim_start and time_in_seconds < stim_end:
        rect.draw()
        win.flip()

    # Setting and clearing the flag, clearing the screen after the stmuli.
    if prev_time <= stim_start and time_in_seconds > stim_start:
        stimuli_present.set()
    elif prev_time <= stim_end and time_in_seconds > stim_end:
        stimuli_present.clear()
        win.flip()

    if time_in_seconds > quit_second:
        quit_program.set()
        break


    prev_time = time_in_seconds
    cnt += 1

win.close()
board.disconnect()
