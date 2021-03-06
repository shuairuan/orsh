import func as lib
import os
import json
import time
import sys

lib.cacheclean()

status = lib.tty()
if status == True:
    pass
else:
    lib.printf("Illegal login, shutting down...")
    lib.delay(1)
    sys.exit(0)

hostname = lib.files("etc/whoami", "read", "")
while True:
    sudo = False
    username = lib.files("proc/username", "read", "")
    prt = username + "@" + hostname + ": ~ $ "
    cmd = input(prt)
    lib.files("proc/.ohsh_history", "write", "\n")
    lib.files("proc/.ohsh_history", "write", username)
    lib.files("proc/.ohsh_history", "write", ": ")
    if "sudo" in cmd:
        lib.printf("You are entering sudo mode.")
        lib.printf("You should know what are you doing right now.")
        lib.printf("sudo mode = run as 'root'")
        psk = input("root's password: ")
        ss = lib.sudo(psk)
        if ss == True:
            username = "root"
            sudo = True
            lib.files("proc/.ohsh_history", "write", "\nsudo mode activated.\n")
        else:
            lib.files("proc/.ohsh_history", "write", "\nTrying to switch root, permission denied.\n")
            lib.printf("\nYou are currently running at normal user mode.")
            pass
        sp = cmd.split()
        try:
            cmd = sp[1]
        except IndexError:
            lib.printf("sudo: empty argument.")
            continue
    lib.files("proc/.ohsh_history", "write", cmd)
    if cmd == "shutdown":
        lib.bye(2, username)
    elif cmd == "rm -rf /":
        lib.printf("You can't do that! That will destroy the entire system.")
        lib.printf("To keep safe, we are going to shutdown..")
        lib.bye(5, username)
    elif cmd == "rm -rf /*":
        lib.printf("You can't do that! That will destroy the entire system.")
        lib.printf("To keep safe, we are going to shutdown..")
        lib.bye(5, username)
    elif cmd == "passwd":
        lib.printf("Starting password change...")
        status = lib.passwd(username)
        if status != True:
            lib.printf("Something went wrong.")
            lib.printf("Operation cancelled.")
        else:
            lib.printf("Operation Executed.")
    elif cmd == "reboot":
        lib.reboot(2, username)
    elif cmd == "browser":
        lib.printf("Loading...")
        status = lib.wbrows()
        if status != True:
            lib.printf("Something went wrong.")
            lib.printf("Operation cancelled.")
        else:
            lib.printf("Operation Executed.")
    elif cmd == "user":
        lib.printf("Loading...")
        status = lib.usrcgr()
        if status != True:
            lib.printf("Something went wrong.")
            lib.printf("Operation cancelled.")
        else:
            lib.printf("Operation Executed.")
    elif cmd == "switchuser":
        lib.printf("Loading...")
        status = lib.switchusr(username)
        if status != True:
            lib.printf("Something went wrong.")
            lib.printf("Operation cancelled.")
        else:
            lib.printf("Operation Executed.")
    elif cmd == "time":
        lib.printf("Loading..")
        status = lib.gtime()
        if status != True:
            lib.printf("Something went wrong.")
            lib.printf("Operation cancelled.")
        else:
            lib.printf("Operation Executed.")
    elif cmd == "useradd":
        lib.printf("Loading..")
        status = lib.cusr(username)
        if status != True:
            lib.printf("Something went wrong.")
            lib.printf("Operation cancelled.")
        else:
            lib.printf("Operation Executed.")
    elif cmd == "userdel":
        lib.printf("Loading..")
        status = lib.dusr(username)
        if status != True:
            lib.printf("Something went wrong.")
            lib.printf("Operation cancelled.")
        else:
            lib.printf("Operation Executed.")

    elif cmd == "surl":
        lib.printf("Loading..")
        status = lib.urlshortener()
        if status != True:
            lib.printf("Something went wrong.")
            lib.printf("Operation cancelled.")
        else:
            lib.printf("Operation Executed.")

    elif cmd == "chost":
        lib.printf("Loading...")
        status = lib.ch(username)
        if status != True:
            lib.printf("Something went wrong.")
            lib.printf("Operation cancelled.")
        else:
            lib.printf("Operation Executed.")
    elif cmd == "morse":
        lib.printf("Loading...")
        status = lib.morse()
        if status != True:
            lib.printf("Something went wrong.")
            lib.printf("Operation cancelled.")
        else:
            lib.printf("Operation Executed.")
    
    elif cmd == "dict":
        lib.printf("Loading...")
        status = lib.dictionary()
        if status != True:
            lib.printf("Something went wrong.")
            lib.printf("Operation cancelled.")
        else:
            lib.printf("Operation Executed.")

    else:
        lib.printf("orsh: command not found.")

    if status == True:
        lib.files("proc/.ohsh_history", "write", ": Successful.")
    elif status == False:
        lib.files("proc/.ohsh_history", "write", ": Failed.")
    else:
        lib.files("proc/.ohsh_history", "write", ": No report.")
    if sudo == True:
        lib.files("proc/.ohsh_history", "write", " sudo mode.")
    else:
        pass
