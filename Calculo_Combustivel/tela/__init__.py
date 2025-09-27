import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

def tela(txt , largura = 40):
    largura_tela = largura
    texto_centralizado = txt.center(largura_tela)
    print(f'{Fore.BLUE}-'*largura_tela)
    print(f'{Fore.BLUE}{texto_centralizado}')
    print(f'{Fore.BLUE}-'*largura_tela)