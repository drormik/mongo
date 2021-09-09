import pymongo

#set <user>, <pass> and  <cluster_address> to the relevant values

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
from json import dumps

services = srvlookup.lookup("mongodb", domain=cluster_address)

for each_host in services:
    print(each_host.host)

