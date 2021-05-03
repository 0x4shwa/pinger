
import os
hostname = input("enter website ===> ")
response = os.system("ping -c 1 " + hostname)

#and then check the response..
if response == 0:
  print ("host is up :<| ")
else:
  print ("hostnameis down! lol ;/ ")
