import os
import time
from string         import ascii_lowercase, ascii_uppercase, digits
from vardxg         import Center
from random         import *

os.system(f"title Password Generator V1")
os.system('cls')

def banner() -> str:
    vardxg = (f"""
    Password Generator V1
    
    
    """)
    print(Center.XCenter(vardxg))

class pwgen:
    def __init__(self) -> None:
        pass
    
    def generate_password() -> str:
        characters = ascii_lowercase + ascii_uppercase
        numbers = digits
        punctuation = ["!", "@", "#", "$", "%", "^", "&", "*"]
        password = choices(characters, k=11) + choices(numbers, k=2) + choices(punctuation, k=2)
        shuffle(password)
        return "".join(password)
    
    for _ in range(500):
        banner()
        password = generate_password()
        print(f"\n Password =>  {password}")
        time.sleep(4)
        os.system('cls')

# => Made by @vardxg on Telegram!
