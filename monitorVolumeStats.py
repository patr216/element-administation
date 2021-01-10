##########################
# PYTHON DEMO
##########################

from solidfire.factory import ElementFactory
import logging
from solidfire import common
common.setLogLevel(logging.ERROR)
from solidfire.models import QoS
import time


#---- CREATE CONNECTION TO SF CLUSTER ----------------------#
# ElementFactory.create(MVIP, username, password)
sf = ElementFactory.create("192.168.0.103", "admin", "NetApp123!")


#----- Get the QoS policy attached to the volume--------#
#------ Here I am hardcoding the volume name but it can be obtained as a user input as well ----#

#---- First, we will get the Volume ID of the volume---#

vol_name_to_lookup = "Pythonfinance-home"
volume_exists = False
list_volumes_result = sf.list_volumes()
for volume in list_volumes_result.volumes:
    if volume.name == vol_name_to_lookup:
        volume_id = volume.volume_id # get the volume id for later use.
        
        qos_object = volume.qos # get the QoS Object attached to the Volume
        qos_id = volume.qos_policy_id # we need the id for later use when we modify the QoS Policy
        max_iops = qos_object.max_iops # Obtain the max_iops from the qos policy for the volume
        print (" ----Max IOPS in the QoSPolicy attached to the volume is -----")
        print (max_iops)
        print
        print
        volume_exists = True
if(not volume_exists):
 print("The volume Pythonfinance-home does not exist. EXITING now")
 exit


qos_max_iops_step_down = 1000 # This is to adjust the MAX IOPs in the QoS Policy 
new_max_iops = max_iops
qos_can_be_modified = True

while(qos_can_be_modified):
    get_volume_stats_result = sf.get_volume_stats(volume_id) # get the stats for the volume
    print
    print(" ----Actual IOPS for the volume Pythonfinance-home is  -----")
    actual_iops = get_volume_stats_result.volume_stats.actual_iops # retrieve the actual IOPS for the volume
    print(actual_iops)
    
    if (actual_iops < (max_iops - ((10/100)*max_iops))): # checking if the actual IOPS on the volume is below the max_iops
        collecting_samples=True
        samples = []

        sample_count = 0
        while (sample_count < 12): # collect samples for 12 cycles with a 5 second delay
            print ("---- Collecting data for actual IOPS every 5 seconds for 60 seconds------")
            get_volume_stats_result = sf.get_volume_stats(volume_id)
            actual_iops = get_volume_stats_result.volume_stats.actual_iops
            print (" Actual IOPS %d" %actual_iops)
            samples.append(actual_iops)
            sample_count = sample_count+1
            time.sleep(5)

        
        # calculate the average of the samples collected
        total_iops = 0
        for sample in samples:
            total_iops = total_iops + sample
        average_iops = total_iops/12
        print("-----Average IOPS in the past 60 seconds = %d" % average_iops)
        
        
        if (average_iops <(max_iops + ((10/100)*max_iops))): #the max in qos policy should be close to the average 
            
            new_max_iops = new_max_iops - qos_max_iops_step_down # bring it down by 1000

            # Test if you should change QoS to this new_max_iops will
            if new_max_iops >= average_iops:
                print("Automatically adjusting the QoS Policy to have a smaller MAX IOPS and BURST IOPS by decrementing Max IOPS by 1000")
                a_new_qos_object = QoS(50,new_max_iops ,new_max_iops+1000)
                a_new_qos_policy_result = sf.modify_qos_policy(qos_policy_id=qos_id,qos=a_new_qos_object)
                print("New MAX IOPS set to %d and new Burst IOPS set to" %new_max_iops,new_max_iops+1000)
            else:
                qos_can_be_modified = False
    else:
           qos_can_be_modified = False

if(not qos_can_be_modified):
    print("There is no need to change the QoS Policy. The current QoS policy is adequate for your workload")
    print("QoS Policy of the volume has MAX IOPS set to %d and Burst IOPS set to" %new_max_iops,new_max_iops+1000)
    print
    
                  