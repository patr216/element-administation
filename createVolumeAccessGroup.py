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

# To create a Volume Access Group, we need a Volume ID and Initiator name
# Here We will create the VAG without the initiator
# We will add the initiator in the next module

#---- First, we will get the Volume ID of the volume that will be added to the Volume access group ---#
#-----We will add this id to a list   -----#
volume_exists = False
list_volumes_result = sf.list_volumes()
for volume in list_volumes_result.volumes:
    if volume.name == "Pythonfinance-home":
        volume_id = volume.volume_id
        volume_ids = [volume_id]# At this time we are adding only one volume to the list of volume ids
        volume_exists = True
        
if volume_exists:
    print
    print (" ---Creating a Volume Access Group with name PythonEng-AG ---------------- ")
    print (" --- Volume ID %d is added into this Volume Access Group---" %volume_id )
    print(" ----An initiator will be added later---")
    print
    print
    volume_access_group_result = sf.create_volume_access_group(name="PythonEng-AG",
                                                           #initiators:windows_initiator_name,- we will add this in another script
                                                           volumes=volume_ids) 
   
    print (" ------------- Volume Access Group has been created ---------")
   
else:
    print
    print ("Volume Access Group could not be created for volume Pythonfinance-home sincethe volume does not exists")
    print





