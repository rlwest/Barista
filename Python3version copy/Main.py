##############################
##### Lofi Cafe #####
### SGOMS production model ###
##############################

import sys
sys.path.append('/Users/robertwest/CCMSuite3-master/')

import ccm
from ccm.lib.actr import *

from Barista_Dave import Barista_Dave
from Lofi_Cafe import Objects

######## run model #########

log = ccm.log()
dave = Barista_Dave()          # name the agent
cafe = Objects()                # name the environment

cafe.agent = dave              # put the agent in the environment


ccm.log_everything(cafe)       # print out what happens in the environment
cafe.run()                # run the environment
ccm.finished()           # stop the environment
