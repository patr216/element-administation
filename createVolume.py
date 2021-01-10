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



#---- Create a volume in the account PythonIT                                  ------#
#---- The Create volume API call requires the account ID as one of the parameters ---#
#----- It also requires the qosPolicyID as a parameter                            ---#
#---- So let us  use an API call to get the account ID of the PythonFinance account ----#

account_by_name_result = sf.get_account_by_name("PythonFinance")
# get the account id value from this result
accnt_id = account_by_name_result.account.account_id

# Get all policies
# Now get the qosPolicy ID of the Policy Default (created using GUI)

qos_policy_result = sf.list_qos_policies()

for policy in qos_policy_result.qos_policies:
    if policy.name == "PythonDefault":   
        policy_id = policy.qos_policy_id
    
    # Now use these ids to create a volume
print("Creating a Volume in account with account id: %d" %accnt_id)
print("and QoS Policy ID %d" %policy_id)
print
print
create_volume_result = sf.create_volume(name="Pythonfinance-home",
                                         account_id=accnt_id,
                                         total_size = "1000000000",
                                         enable512e="False",
                                         qos_policy_id=policy_id)
print("Volume Pythonfinance-Home has been created")                                        

#---- The students can check if this new volume in the specified account and QoS policy has been created using the Element OS GUI ----#