##############################
##### Lofi Cafe #####
### SGOMS production model ###
##############################

import sys
sys.path.append('/Users/robertwest/pythonACTR3-master/')

import ccm
from ccm.lib.actr import *

# get environment elements
from Objects import Objects
from Coffee_Machine import Coffee_Machine_Objects

# put objects together
Lofi_Cafe = type('Lofi_Cafe', (Objects,Coffee_Machine_Objects), dict(lofi='lofi'))

# create environment
lofi_cafe = Lofi_Cafe()

# get agent descriptions
from Barista_Dave import Barista_Dave
from Coffee_Machine import Coffee_Machine

# create agents for environment
dave = Barista_Dave()
coffee_machine = Coffee_Machine()

# put agents into environment
lofi_cafe.agent = dave
lofi_cafe.agent = coffee_machine 

# run
ccm.log_everything(lofi_cafe)
lofi_cafe.run()
ccm.finished()

