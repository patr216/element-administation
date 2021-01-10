##########################
# PYTHON SCRIPT USING APIs
##########################

from solidfire.factory import ElementFactory
import logging
from solidfire import common
common.setLogLevel(logging.ERROR)

#---- CREATE CONNECTION TO SF CLUSTER ----------------------#
# ElementFactory.create(MVIP, username, password)
sf = ElementFactory.create("192.168.0.103", "admin", "NetApp123!")

#---- Get Drives Information----------------------#
drives_result = sf.list_drives()
print("--------Drive Information--------")
print(drives_result)
print("--------END OF Drives Information--------")
print
print
   

