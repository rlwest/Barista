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

# get objects
from Objects import Objects
from Coffee_Machine import Coffee_Machine_Objects

# assemble objects into environment 
Lofi_Cafe = type('Lofi_Cafe', (Objects,Coffee_Machine_Objects), dict(lofi='lofi'))

######## run model #########

#log = ccm.log()
dave = Barista_Dave()
coffee_machine = Coffee_Machine()
lofi_cafe = Lofi_Cafe()


lofi_cafe.agent = dave
lofi_cafe.agent = coffee_machine 


ccm.log_everything(lofi_cafe)
lofi_cafe.run()
ccm.finished()

