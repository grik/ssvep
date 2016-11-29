# name: flash_2rectangles.py
# type: script

from psychopy import visual, core  
import numpy as np

############################################
#
# How to control a SSVEP stimuli with a sinusoid.
#

# Create a window.
win = visual.Window(
    [1200,1000],
    monitor="testMonitor",
    units="deg"
    )

# Sinusoidal control version.
freq_one = 12
freq_two = 20


start = core.getTime()
cnt = 0
while cnt<150:
    second = core.getTime() - start

    sin_val_one = 0.5+0.5*np.sin(2 * np.pi * second * float(freq_one))
    print(sin_val_one)
    sin_val_two = 0.5+0.5*np.sin(2 * np.pi * second * float(freq_two))
    
    rect_one = visual.Rect(
        win=win,
        fillColor='red',
        lineColor='red',
        size=20,
        pos=(-7, 0),
        opacity=sin_val_one
        )
    rect_two = visual.Rect(
        win=win,
        fillColor='blue',
        lineColor='blue',
        size=20,
        pos=(7, 0),
        opacity=sin_val_two
        )

    if sin_val_one >= 0:
        rect_one.draw()
    if sin_val_two >= 0:
        rect_two.draw()
    win.flip()
    cnt += 1

win.close()
