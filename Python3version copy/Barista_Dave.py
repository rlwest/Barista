import sys
import ccm
from ccm.lib.actr import *
from MotorModule import *

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
    DM.add('isa:order order:coffee')

# PRODUCTIONS
#    def START(focus='start'):
#        print ('do shit')
#        focus.set('stop')

    def START2(cup='state:empty'):
        print ('fill cup')
        #self.parent.cup.state='full'
        motor.action('cup', 'state', 'full')