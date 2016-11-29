# name: flash_1rectangle.py
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

# Sinusoidal control frequency.
freq = 15

start = core.getTime()
cnt = 0
while cnt<150:
    second = core.getTime() - start
    sin_val = np.sin(2 * np.pi * second * float(freq))
    
    rect = visual.Rect(
        win=win,
        fillColor=[sin_val, 0, 0],
        lineColor=[sin_val, 0, 0],
        size=20
        )

    if sin_val >= 0:
        rect.draw() 
    win.flip()
    cnt += 1

win.close()
