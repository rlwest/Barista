##############################
##### Lofi Cafe #####
### SGOMS production model ###
##############################

import sys
sys.path.append('/Users/robertwest/CCMSuite3-master/')

import ccm

from Barista_Dave import Barista_Dave
from Lofi_Cafe import Objects, Physics_Engine
from ccm.lib.actr import *

######## run model #########

log = ccm.log()
dave = Barista_Dave()          # name the agent
physics = Physics_Engine()
cafe = Objects()                # name the environment

cafe.agent = dave              # put the agent in the environment
cafe.agent = physics

ccm.log_everything(cafe)       # print out what happens in the environment
cafe.run()                # run the environment
ccm.finished()           # stop the environment
