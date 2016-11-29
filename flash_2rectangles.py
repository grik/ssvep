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
rect_one = visual.Rect(
    win=win,
    fillColor='red',
    lineColor='red',
    size=20,
    pos=(-7, 0)
    )
rect_two = visual.Rect(
    win=win,
    fillColor='blue',
    lineColor='blue',
    size=20,
    pos=(7, 0)
    )

# Sinusoidal control version.
freq_one = 7
freq_two = 14

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
    period_one = second2period(second, freq_one)
    period_two = second2period(second, freq_two)
    sin_one_val = get_sin_val(period_one, freq_one)
    sin_two_val = get_sin_val(period_two, freq_two)
    if sin_one_val >= 0:
        rect_one.draw()
    if sin_two_val >= 0:
        rect_two.draw()
    win.flip()
    cnt += 1

win.close()
