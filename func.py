import os
import json
import time
import datetime
import sys

def printf(req):
    with open("./proc/log.conf", 'a') as fp:
        fp.write("\n")
        fp.write(req)
    print(req)
    return True

def delay(req):
    timed = int(req)
    time.sleep(timed)
    return True

def files(locat, opt, txt):
    if opt == "read":
        o = 'r'
    elif opt == "ovwrite":
        o = 'w'
    elif opt == "write":
        o = 'a'
    else:
        return False
    
    if o == 'r':
        with open(locat, 'r') as fp:
            ret = fp.read()
        return ret
    elif o == 'w':
        with open(locat, 'w') as fp:
            fp.write(txt)
        return True
    elif o == 'a':
        with open(locat, 'a') as fp:
            fp.write(txt)
        return True
    else:
        return False
    printf("Process ended with True")

def tty():
    data = datetime.datetime.now()
    yar = data.year
    mon = data.month
    day = data.day
    hrs = data.hour
    miu = data.minute
    sec = data.second
    dat = str(yar) + "-" + str(mon) + "-" + str(day) + " " + str(hrs) + ":" + str(miu) + ":" + str(sec)
    printf("ORSH 1.0.0 login on tty " + dat)
    usr = input("\nUsername: ")
    psk = input("\nPassword: ")
    with open("etc/auth/tty.sam",  'r') as fp:
        d = fp.read()
    que = usr + " " + psk
    if que != d:
        printf("Access Denied.")
        a = False
    else:
        a = True
    
    if a != True:
        printf("Illegal login! Shutting down...")
        time.sleep(2)
        sys.exit(0)
    else:
        printf("Access Granted, preparing main frame...")
        return True
