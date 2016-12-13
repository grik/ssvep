"""
name: 05a_spectrogram_and_stimuli.py
type: script

How acquire (and write) data with OpenBCI.

Two processes
 * parent (main) - SSVEP stimulus display
 * child (subprocess) - data acquisition and writing

Present the stimulus and clear it after a couple of seconds.
Information about when the stimulus was present on the screen
will be passed to the child process and written to file with
the data.

"""

import numpy as np
import matplotlib.pyplot as plt

import pyseeg.modules.spectrogram as sg


# Sampling frequncy.
fs = 256

# File to read the data from.
filename = '/tmp/openbci_example_data.txt'

data = np.loadtxt(filename, delimiter=',')
# First are sample ids which we are not interesed in.
_, data, stim = data.T


############################################
#
#    Spectrogram
#

plt.subplot(211)
plt.xlabel('time [s]')
plt.ylabel('frequency [Hz]')
plt.xlim(0, data.shape[0])
sg.spectrogram(data, fs, show_plot=False)


############################################
#
#    Stimulus
#

plt.subplot(212)
plt.xlabel('time [s]')
plt.ylabel('stimulus [-]')
plt.plot(np.arange(stim.shape[0])/fs, stim,
         linewidth=2.0, color='r')
plt.xlim(0, stim.shape[0]/256)
plt.ylim(-0.1, 1.1)

# Title for whole figure.
plt.suptitle('Spectrogram and stimulus timecourse')

plt.show()
