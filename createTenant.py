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

#---- LIST ALL ACCOUNTS ON THE CLUSTER BEFORE WE ADD ANOTHER ACCOUNT----------------------#
list_accounts = sf.list_accounts()
print("--------DISPLAY EXISTING ACCOUNTS BEFORE CREATING A NEW ACCOUNT --------")

for account in list_accounts.accounts:
   print(account)

print
print

#---- ADD ANOTHER ACCOUNT                                                  ----#
#---- Add a new account with username "PythonIT" only if it does not exist ----#
#---- If it exists, skip this step                                         ----#
accnt_exists = False
for account in list_accounts.accounts:
   if account.username == "PythonIT":
      accnt_exists = True
      print("An account with username PythonIT already exists")
      print ("This account was not added again")
      print

if not accnt_exists:
    add_account = sf.add_account(username = "PythonIT")
    print("A new account with username PythonIT was added")
    print
    print


#---- LIST ALL ACCOUNTS ON THE CLUSTER AFTER WE HAVE ADDED ANOTHER ACCOUNT USING PYTHON CODE----------------------#
list_accounts = sf.list_accounts()
print("--------DISPLAY OF ACCOUNTS AFTER ADDING THE NEW ACCOUNT PythonIT--------")
for account in list_accounts.accounts:
   print(account)
print
print

#---- DELETE THIS NEWLY ADDED ACCOUNT-----------------------------------------------------------------------------------#
# We will use the RemoveAccount API. But this API requires an Account ID as a parameter to remove a specified Account---#
# So we will first use the API GetAccountByName and retrieve the Account with username PythonIT.                    ----#
# The response to this API call will contain the ID of the account.                                                  ---#
# We will use this ID in RemoveAccount API call to delete the account                                               ---#
accnt_exists = False
list_accounts_result = sf.list_accounts()
for account in list_accounts_result.accounts: 
   if account.username == "PythonIT":
      accnt_exists = True
      accnt_id  = account.account_id

if accnt_exists:
   remove_account = sf.remove_account(accnt_id)
   print("The account with username PythonIT was deleted")
else:
   print("The account with username PythonIT cannot be deleted since it does not exist")
      
print
print

#---- LIST ALL ACCOUNTS ON THE CLUSTER AFTER WE HAVE REMOVED THE ACCOUNT----------------------#
list_accounts = sf.list_accounts()
print("--------FINAL DISPLAY OF ACCOUNTS AFTER REMOVING THE NEW ACCOUNT PythonIT THAT WAS PREVIOUSLY ADDED--------")
for account in list_accounts.accounts:
   print(account)
print
print

#----- Exercise for the students                             -----------#
#----- Add the block of code to create PythonFinance Account -----------#






