from pystyle import Col
from Plugins.api_list import handler
from colorama import Fore
from typing import Optional
from os import path
from random import choice


class Functions:


    @staticmethod
    def start(choice: str, number: str, spam_count: Optional[int] = 10, proxies: Optional[dict] = None):
        if Functions.proxy_state():
            proxies = {"http": Functions.get_proxy(), "https": Functions.get_proxy()}
        
        
        func = {
            "call": handler.send_call,
            "sms": handler.send_sms
        }

        count = {
            "call": handler.call_api_count,
            "sms": handler.sms_api_count
        }


        print(f"{Col.yellow}[!]{Col.green} Started sending {choice} with {Fore.LIGHTCYAN_EX}{count[choice]}{Col.green} apis")
        for i in range(spam_count):
            func[choice](number, proxies)
    

    @staticmethod
    def get_input(text: str, checker: callable = True):

        v = input(text)
        if not checker(v):
            while not checker(v):
                print(f"{Fore.LIGHTRED_EX}[!]{Fore.YELLOW} Try again")
                v = input(text)
        
        return v
    
    @staticmethod
    def proxy_state():
        return path.exists("./proxies.txt")
    
    @staticmethod
    def get_proxy():

        if path.exists("./proxies.txt"):
            with open("proxies.txt") as file:
                return choice(file.read().splitlines()) if len(file.readlines()) != 0 else None
            
