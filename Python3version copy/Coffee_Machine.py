import sys
import ccm
from ccm.lib.actr import *
from MotorModule import *

#####################
##### The Agent #####
#####################

class Coffee_Machine_Objects (ccm.Model):

### objects in the environment
    coffee_machine = ccm.Model(isa='coffee_machine', state='off')

class Coffee_Machine(ACTR):

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


    def On(coffee_machine='state:on',
           cup='state:empty'):
        motor.action('cup', 'state', 'full')