# import some libraries from PsychoPy
from psychopy import visual, core

#create a window
mywin = visual.Window([800,600], monitor="testMonitor", units="deg")

#create some stimuli
rect = visual.Rect(win=mywin, fillColor='red', lineColor='red', size=10)

#draw the stimuli and update the window
rect.draw()
mywin.update()

#pause, so you get a chance to see it!
core.wait(5.0)
