import colorama
from colorama import Fore , Style
from entradas import *
import time
from time import sleep
colorama.init(autoreset=True)

def calculo_de_deslocamento(nome , consumo_medio):
    """
    Essa função solicita o nome do usuário e o consumo médio do seu veiculo
    ela irá receber do usuário no leiafloat(txt) e leiaint(txt) as infomações para iniciar o calculo, essas funções
    usam de base o float() e o int() nativo do python, mas já com algum nivel de segurança para o programa não quebrar
    caso o usuário digite um comando invalido.
    """
    posto_A = leiafloat('Quantos KM até o primeiro posto? ')
    valor_combustivelA = leiafloat('Quanto está o valor nesse posto? ')

    posto_B = leiafloat('Quantos KM até o segundo posto? ')
    valor_combustivelB = leiafloat('E nesse posto quanto está? ')
    while True:
        abastecer = leiaint('Quantos litros você deseja abastecer? ')
        if abastecer <= 70:
            break
        else:
            print(f'{Fore.RED}O Valor "{abastecer}" não está em conformidade com os tanques atualmente, digite o valor correto.')
            continue
    #Calculo da distancia de ida e volta, não leva em conta o transito no momento
    distancia_postoA = posto_A*2
    distancia_postoB = posto_B*2
    #Calculamos o total de litros gastos de ir no posto e voltar para casa
    litros_gastosA = distancia_postoA / consumo_medio
    litros_gastosB = distancia_postoB / consumo_medio
    #Calculamos o custo inicial para ir até o posto
    custoA = litros_gastosA *valor_combustivelA
    custoB = litros_gastosB * valor_combustivelB
    #Nessa parte é o custo de ida e volta, definindo onde será mais econômico
    custo_total_A = (abastecer * valor_combustivelA) + custoA
    custo_total_B = (abastecer * valor_combustivelB) + custoB

    if custo_total_A > custo_total_B:
        melhor_opcao = "Abasteça no posto B"
        economia = custo_total_A - custo_total_B
    elif custo_total_A < custo_total_B:
        melhor_opcao = "Abasteça no posto A"
        economia = custo_total_B - custo_total_A
    else:
        melhor_opcao = "Abasteça no posto A"
        economia = "tempo , pois o valor nos postos será o mesmo no final"
    print(f'{Fore.CYAN}Calculando a melhor rota entre os postos...')
    sleep(2)
    print(f'{Fore.CYAN}Já vamos ter o resultado {nome}...')
    sleep(2)

    print('-'*40)
    print(f'{Fore.YELLOW}{melhor_opcao} ,{Fore.GREEN}você economizará R${economia:.2f}!'.center(40))
    print('-'*40)
