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
    if f == False:
        printf("User not exist!")
        return False
    else:
        pass

    for cp in sam.values():
        if psk != cp:
            f = False
            pass
        else:
            f = True
            if cp == '':
                wp = True
            else:
                wp = False
            break

    if f == True:
        printf("Correct credential.")
        printf("Preparing terminal...")
        if wp == True:
            printf("Weak password detected! Please change your password immediately!")
        else:
            pass
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

def cusr(usr): 
    if usr != "root":
        printf("User Creation cannot be executed by a normal user.")
        printf("Please switch to root or run as sudo.")
        return False
    else:
        pass

    un = input("Username: ") 
    f = jsonf("etc/auth/tty.sam", "read", "")
    for eu in f.keys():
        if un == eu:
            printf("User Exists!")
            return False
        else:
            pass

    printf("Creating..")
    ps = input("Password for " + un + ": ")
    if ps == '':
        printf("You did't set a password, it's very danger, and it means everyone can login to your account. You should change your password when next login!")
    else:
        pass
    f[un] = ps
    jsonf("etc/auth/tty.sam", "ovwrite", f)
    return True

def dusr(usr):
    if usr != "root":
        printf("User Deletion cannot be executed by a normal user.")
        printf("Please switch to root or run as sudo.")
        return False
    else:
        pass

    printf("You are entering destroy mode.")
    printf("You should make sure you know what are you doing right now.")
    un = input("Username: ")
    f = jsonf("etc/auth/tty.sam", "read", "")
    for eu in f.keys():
        if un != eu:
            fo = False
        else:
            fo = True
            break

    if fo != True:
        printf("User not exist!")
        return False
    else:
        pass

    cfm = input("You will delete user " + un + " permanently and unrecoverable! We will delete all data associated to this user! Type he/she's username to confirm: ")
    if cfm == un:
        pass
    else:
        printf("Operation timeout.")
        return False
   
    del f[un]
    jsonf("etc/auth/tty.sam", "ovwrite", f)
    printf("User " + un + " has been terminated and deleted from this system. You never find him/her until you create again!")
    return True

def cacheclean():
    with open("proc/username", 'w') as cc:
        cc.write("")

def urlshortener():
    try:    
        import requests
    except ImportError:
        printf("Libraries missing.")
        return False
    def apikey():
        ret = "5e8aee8d3a005a1e3878b6ee@fe8c3b9881b4143b171c7d2531d756d9"
        return ret

    def save(raw, surl):
        n = datetime.datetime.now()
        y = n.year
        m = n.month
        d = n.day
        h = n.hour
        mi = n.minute
        s = n.second
        da = "-"
        string = str(y)+da+str(m)+da+str(d)+da+str(h)+da+str(mi)+da+str(s)+" "+str(raw)+" -> "+str(surl)
        string = str(string)
        with open("history.txt", 'a') as f:
            f.write(string)
            f.write("\n")

    print("URL Shortener customize for ORSH(TM)")
    print("We used suo.im's api!")

    while True:
        raw = input("URL(Enter 'q' to quit): ")
        if raw == "q":
            return True
        print("Running quietly..")
        sapikey = "5e8aee8d3a005a1e3878b6ee@fe8c3b9881b4143b171c7d2531d756d9"
            # if "http" in url:
            #     pass
            # else:
            #     print("The URL must include http:// or https://")
            #     return False
        address = "http://suo.im/api.htm?url=" + raw + "&key=" + sapikey + "&format=json&expireDate=2099-12-31"
        req = requests.get(address)
        res = req.json()
        err = res['err']
        surl = res['url']
        if err == '':
            pass
        else:
            print("Something went wrong...")
            print(err)
            continue
        if surl == raw:
            print("Shorten failed.")
            print("Check your URL exist or this URL didn't supported.")
            continue
        else:
            pass

        printf("Shorten successful!")
        printf("\n\n\n")
        printf(surl)
        return True

def ch(usr):
    if usr != "root":
        printf("Hostname Change cannot be executed by a normal user.")
        printf("Please switch to root or run as sudo.")
        return False
    else:
        pass
    nh = input("New hostname: ")
    h = files("etc/whoami", "read", "")
    if nh == h:
        printf("Same hostname!")
        return False
    else:
        pass
    printf("Changing hostname..")
    files("etc/whoami", "ovwrite", nh)
    printf("Applying Changes..")
    printf("Reboot the system to apply changes!")
    return True
    
def libmorse_e():
    printf("Type the raw text(All lowercase will be turned to uppercase.Please not using any symbols.):")
    rawtext = input("")
    printf("\n\n\nEncrypting...")
    db = jsonf("etc/morse/dat.json", "read", "")
    prc = rawtext.upper()
    stage_1 = prc.split()
    stg1_length = len(stage_1)
    if stg1_length <= 1:
        st = True
    else:
        st = False
    files("proc/morse_code.tmp", "ovwrite", "")
    if st == True:
        stage_2 = stage_1[0]
        stage_3 = stage_2[:]
        for stage_4 in stage_3:
            cur = db[stage_4]
            files("proc/morse_code.tmp", "write", cur)
            files("proc/morse_code.tmp", "write", "/")
        
        printf(files("proc/morse_code.tmp", "read", ""))
        return True
    elif st == False:
        for stage_2 in stage_1:
            current = 0
            while True:
                global stg2_length
                stg2_length = len(stage_2)
                # printf(stg2_length)
                # printf(current)
                if current >= stg2_length:
                    break
                cur = db[stage_2[current]]
                files("proc/morse_code.tmp", "write", cur)
                files("proc/morse_code.tmp", "write", "/")
                current = current + 1
        printf(files("proc/morse_code.tmp", "read", ""))
        return True

def libmorse_d():
    db = jsonf("etc/morse/dat.json", "read", "")
    for k, v in db.items():
        s = str(k) +  "   " + str(v)
        printf(s)
    printf("Please follow these list to decrypt your code.")
    return True
    

def morse():
    printf("International Morse Code")
    printf("What do you want to do?")
    printf("1. Encrypt")
    printf("2. Decrypt")
    o = input("> ")
    if o == '1':
        libmorse_e()
    elif o == '2':
        libmorse_d()
    else:
        return False