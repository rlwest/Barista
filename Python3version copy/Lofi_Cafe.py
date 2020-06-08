

import sys
import ccm
from MotorModule import *
from ccm.lib.actr import *
from random import randrange, uniform


class Objects (ccm.Model):

### objects in the environment
    cup = ccm.Model(isa='cup', state='empty')

class Physics_Engine(ccm.Model): # defines actions in the environment
    
    def referee_action(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('[referee]')
        print('object=',env_object)
        print('slot=',slot_name)
        print('value=',slot_value)
