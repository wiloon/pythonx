import os
import sys

f = open("/root/tmp/ip.txt", "r")
lines = f.readlines()

print(len(lines))

for line in lines:
    line = line.strip()
    command = "ansible '" + line + "' -m shell -a 'systemctl start filebeat'"
    print(command)
    value = input("press any key to continue:")
    if value == "q":
        sys.exit(0)
    os.system(command)
