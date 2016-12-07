# name: 04a_data_acquisition.py
# type: script

import pyseeg.modules.board_simple as bs

############################################
#
# How acquire (and write) data with OpenBCI.
#

channel = 0
board = bs.BoardManager()

# File to write data to.
filename = '/tmp/openbci_example_data.txt'

for i in range(2500):
    sample = board.get_sample(channel=channel, filter=False)
    number = str(sample.id)
    data = str(sample.channel_data[0])
    # print('%.3d ::: %s' % (id, sample))

    open(filename, 'a').write(','.join([number, data])+'\n')

board.disconnect()
print('Disconnected')
