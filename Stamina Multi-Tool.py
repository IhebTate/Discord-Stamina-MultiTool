import re
import os
import discord
import asyncio
import requests
import time
from time import sleep
from tqdm import tqdm
from colorama import Fore as C
from discord.ext import commands

def anti_afk():
    os.system('cls')

    bot = commands.Bot(command_prefix="!")

    print(f'''
    {C.WHITE}                        ┌─┐┌┐┌┌┬┐┬  ┌─┐┌─┐┬┌─  ┌─┐┬ ┬┌─┐┌─┐┬┌─
                            {C.MAGENTA}├─┤│││ │ │  ├─┤├┤ ├┴┐  │  ├─┤├┤ │  ├┴┐
                            {C.LIGHTWHITE_EX}┴ ┴┘└┘ ┴ ┴  ┴ ┴└  ┴ ┴  └─┘┴ ┴└─┘└─┘┴ ┴
    {C.MAGENTA}                        ┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
                                  {C.WHITE}Enter Your {C.MAGENTA}Token{C.WHITE} To Continue
                            {C.MAGENTA}┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙
    ''')

    token = input(f'{C.WHITE}Enter {C.MAGENTA}Token:{C.WHITE} ')
    r = input(f'{C.WHITE}Enter {C.MAGENTA}Response:{C.WHITE} ')
    d = input(f'{C.WHITE}Enter {C.MAGENTA}Delay {C.WHITE}(In {C.MAGENTA}Seconds{C.WHITE}){C.MAGENTA}:{C.WHITE} ')


    @bot.event
    async def on_ready():
        os.system(f'title [Anti-AFK]')
        os.system('cls')
        print(f'''
    {C.WHITE}        ┌─┐┌┐┌┌┬┐┬  ┌─┐┌─┐┬┌─  ┌─┐┬ ┬┌─┐┌─┐┬┌─
    {C.MAGENTA}        ├─┤│││ │ │  ├─┤├┤ ├┴┐  │  ├─┤├┤ │  ├┴┐
    {C.WHITE}        ┴ ┴┘└┘ ┴ ┴  ┴ ┴└  ┴ ┴  └─┘┴ ┴└─┘└─┘┴ ┴
    {C.MAGENTA}          ┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
    {C.WHITE}                    Login:{C.MAGENTA}[{C.WHITE}{bot.user.name}{C.MAGENTA}#{C.WHITE}{bot.user.discriminator}{C.MAGENTA}]
    {C.WHITE}                    Response:{C.MAGENTA}[{C.WHITE}{r}{C.MAGENTA}]
    {C.WHITE}                    Delay:{C.MAGENTA}[{C.WHITE}{d}{C.MAGENTA}]{C.WHITE} Seconds
    {C.MAGENTA}          ┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙
    ''')


    @bot.event
    async def on_message(x):
        if f"<@!{bot.user.id}>" in x.content.lower() or 'afk' in x.content.lower() and '1' in x.content.lower():
            await asyncio.sleep(int(d))
            await x.channel.send(r)
            print(f'{C.MAGENTA}<{C.WHITE}+{C.MAGENTA}> {C.WHITE}1{C.MAGENTA} AFK Check Blocked -> {C.WHITE}{x.author} {C.MAGENTA}')

    bot.run(token, bot=False)



