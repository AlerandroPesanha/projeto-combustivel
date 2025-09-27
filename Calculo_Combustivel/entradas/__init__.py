import colorama
from colorama import Fore , Style
colorama.init(autoreset=True)
def leiaint(txt):
    while True:
        try:
            n = input(txt).strip("")
            n = int(n)
            return n
        except ValueError:
            print(f'{Fore.RED}Valor incorreto, digite novamente')
            continue
        except TypeError:
            print(f'{Fore.RED}O tipo de entrada está incorreto.')
            continue
        except KeyboardInterrupt:
            n = 0 
            print(f'{Fore.RED}O usuário decidiu parar o programa.')
            return n

def leiafloat(txt):
    while True:
        try:
            n = input(txt).replace("," , ".").strip("")
            n = float(n)
            return n
        except ValueError:
            print(f'{Fore.RED}Valor digitado incorreto.')
        except TypeError:
            print(f'{Fore.RED}Tipo informado está incorreto.')
        except KeyboardInterrupt:
            n = 0
            print(f'{Fore.RED}O Usuário decidiu para o programa.')
            return n
        
