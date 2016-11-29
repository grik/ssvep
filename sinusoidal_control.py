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
periods = float(freq ** 2)
values_axis = np.sin(2 * np.pi * np.arange(periods) / freq)
time_axis = np.arange(periods) / freq**2

plt.subplot(211)
plt.plot(values_axis)
plt.title('What happens when you will not change x-axis values')
plt.xlabel('periods [-]')
plt.ylabel('sin() value [-]')

plt.subplot(212)
plt.plot(time_axis, values_axis)
plt.title('The proper one')
plt.xlabel('time [s]')
plt.ylabel('sin() value [-]')
plt.show()


############################################
#
# Second create an universal millisecond -> sinusoid function
# value converter.
#

# Function to transform current millisecond to periodical value.
def millisecond2period(millisecond, freq):
    millisecond /= float(1000)
    period = millisecond * freq ** 2
    return period

# Getting sin value for code consistency clearness.
def get_sin_val(period, freq):
    sin_val = np.sin(2 * np.pi * period / float(freq))
    return sin_val

# Above zero - only these sin() values will be stored here.
above_zero = []
# Do up to 1000th millisecond, works for (1000, 2000) as well, etc.
for i in range(1000):
    period = millisecond2period(i, freq)
    sin_val = get_sin_val(period, freq)
    if sin_val >= 0:
        above_zero.append(sin_val)
    else:
        above_zero.append(0)

plt.plot(above_zero)
plt.ylim(-1, 1)
plt.xlabel('time [ms]')
plt.ylabel('sin() value [-]')
plt.show()
