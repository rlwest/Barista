##############################
##### Lofi Cafe #####
### SGOMS production model ###
##############################

import sys
sys.path.append('/Users/robertwest/pythonACTR3-master/')

import ccm
from ccm.lib.actr import *

from Barista_Dave import Barista_Dave
from Coffee_Machine import Coffee_Machine

from Lofi_Cafe import Objects
from Coffee_Machine import Coffee_Machine_Objects
C = type('C', (Objects,Coffee_Machine_Objects), dict(c='c'))

######## run model #########

log = ccm.log()
dave = Barista_Dave()          # name the agent
coffee_machine = Coffee_Machine()
#cafe = Objects()                # name the environment
cafe = C()                # name the environment


cafe.agent = dave              # put the agent in the environment
cafe.agent = coffee_machine 


ccm.log_everything(cafe)       # print out what happens in the environment
cafe.run()                # run the environment
ccm.finished()           # stop the environment
