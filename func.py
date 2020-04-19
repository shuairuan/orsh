# coding=gbk
import os
import json
import time
import datetime
import sys
import requests

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

def bye(req, usr):
    if usr != "root":
        printf("Process 'System' cannot be terminated by a normal user.")
        printf("Please switch to root.")
        return False
    else:
        pass
    printf("Shutting down...")
    delay(req)
    sys.exit(0)

def reboot(req, usr):
    if usr != "root":
        printf("Process 'System' cannot be terminated by a normal user.")
        printf("Please switch to root.")
        return False
    else:
        pass
    printf("Rebooting...")
    delay(req)
    os.system("main.py")
    sys.exit(0)

def jsonf(locat, opt, txt):
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
            ret = json.load(fp)
        return ret
    elif o == 'w':
        with open(locat, 'w') as fp:
            json.dump(txt, fp)
        return True
    elif o == 'a':
        with open(locat, 'a') as fp:
            json.dump(txt, fp)
        return True
    else:
        return False
    printf("Process ended with True")

def gettime():
    data = datetime.datetime.now()
    yar = data.year
    mon = data.month
    day = data.day
    hrs = data.hour
    miu = data.minute
    sec = data.second
    dat = str(yar) + "-" + str(mon) + "-" + str(day) + " " + str(hrs) + ":" + str(miu) + ":" + str(sec)
    return dat

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

def termprepare(req):
    files("proc/username", "ovwrite", req)
    return True

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
    sam = jsonf("etc/auth/tty.sam", "read", "")
    for cu in sam.keys():
        if usr != cu:
            f = False
            pass
        else:
            f = True
            break
    
    for cp in sam.values():
        if psk != cp:
            f = False
            pass
        else:
            f = True
            break

    if f == True:
        printf("Correct credential.")
        printf("Preparing terminal...")
        termprepare(usr)
        return True
    else:
        printf("The credential you gave is invalid.")
        return False

    if a != True:
        printf("Illegal login! Shutting down...")
        time.sleep(2)
        sys.exit(0)
    else:
        printf("Access Granted, preparing main frame...")
        return True

def passwd(req):
    printf("You are " + req)
    opsk = input("Old password: ")
    f = jsonf("etc/auth/tty.sam", "read", "")
    u = f[req]
    if opsk != u:
        printf("Old password wrong! Please try to remember that.")
        return False
    else:
        pass
    npsk = input("New password: ")
    rpsk = input("Repeat new password: ")
    if npsk != rpsk:
        printf("Password not match.")
        return False
    else:
        pass
    printf("Nothing there buds.")
    f[req] = npsk
    jsonf("etc/auth/tty.sam", "ovwrite", f)
    printf("Done!")
    printf("Now user: " + req + "'s password changed from " + opsk + " to " + npsk + ".")
    return True

def wbrows():
    printf("Loaded")
    url = input("Web Link(Including http:// or https://): ")
    get = requests.get(url)
    sc = get.status_code
    printf("Status code: " + str(sc))
    printf("Tip: If the status code is not equal to 200, there is something wrong.")
    printf("301/302: The address pointed to is redirected and there is generally no problem. Go where the link point.")
    printf("401: This server needs credential. Unauthorized.")
    printf("404: The address pointed to does not exist.")
    printf("500: The other's server has a problem.")
    if str(sc) != "200":
        printf("Error.")
        return False
    else:
        pass
    json = input("Is this a json file?(yes/no):  ")
    if json == "yes":
        printf("Loading..")
        txt = get.json()
        printf(txt)
        printf("\n\n\n")
        u = input("Do you want to save to file?(yes/no): ")
        if u == "yes":
            printf("Saved to /tmp/get.json")
            files("tmp/get.json", "write", txt)
        else:
            pass
    else:
        printf("Loading...")
        obj = get.text
        printf(obj)
        printf("\n\n\n")
        u = input("Do you want to save to file?(yes/no): ")
        if u == "yes":
            printf("Saved to /tmp/get.txt")
            files("tmp/get.json", "write", obj)
    return True

def usrcgr():
    ousr = input("Old username: ")
    nusr = input("New username: ")
    sam = jsonf("etc/auth/tty.sam", "read", "")
    for username in sam.keys():
        if ousr == username:
            printf("Executing..")
            f = True
            break
        else:
            f = False
            pass
    if f != True:
        printf("Old user don't exist.")
        return False
    else:
        pass
    
    printf("Changing " + ousr + " to " + nusr)
    usrpsk = sam[ousr]
    del sam[ousr]
    sam[nusr] = usrpsk
    jsonf("etc/auth/tty.sam", "ovwrite", sam)
    printf("Done!")
    return True

def switchusr(c):
    t = input("You want to switch to: ")
    sam = jsonf("etc/auth/tty.sam", "read", "")
    p = input(t + "'s password: ")
    for key in sam.keys():
        if t == key:
            y = True
            break
        else:
            y = False
            pass
    if y == False:
        printf("The user '" + t + "' doesn't exist.")
        return False
    else:
        pass

    for value in sam.values():
        if p == value:
            y = True
            break
        else:
            y = False
            pass
    if y == False:
        printf("Access denied")
        return False
    else:
        printf("Access Granted.")
        pass

    files("proc/username", "ovwrite", t)
    printf("Switched to user " + t)
    return True

def sudo(pwd):
    sam = jsonf("etc/auth/tty.sam", "read", "")
    p = sam["root"]
    if pwd == p:
        printf("sudo mode activated instantly.")
        return True
    else:
        printf("Permission denied.")
        return False

def gtime():
    printf(gettime())
    return True
