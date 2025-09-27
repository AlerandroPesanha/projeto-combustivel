import colorama
from colorama import Fore , Style
colorama.init(autoreset=True)
import entradas
from entradas import leiafloat
import calculos
from calculos import *
import tela
from tela import tela


tela('BEM-VINDO AO CALCULO DE COMBUSTIVEL')

nome_usuario = str(input('Como devo lhe chamar? ')).title().strip()
consumo_medio = leiafloat("Qual o consumo médio (km/l) do seu carro? ")

print(f"Ok {nome_usuario}, anotamos que seu carro tem o consumo médio de {consumo_medio} km/l")
calculo_de_deslocamento(nome_usuario , consumo_medio)
