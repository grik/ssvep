"""
name: 04b_two_threads.py
type: script

How acquire (and write) data with OpenBCI.

Two processes
 * parent (main) - SSVEP stimulus display
 * child (subprocess) - data acquisition and writing

Paret process awaits for user decision: exit or quit to
terminate te program and finish both processes.

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
    while not quit_program.is_set():
        sample = board.get_sample(channel=channel, filter=False)
        number = str(sample.id)
        data = str(sample.channel_data[0])
        # print('%.3d ::: %s' % (sample.id, sample.channel_data[0]))

        open(filename, 'a').write(','.join([number,
                                            data])+'\n')

# Multiprocessing event is a flag (a trigger).
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

# Awaits user decision.
while not quit_program.is_set():
    print('Type \'exit\' or \'quit\' to terminate:\n')
    decision = raw_input()
    if decision == 'exit' or decision == 'quit':
        quit_program.set()
