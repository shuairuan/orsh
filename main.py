import func as lib
import os
import json
import time
import sys

time.sleep(1)
status = lib.tty()
if status == True:
    pass
else:
    lib.printf("Illegal login, shutting down...")
    delay(1)
    sys.exit(0)

hostname = lib.files("etc/whoami", "read", "")

while True:
    prt = "root@" + hostname + ": ~ $ "
    cmd = input(prt)