# name: sinusoidal_control.py
# type: script

import numpy as np
import matplotlib.pyplot as plt

############################################
#
# How to understand sinusoidal control of the SSVEP stimuli.
#


############################################
#
# First create an "offline" sinusoid.
#
freq = 14
# e.g. 1 second, i.e. 1000 ms
samples = 1000
time_axis = np.arange(samples)
# Get milliseconds.
time_axis = time_axis / float(1000)
values_axis = np.sin(2 * np.pi * time_axis * freq)

plt.subplot(211)
plt.plot(values_axis)
plt.title('Unscaled version')
plt.xlabel('time [ms]')
plt.ylabel('sin() value [-]')

plt.subplot(212)
plt.plot(time_axis, values_axis)
plt.title('As a function of seconds (with millisecond timepoints)')
plt.xlabel('time [s]')
plt.ylabel('sin() value [-]')
plt.show()


############################################
#
# Second create an universal millisecond -> sinusoid function
# value converter. A simulation of an experimental condions.
#


# Sinus values log.
sin_values = []
# Above zero - only these sin() values will be stored here.
above_zero = []
# Do up to 1000th millisecond, works for (1000, 2000) as well, etc.
for time in range(1000):
    # Get milliseconds.
    time /= float(1000)
    sin_val = np.sin(2 * np.pi * time * float(freq))
    print(sin_val)
    sin_values.append(sin_val)

    if sin_val >= 0:
        above_zero.append(sin_val)
    else:
        above_zero.append(0)
sin_values = 0.5 + np.array(sin_values) * 0.5


plt.subplot(211)
plt.plot(above_zero)
plt.ylim(-1, 1)
plt.title('Above zero')
plt.xlabel('time [ms]')
plt.ylabel('sin() value [-]')

plt.subplot(212)
plt.plot(sin_values)
plt.ylim(-1, 1)
plt.title('Scaled to (0.0, 1.0) range, for e.g. transparency')
plt.xlabel('time [ms]')
plt.ylabel('sin() value [-]')

plt.show()
