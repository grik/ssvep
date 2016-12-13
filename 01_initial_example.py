"""
name: 01_initial_example.py
type: script

A basic example of the stimuli generated with PsychoPy.

"""

# Import some libraries from PsychoPy.
from psychopy import visual, core

# Create a window.
mywin = visual.Window([800,600], monitor="testMonitor", units="deg")

# Create some stimuli.
grating = visual.GratingStim(win=mywin, mask="circle", size=3, pos=[-4,0], sf=3)
fixation = visual.GratingStim(win=mywin, size=0.5, pos=[0,0], sf=0, rgb=-1)

# Draw the stimuli and update the window.
grating.draw()
fixation.draw()
mywin.update()

# Pause, so you get a chance to see it!
core.wait(5.0)
