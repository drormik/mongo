import pymongo

# This script tests python is able to access a MongoDB cluster using SRV Connection string.
# the script requires to install:

# a.  pip install pymongo
# b.  pip install dnspython (this should automatically be installed when installing pymongo)
# c.  pip install srvlookup

# if neither dnspython nor srvlookup are able to find the SRV records, then either the current python environment has an issue reading SRV records from the DNS 
#    (this happens when the python environment becaomes corrupt), OR  the current host (where the python script is running) doesnt have access to the DNS server
#       OR  the SRV records do not exist in the DNS
# 

#  Assign the relevant values to <user>, <pass> and  <cluster_address> 

user= test
pass= test
cluster_address = host.net.com

conn_str = "mongodb+srv://"+user+":"+pass+"@""+cluster_address+"?retryWrites=true&w=majority"
# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
try:
    print(client.server_info())
    print("connected successfully")
except Exception:
    print("Unable to connect to the server.")


import srvlookup

services = srvlookup.lookup("mongodb", domain=cluster_address)

for each_host in services:
    print(each_host.host)

