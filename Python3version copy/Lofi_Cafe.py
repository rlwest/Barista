

import sys
import ccm
from MotorModule import *
from ccm.lib.actr import *
from random import randrange, uniform


class Objects (ccm.Model):

### objects in the environment
    response = ccm.Model(isa='response', state='state')
    display = ccm.Model(isa='diplay', state='RP')
    response_entered = ccm.Model(isa='response_entered', state='no')
    vision_finst = ccm.Model(isa='motor_finst', state='re_set')

class Physics_Engine(ccm.Model): # defines actions in the environment
    
    def referee_action(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('[referee]')
        print('object=',env_object)
        print('slot=',slot_name)
        print('value=',slot_value)
