"""
name: 04c_trigger.py
type: script

How acquire (and write) data with OpenBCI.

Two processes
 * parent (main) - SSVEP stimulus display
 * child (subprocess) - data acquisition and writing

Paret process awaits for user decision: exit or quit to
terminate te program and finish both processes.

NOVUM:
type `s` to simulate stimulus appearance.
Then third column of the written data will be set to 1,
else (as default) 0 is set.

"""

import multiprocessing as mp

import pyseeg.modules.board_simple as bs


############################################
#
#  Child process
#  Acquire and write data with OpenBCI
#

channel = 0
board = bs.BoardManager()

# File to write data to.
filename = '/tmp/openbci_example_data.txt'

def data_acquisition():
    stim = '0'
    while not quit_program.is_set():
        sample = board.get_sample(channel=channel,
                                  filter=False)
        number = str(sample.id)
        data = str(sample.channel_data[0])
        if stimuli_present.is_set():
            stim = '1'
        else:
            stim = '0'
        #  print('%.3d ::: %.6f ::: %s' % (sample.id,
                                        #  sampe.channel_data[0]
                                        #  stim)

        open(filename, 'a').write(','.join([number,
                                            data,
                                            stim])+'\n')

# Multiprocessing event is a flag (a trigger).
stimuli_present = mp.Event()
quit_program = mp.Event()

# Define a process.
proc_acq = mp.Process(
    name='acquisition_',
    target=data_acquisition,
    args=()
    )

# Start defined process.
proc_acq.start()
print('A subprocess (child porcess) started')


############################################
#
#  Parent process
#  SSVEP stimuli (sinusoid controlled)
#

def switch_state(mp_event):
    if mp_event.is_set() != True:
        mp_event.set()
    else:
        mp_event.clear()

# Awaits user decision.
while not quit_program.is_set():
    print('Type \'s\' to simulate stimuli\n')
    print('Type \'exit\' or \'quit\' to terminate:\n')
    decision = raw_input()
    if decision == 's':
        switch_state(stimuli_present)
    elif decision == 'exit' or decision == 'quit':
        quit_program.set()
