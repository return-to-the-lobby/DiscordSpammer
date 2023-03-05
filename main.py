import requests
import colorama

from ast import literal_eval
from time import sleep
from math import floor
from random import uniform
from configparser import ConfigParser

colorama.init(autoreset=True)

parser = ConfigParser()
parser.read('config.ini', encoding='UTF-8')

content = parser.get('config', 'Content')
space = parser.get('config', 'Space')
delay = parser.get('config', 'Delay')
authorization = parser.get('config', 'Authorization')
channel = parser.get('config', 'Channel')

space = literal_eval(space)
delay = literal_eval(delay)

print(delay)

sent = 0

counts = 2000 / len(content) if not space else 2000 / (len(content) + 1)
counts = floor(counts)
print(f'Word length for {content!r} is', colorama.Fore.YELLOW + str(counts), end='\n')

def request():
    if not space:
        word = content * counts
    else:
        word = (content + ' ') * counts
    length = len(word)
    print(colorama.Fore.GREEN + '[*]', 'THE MESSAGE\'S LENGTH IS', colorama.Fore.YELLOW + str(length), end='\n')
    response = requests.post(
        f'https://discord.com/api/v9/channels/{channel}/messages',
        headers={'authorization': authorization, 'content-type': 'application/json'},
        json={'content': word},
    )
    if not response.ok:
        print(colorama.Fore.RED + '[!]', f'REQUEST RESPONSE RETURNED BAD RESPONSE: CODE {response.status_code} ({response.reason})', end='\n')
    else:
        print(colorama.Fore.GREEN + '[@]', 'MESSAGE SENT', end='\n')
    return response

try:
    while 1:
        request()
        second = uniform(*delay)
        print(colorama.Fore.GREEN + '[*]', 'SLEELPING FOR', colorama.Fore.YELLOW + str(second), 'SECONDS', end='\n')
        sent += 1
        sleep(second)
except KeyboardInterrupt:
    print(f'[{colorama.Fore.BLUE + "TOTAL SENT" + colorama.Fore.RESET}: {colorama.Fore.YELLOW + str(sent) + colorama.Fore.RESET}]')
