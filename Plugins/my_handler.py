from threading import Thread
from pystyle import Col
from colorama import Fore
from typing import Optional, Union

class Handler:
    def __init__(self) -> None:
        self.sms, self.call = [], []
    
    def sms_api(self, func):

        self.sms.append(func)
    
    def send_sms(self, num: str, proxies: Optional[dict] = None):

        

        threads = [Thread(target=self.launcher, args=[func, num, proxies]) for func in self.sms]

        for thread in threads:
            thread.start()
        else:
            for thread in threads:
                thread.join()

    def send_call(self, num: str, proxies: Optional[dict] = None):


        threads = [Thread(target=self.launcher, args=[func, num, proxies]) for func in self.call]

        for thread in threads:
            thread.start()
        else:
            for thread in threads:
                thread.join()

    def launcher(self, func: callable, num: str, proxies: Union[dict | None]):

        try:
            func(num, proxies)
            print(f"{Col.green}[+]{Fore.LIGHTMAGENTA_EX} Sent {Col.light_blue}{func.__name__}")
        except: 
            print(f"{Col.red}[-]{Fore.LIGHTBLACK_EX} Failed to send {Col.yellow}{func.__name__}")




    def call_api(self, func):
        
        self.call.append(func)

    @property
    def sms_api_count(self):
        return len(self.sms)
    
    @property
    def call_api_count(self):
        return len(self.call)