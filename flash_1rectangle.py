# name: flash_1rectangle.py
# type: script

from psychopy import visual, core  
import numpy as np

############################################
#
# How to control a SSVEP stimuli with a sinusoid.
#

# Create a window.
# For configuring and debugging the code turn off full screen.
fullscr = False
win = visual.Window(
    [1200,1000],
    monitor="testMonitor",
    units="deg",
    fullscr=fullscr
    )
win.setMouseVisible(False)

# Sinusoidal control frequency.
freq = 1.5
# Color of the rectangle.
color = '#606a79'
# Position of the rectange, default 0,0 (middle of the screen).
pos = (0, 0)

start = core.getTime()
cnt = 0
while cnt<300:
    second = core.getTime() - start
    sin_val = 0.5+0.5*np.sin(
        2 * np.pi * second * float(freq)
        )
    # If you remove or comment this print, it sould work faster
    print('sec: %.4f; sin: %.4f' % (second, sin_val))
    
    rect = visual.Rect(
        win=win,
        lineColor=color, 
        fillColor=color,
        size=20,
        opacity=sin_val,
        pos=pos
        )

    rect.draw() 
    win.flip()

    cnt += 1

win.close()
