##########################
# PYTHON DEMO
##########################

from solidfire.factory import ElementFactory
import logging
from solidfire import common
common.setLogLevel(logging.ERROR)

#---- CREATE CONNECTION TO SF CLUSTER ----------------------#
# ElementFactory.create(MVIP, username, password)
sf = ElementFactory.create("192.168.0.103", "admin", "NetApp123!")

show_more_faults = False
first_pass = True

# Go into the loop atleast once
while(show_more_faults or first_pass):
  
#---- LIST ALL Faults IN THE CLUSTER----------------------#
   list_cluster_faults_result = sf.list_cluster_faults()

   print("--------SHOWING ALL CURRENT FAULTS IN THE SYSTEM--------")

   for fault in list_cluster_faults_result.faults:
      print(fault)
      print("-----------")

   first_pass = False
   # use input when using python 3
   key = input("press Enter to continue or s followed by Enter to stop")
   if key == 's':
      break
   else:
      show_more_faults = True

