import sys
import ccm
from MotorModule import *
from ccm.lib.actr import *

#####################
##### The Agent #####
#####################

class Barista_Dave(ACTR):

# BUFFERS
    focus=Buffer()
    b_DM = Buffer()
    b_motor = Buffer()
    b_visual = Buffer()

# MODULES
    motor = MotorModule(b_motor)
    DM = Memory(b_DM)

# INITIAL SETTINGS
    focus.set('start')
    DM.add('isa:coffee')

# PRODUCTIONS
    def START(focus='start'):
        print ('do shit')

