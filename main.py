import func as lib
import os
import json
import time
import sys

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
    if cmd == "shutdown":
        lib.bye(2)
    elif cmd == "rm -rf /":
        lib.printf("You can't do that! That will destroy the entire system.")
        lib.printf("To keep safe, we are going to shutdown..")
        lib.bye(5)
    elif cmd == "rm -rf /*":
        lib.printf("You can't do that! That will destroy the entire system.")
        lib.printf("To keep safe, we are going to shutdown..")
        lib.bye(5)
    elif cmd == "passwd":
        lib.printf("Starting password change...")
        status = lib.passwd("root")
        if status != True:
            lib.printf("Something went wrong.")
            lib.printf("Operation cancelled.")
        else:
            lib.printf("Operation Executed.")
    elif cmd == "reboot":
        lib.reboot(2)
    elif cmd == "browser":
        lib.printf("Loading...")
        status = lib.wbrows()
        if status != True:
            lib.printf("Something went wrong.")
            lib.printf("Operation cancelled.")
        else:
            lib.printf("Operation Executed.")