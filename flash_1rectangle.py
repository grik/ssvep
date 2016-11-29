# name: flash.py
# type: script

from psychopy import visual, core  
import numpy as np
import matplotlib.pyplot as plt

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

# Create some stimuli.
rect = visual.Rect(
    win=win,
    fillColor='red',
    lineColor='red',
    size=20
    )

# Sinusoidal control version.
freq = 14

def second2period(second, freq):
    period = second * freq ** 2
    return period

# Getting sin value for code consistency clearness.
def get_sin_val(period, freq):
    sin_val = np.sin(2 * np.pi * period / float(freq))
    return sin_val

start = core.getTime()
cnt = 0
while cnt<150:
    second = core.getTime() - start
    print(second)
    period = second2period(second, freq)
    sin_val = get_sin_val(period, freq)
    if sin_val >= 0:
        rect.draw()
    win.flip()
    cnt += 1

win.close()