def auto_presser():
    token  = input('Token: ')
    bot    = commands.Bot(command_prefix='>', self_bot=True)

    class i:
        def __init__(self) -> None:
            self.messages = [
    'FOCUS', 'IN', 'CHAT',
    'DWEEB ASS', 'PEON', 'UNSKILLED FARM WORKER',
    'IM STEPPIN ON U LOLOLOO', 'L', 'O', 'L',
    'O', 'L', 'O', 'L', 'LOOOOOOOOOOOOOOOOOOOOOOO',
    'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOLLLL',
    'GET MAD SON WYD', 'YE LO', 'DWEEB ASS PEASANT',
    'HOW DARE A MERE VERMIN', 'STEP', 'TO',
    'ME', 'DWEEB ASS PEASANT',
    'IM STEPPING ON YOU LOLOLOLOL',
    'HAHAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHHAHA',
    'SON WHY CANT U TYPE FASTER',
    'UR FINGERS R THROBBING', 'WEAK BITCH',
    'DONT FOLD TO ME NOW',
    'I CAN PRESS FOR ETERNITY',
    'U WERE ARTIFICIALLY MADE TO LOSE TO KE',
    'WEAK ASS KID', 'DWEEB ASS BITCH',
    'OOOLOOOLOLOLOLOLOLOLOLOLLO',
    'LOLOLOLOLOLOLOLOLOLOLOLOLOLOLOL',
    'SHITTER AFTICAN KICK BOXER',
    'U SNORT SOGGY BISCUITS FOR NO REASON',
    'LO SON DIDNT U TRY TO RAPE A BISEXUAL',
    'DLOLOLOL WTF UR WEIRD BITCH', 'WEAK', 'ass',
    'LOSER ASS', 'PEON', 'ASS', 'BITCH', 'ASS',
    'HOE', 'ASS', 'NERD', 'ASSS', 'PUSSY',
    'ASS', 'BUM ASS ROBLOXIAN PACKER BITCH',
    'ROLEPLAY VR ESEXER', 'ARMADILLO KNEE CAP LICKER',
    'FUCKIMG LOSER', 'GO GET UR MONEY UP',
    'LO', 'LOLOLOLOLOLOLO', 'L', 'O', 'L', 'O', 'L',
    'UR MOTHER IS SWALLOW MY EDICK LO',
    'SHE RUBS HER LIL EPUSSY TO ME IN VC', 'lo',
    'UR MAD BITCH', 'DONT CRY NOW',
    'U SET URSELF UP FOR FAILURE STEPPIN TO ME',
    'DOES', 'IT', 'LOOK','LIKE',
    'I', 'G', 'A', 'F', 'PIEGON FUCKER',
    'HOW YOU FEEL BUM ASS NIGGA'
    ]

    bot.remove_command('help')

    @bot.event
    async def on_ready():
        print('Listening for: "lets pack [mention user]"')

    @bot.event
    async def on_message(x):

        l = False

        def r(z = r'<@!?([0-9]+)>') -> list:
            return re.findall(z, x.content)

        if not l:
            if r() and 'lets pack' in x.content.lower() and x.author == bot.user:
                l = True
                await asyncio.sleep(0)
                async with x.channel.typing():
                    for v in i().messages:
                        for c in str(v):
                            await asyncio.sleep(0.00)
                        async with x.channel.typing():
                            await x.channel.send(v)

                l = False

    bot.run(token, bot=False)



def anti_block():
    class BlockBypass:
        def __init__(self, token, userId):
            self.channelId = None
            self.userId = userId
            self.api = 'https://discord.com/api/v8/'
            self.headers = {
                'Authorization': token,
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
            }

        def generateChannel(self):
            request = requests.post(f'{self.api}users/@me/channels', json={'recipients': [ self.userId ]}, headers=self.headers)

            if request.status_code == 200:
                print('[] Successfully created the channel\n')
                self.channelId = request.json()['id']
                self.main()
            else:
                print('[] Couldn\'t create the channel!')
                print(request.status_code, request.json())
                exit(0)

        def sendMessage(self, message):
            request = requests.post(f'{self.api}channels/{self.channelId}/messages', json={'content': message}, headers=self.headers)

            if request.status_code == 200:
                print('[] Successfully sent the message\n')
            else:
                print('[] Failed', request.json(), '\n')

            self.main()

        def main(self):
            content = input('[Message To Send] -> ')

            self.sendMessage(content)

    if __name__ == '__main__':
        print('\nWelcome to BlockBypass.\nWhat is it -> This is a simple script that let\'s you talk to anyone who YOU blocked.\nWhy -> Just a simple troll\nHow -> Someone by the name of Yaekith discovered this a while ago (2018) while messing around with the discord api.\n\n')
        # Variables
        token = input('Token -> ')
        userId = input('UserId to Message -> ')
        print('\n')
        # Class Definition
        yesnt = BlockBypass(token, userId)
        yesnt.generateChannel()
        yesnt.main()


