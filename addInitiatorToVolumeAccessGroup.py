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

# We have already created a Volume Access Group called PythonEng-AG
# Here we will retrieve the VAG and add the initiator to it

windows_initiator_name = "iqn.1991-05.com.microsoft:jumphost.demo.netapp.com"

list_volume_access_groups_result = sf.list_volume_access_groups()
for volume_access_group in list_volume_access_groups_result.volume_access_groups:
    if volume_access_group.name == "PythonEng-AG":
        vag_id = volume_access_group.volume_access_group_id
        vag_initiators = [windows_initiator_name]
        add_initiator_result = sf.add_initiators_to_volume_access_group(vag_id,vag_initiators)
        print
        print("------ The Windows initiator has been added to the Volume Access Group PythonEng-AG---")
        print ("---- The initiator iqn is iqn.1991-05.com.microsoft:jumphost.demo.netapp.com ---")
        print
    else:
        print
        print("------ The the Volume Access Group PythonEng-AG does not exist and so the initiator was not added---")
        print 
                                                                       
        







