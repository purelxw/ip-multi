# client is the ip that is needed to be entered.
# noted...

import subprocess
import os
from os import system, name 
import sys
from colorama import Fore
import time
from time import sleep

def main():
    print('')
    client = input(f" [{Fore.RED}?{Fore.RESET}] Enter IP Address: ")
    print('')
    ping(client)

def ping(client):
    while not validation(client):
        client = input(f" [{Fore.RED}!{Fore.RESET}] {Fore.RED}Make sure you entered a correct IP Address...{Fore.RESET}")
    else:
        while True:
            try:
                subprocess.check_call(f"PING {client} -n 1 | FIND \"TTL=\" > NUL",shell=True)
                print(f" [{Fore.RED}>{Fore.RESET}] {Fore.GREEN}{client} is online!")
            except subprocess.CalledProcessError:
                print(f" [{Fore.RED}>{Fore.RESET}] {Fore.RED}{client} is offline!")
            except KeyboardInterrupt:
                main()

def validation(client): # i love you stackoverflow
    i = 0
    valid = True
    for element in client:
        if element == '.':
            i += 1
        else:
            try:
                int(element)
            except:
                valid = False
                pass
    if not i == 3:
        valid = False
    return valid 

main()