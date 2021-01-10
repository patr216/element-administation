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

#---- Get Cluster Information----------------------#
cluster_info_result = sf.get_cluster_info()
print("--------Cluster Information--------")
print(cluster_info_result)
print("--------END OF Cluster Information--------")
print
print
   

#---- List all nodes in the cluster----------------------#
cluster_nodes_result = sf.list_all_nodes()
print("--------Cluster Nodes Information--------")
print(cluster_nodes_result)
print("--------END OF Cluster Nodes Information--------")
print
print

#---- Get NTP Information----------------------#
ntp_info_result = sf.get_ntp_info()
print("--------Cluster NTP Information--------")
print(ntp_info_result)
print("--------END OF Cluster NTP Information--------")
print
print