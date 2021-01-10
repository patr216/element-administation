##########################
# PYTHON DEMO
##########################

from solidfire.factory import ElementFactory
import logging
from solidfire import common

#from solidfire.custom.models import TimeIntervalFrequency
from solidfire.models import QoS

#common.setLogLevel(logging.ERROR)

#---- CREATE CONNECTION TO SF CLUSTER ----------------------#
# ElementFactory.create(MVIP, username, password)
sf = ElementFactory.create("192.168.0.103", "admin", "NetApp123!")



#---- Create a QoSPolicy with name = PythonDefault only if it does not already exist   ---#
#---- Students can use POSTMAN Client to quickly check if the user exists.             ---#
#---- If it does, then they can use POSTMAN Client to delete                           ---#
#---- The APIs to use are ListQoSPolicies and DeleteQoSPolicy under Volumes group      ---#
# ---- Once the above steps are completed, you can now add the QoSPolicy               ---#
# ---- with name = PythonDefault                                                    ---#

qos_name = "PythonDefault"
qos_object = QoS(50,15000,15000)
qos_policy_result = sf.create_qos_policy(qos_name,qos_object)

#---- The students can check if this new QoS policy has been created using the Element OS GUI ----#