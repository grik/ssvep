"""
name: 02_rect_example.py
type: script

Slightly different example: create, draw and expose a rectangle.

"""

# Import some libraries from PsychoPy.
from psychopy import visual, core

# Create a window.
mywin = visual.Window([800,600], monitor="testMonitor", units="deg")

# Create some stimuli.
rect = visual.Rect(win=mywin, fillColor='red', lineColor='red', size=10)

# Draw the stimuli and update the window.
rect.draw()
mywin.update()

# Pause, so you get a chance to see it!
core.wait(5.0)
