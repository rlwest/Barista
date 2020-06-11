

import sys
import ccm
from MotorModule import *
from ccm.lib.actr import *
from random import randrange, uniform


class Objects (ccm.Model):

### objects in the environment
    cup = ccm.Model(isa='cup', state='empty')


