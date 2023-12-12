import os
import re
import sys

ip = sys.argv[-1]
response2 = os.popen("ping -c 1 " + ip).read()

x = re.search(r'(ttl).\d+', response2)

#ttl=128
systemOS = x.group()

#128
cutNumber = re.search('\d+', systemOS)
print("TTL: ", cutNumber.group())

result = cutNumber.group()
result = int(result)

if result < 65:
	print("Host is Linux")
	
elif result > 120:
	print("Host is Windows")
