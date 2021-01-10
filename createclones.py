##########################
# PYTHON DEMO
##########################

from solidfire.factory import ElementFactory

#---- CREATE CONNECTION TO SF CLUSTER ----------------------#
# ElementFactory.create(MVIP, username, password)
sf = ElementFactory.create("192.168.0.103", "admin", "NetApp123!")

listofvols = sf.list_volumes(volume_name = "Eng-DB")
for vol in listofvols.volumes:
   db_vol_id = vol.volume_id

clonename_base = vol.name + "-clone"
print(db_vol_id)
# range(start,stop), to increase number of clones change stop value
for volnum in range(1,2):
   clonename = clonename_base + str(volnum)

   print("Create clone:" + clonename)
   clone_result = sf.clone_volume(volume_id=db_vol_id, name=clonename)
   # wait for clone creation to finish before creating next clode
   my_async_handle = clone_result.async_handle
   async_result = sf.get_async_result(async_handle=my_async_handle, keep_result=True)
   while(async_result['status'] == 'running'):
       async_result = sf.get_async_result(async_handle=my_async_handle, keep_result=True)
