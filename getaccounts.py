##########################
# PYTHON DEMO
##########################

from solidfire.factory import ElementFactory
import logging
from solidfire import common
#common.setLogLevel(logging.ERROR)

#---- CREATE CONNECTION TO SF CLUSTER ----------------------#
# ElementFactory.create(MVIP, username, password)
sf = ElementFactory.create("192.168.0.103", "admin", "NetApp123!")

#---- LIST ALL ACCOUNTS ON THE CLUSTER ----------------------#
list_accounts = sf.list_accounts()
print("DISPLAY EXISTING ACCOUNTS")
for account in list_accounts.accounts:
   print(account)