def afk_checker():
    def clear(): return os.system('cls') if os.name == 'nt' else os.system('clear')


    clear()
    token = input(C.MAGENTA+" root" + C.WHITE+"@" + C.MAGENTA+"ihebman" +
                  C.WHITE+":" + C.CYAN+"~" + C.WHITE+"Enter Token: " + C.WHITE+" ")


    class counter(discord.Client):
        async def on_ready(self):
            os.system(
                f'title [AFK-CHECKER] │ Connected As: {self.user}')
            print(f"""
    {C.MAGENTA}
    {C.WHITE}                ██╗██╗  ██╗███████╗██████╗ 
    {C.MAGENTA}                ██║██║  ██║██╔════╝██╔══██╗
    {C.WHITE}                ██║███████║█████╗  ██████╔╝
    {C.MAGENTA}                ██║██╔══██║██╔══╝  ██╔══██╗
    {C.WHITE}                ██║██║  ██║███████╗██████╔╝
    {C.MAGENTA}                ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝                  
    {C.MAGENTA}              ┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
    {C.WHITE}              Dev: {C.MAGENTA}GodJustice/Iheb
    {C.WHITE}                       Loading....
    {C.MAGENTA}              ┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙
    """)
            print(f"{C.MAGENTA}")
            progressbar = tqdm([2, 4, 6, 8, 10])
            for item in progressbar:
                sleep(0.1)
                progressbar.set_description(' Loading: ')

            clear()
            print(f"""
            {C.WHITE}                     ██╗██╗  ██╗███████╗██████╗ 
            {C.MAGENTA}                     ██║██║  ██║██╔════╝██╔══██╗
            {C.WHITE}                     ██║███████║█████╗  ██████╔╝
            {C.MAGENTA}                     ██║██╔══██║██╔══╝  ██╔══██╗
            {C.WHITE}                     ██║██║  ██║███████╗██████╔╝
            {C.MAGENTA}                     ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝                  
            {C.MAGENTA}                    ┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
            {C.WHITE}                      Dev: {C.MAGENTA}GodJustice/Iheb
            {C.WHITE}                     Trigger Word:{C.MAGENTA}['{C.WHITE}AFK{C.WHITE} CHECK{C.WHITE}{C.MAGENTA} @user{C.WHITE}{C.MAGENTA}']
            {C.MAGENTA}                    ┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙

            """)

        async def on_message(self, x):
            regex = re.findall(r'<@!?([0-9]+)>', x.content)
            if regex and 'afk check' in x.content.lower() and x.author == self.user:
                for i in range(1, 100001):
                    await x.channel.send(i)


    counter().run(token, bot=False)



class Main():
    def __init__(self) -> None:
        self._banner = """
           
                    ██╗██╗  ██╗███████╗██████╗
                    ██║██║  ██║██╔════╝██╔══██╗
                    ██║███████║█████╗  ██████╔╝
                    ██║██╔══██║██╔══╝  ██╔══██╗
                    ██║██║  ██║███████╗██████╔╝
                    ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝       
                ╔══════════════════════════════════════════════╗
                ║                                              ║
                ║    [1] ANTI-AFK      [3] AUTO-PRESSER        ║
                ║    [2] AFK CHECKER   [4] BLOCK-BYPASS        ║
                ║                                              ║
                ╚══════════════════════════════════════════════╝               
        """
    def _home(self):
        os.system('title PRIVATE STAMINA [MULTI-TOOL]')
        print(self._banner)
        _v       = int(input("Select a tool - "))
        _choices = [1, 2, 3, 4]
        
        if _v in _choices:
            if _v == 3:
                auto_presser()
            
            if _v == 1:
                anti_afk()
            
            if _v == 2:
                afk_checker()

            if _v == 4:
                anti_block()

        if _v not in _choices:
                print("Invalid option")
                time.sleep(1)
                Main()._home()


if __name__ == '__main__':
    Main()._home()