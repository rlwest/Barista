import sys
import ccm
from ccm.lib.actr import *
from random import randrange, uniform

########################
##### MOTOR MODULE #####
########################

class MotorModule(ccm.Model): # defines actions in the environment
    

##### This sees the code, which is a value in the state slot of the display object
    def referee_action(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('[referee]')
        print('object=',env_object)
        print('slot=',slot_name)
        print('value=',slot_value)
