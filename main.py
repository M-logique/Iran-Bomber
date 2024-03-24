# import requests as req
from pystyle import Col, Center, System
from Plugins.api_list import handler
from colorama import Fore
from Plugins.functions import Functions

r, g = Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX


def start(choice: str, number: str):
    func = {
        "calls": handler.send_call,
        "sms": handler.send_sms
    }

    count = {
        "calls": handler.call_api_count,
        "sms": handler.sms_api_count
    }

    print(f"{Col.yellow}[!]{Col.green} Started Sending {choice} with {Fore.LIGHTCYAN_EX}{count[choice]}{Col.green} apis")
    return func[choice](number)


if __name__ == "__main__":
    logo = f'''

                {g}██{r}╗{g}██████{r}╗{g}  █████{r}╗{g} ███{r}╗{g}  ██{r}╗{g}
                ██{r}║{g}██{r}╔══{g}██{r}╗{g}██{r}╔══{g}██{r}╗{g}████{r}╗ {g}██{r}║
               {g} ██{r}║{g}██████{r}╔╝{g}███████{r}║{g}██{r}╔{g}██{r}╗{g}██{r}║
                {g}██{r}║{g}██{r}╔══{g}██{r}╗{g}██{r}╔══{g}██{r}║{g}██{r}║╚{g}████{r}║
                {g}██{r}║{g}██{r}║  {g}██{r}║{g}██{r}║ {g} ██{r}║{g}██{r}║ ╚{g}███{r}║
                ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚══╝
    {g}██████{r}╗  {g}█████{r}╗ {g}███{r}╗   {g}███{r}╗{g}██████{r}╗ {g}███████{r}╗{g}██████{r}╗ 
    {g}██{r}╔══{g}██{r}╗{g}██{r}╔══{g}██{r}╗{g}████{r}╗ {g}████{r}║{g}██{r}╔══{g}██{r}╗{g}██{r}╔════╝{g}██{r}╔══{g}██{r}╗
    {g}██████{r}╦╝{g}██{r}║  {g}██{r}║{g}██{r}╔{g}████{r}╔{g}██{r}║{g}██████{r}╦╝{g}█████{r}╗  {g}██████{r}╔╝
    {g}██{r}╔══{g}██{r}╗{g}██{r}║{g}  ██{r}║{g}██{r}║╚{g}██{r}╔╝{g}██{r}║{g}██{r}╔══{g}██{r}╗{g}██{r}╔══╝{g}  ██{r}╔══{g}██{r}╗
    {g}██████{r}╦╝╚{g}█████{r}╔╝{g}██{r}║ ╚═╝ {g}██{r}║{g}██████{r}╦╝{g}███████{r}╗{g}██{r}║  {g}██{r}║
    {r}╚═════╝  ╚════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
    '''




    while True:
        System.Clear()
        print(Center.XCenter(logo))

        try:
            proxy_state = Fore.GREEN + "Enabled" if Functions.proxy_state() else Fore.RED + "Disabled"
            choices = {
                "1": "call",
                "2": "sms"
            }
            print(f"{Col.yellow}[!]{Col.gray} Proxies are {proxy_state}")
            print(f"{Col.yellow}[!]{Fore.CYAN} Choices: ")

            for ch in choices:
                print(f"   {Fore.CYAN}{ch}- {Fore.GREEN}{choices[ch].capitalize()} Bomber ")
            
            print()
            choice = Functions.get_input(f"{Fore.CYAN}[=]{Col.gray} Enter Your Choice: {Col.green}", lambda x: x in [str(i) for i in choices])
            number = Functions.get_input(f"{Fore.CYAN}[=]{Col.gray} Enter the phone number {Fore.CYAN}[9xxxxxxxxx]{Col.gray}: {Col.green}", checker=lambda x: x != "" and x.isnumeric() and x.startswith("9") and len(x) == 10)

            Functions.start(choices[choice], number)


        except KeyboardInterrupt:
            print("\n" + Fore.BLUE, "Exiting...")
            exit()
