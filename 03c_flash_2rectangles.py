# name: flash_2rectangles.py
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

# Sinusoidal control version.
freq_one = 0.5
freq_two = 1.5
# Colors of the rectangles.
color_one = 'red'
color_two = 'green'
# Positions of the rectanges.
pos_one = (-7, 0)
pos_two = (7, 0)


start = core.getTime()
cnt = 0
while cnt<600:
    second = core.getTime() - start

    sin_val_one = 0.5+0.5*np.sin(2 * np.pi * second * float(freq_one))
    sin_val_two = 0.5+0.5*np.sin(2 * np.pi * second * float(freq_two))
    
    rect_one = visual.Rect(
        win=win,
        fillColor=color_one,
        lineColor=color_one, 
        size=20,
        pos=pos_one,
        opacity=sin_val_one
        )
    rect_two = visual.Rect(
        win=win,
        fillColor=color_two,
        lineColor=color_two, 
        size=20,
        pos=pos_two,
        opacity=sin_val_two
        )

    rect_one.draw()
    rect_two.draw()
    win.flip()
    cnt += 1

win.close()
