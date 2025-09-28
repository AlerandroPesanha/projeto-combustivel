# main.py
import streamlit as st
from streamlit_geolocation import streamlit_geolocation

#Importando as funções com os nomes do arquivo api_handler.py
from api_handler import buscar_postos_proximos, calcular_distancia

st.title("⛽ Calculadora de Posto de Combustível")

st.sidebar.header("Informações Gerais")
consumo = st.sidebar.number_input("Consumo do veículo (km/l)", min_value=1.0, value=18.0)
qtd_abastecer = st.sidebar.number_input('Quanto deseja abastecer (Litros)?', min_value=1.0, value=40.0)

st.header("1. Encontre os Postos")

localizacao = streamlit_geolocation()

if st.button("Buscar Postos Próximos"):
    if localizacao and localizacao.get('latitude'):
        st.session_state['localizacao_usuario'] = localizacao
        st.session_state['postos_encontrados'] = buscar_postos_proximos(
            localizacao['latitude'], 
            localizacao['longitude']
        )
        st.success('Postos (simulados) encontrados! Preencha os preços abaixo.')
    else:
        st.warning("Localização não obtida. Por favor, clique novamente ou verifique as permissões do seu navegador.")

# --- Bloco de exibição FORA do primeiro botão ---
if 'postos_encontrados' in st.session_state:
    postos = st.session_state['postos_encontrados']
    
    # Usando a chave "resultados" 
    if postos and postos.get('resultados'):
        st.subheader("2. Preencha os Preços")
        
        # Estrutura : 'posto' (singular) para o item do loop
        for posto in postos['resultados']:
            with st.container(border=True):
                nome = posto['name']
                endereco = posto['vicinity']

                st.subheader(nome)
                st.write(f"**Endereço:** {endereco}")

                st.number_input(
                    "Preço do Combustível (R$):", 
                    key=nome,
                    min_value=2.50,
                    value=5.50,
                    step=0.10,
                    format='%.2f'
                )
        
        st.header("3. Calcule a Melhor Opção")
        if st.button("Calcular Melhor Opção"):
            loc_usuario = st.session_state['localizacao_usuario']
            lat_usuario = loc_usuario['latitude']
            lon_usuario = loc_usuario['longitude']

            lista_resultados = []

            # Estrutura: Loop usando a chave 'resultados'
            for posto in postos['resultados']:
                nome_posto = posto['name']
                preco_combustivel = st.session_state[nome_posto]

                lat_posto = posto['geometry']['location']['lat']
                lon_posto = posto['geometry']['location']['lng']
                distancia = calcular_distancia(lat_usuario, lon_usuario, lat_posto, lon_posto)
                
                distancia_total_viagem = distancia * 2
                litros_gastos_viagem = distancia_total_viagem / consumo
                custo_da_viagem = litros_gastos_viagem * preco_combustivel
                
                custo_abastecimento = qtd_abastecer * preco_combustivel
                custo_total = custo_da_viagem + custo_abastecimento

                lista_resultados.append({
                    "nome": nome_posto,
                    "distancia": f"{distancia:.2f} km",
                    "preco_litro": f"R$ {preco_combustivel:.2f}",
                    "custo_viagem": f"R$ {custo_da_viagem:.2f}",
                    "custo_total": custo_total
                })
            
            # Estrutura: Cálculo e exibição APÓS o loop
            if lista_resultados:
                melhor_opcao = min(lista_resultados, key=lambda x: x['custo_total'])

                st.subheader("🏆 Resultado da Análise")
                st.success(f"A melhor opção é o **{melhor_opcao['nome']}**!")
                
                with st.container(border=True):
                    st.metric(label="Custo Total Estimado", value=f"R$ {melhor_opcao['custo_total']:.2f}")
                    st.write(f"Preço por litro: {melhor_opcao['preco_litro']}")
                    st.write(f"Distância: {melhor_opcao['distancia']} (só ida)")
                    st.write(f"Custo estimado do deslocamento: {melhor_opcao['custo_viagem']}")
                
                for item in lista_resultados:
                    item['custo_total'] = f"R$ {item['custo_total']:.2f}"

                st.subheader("Comparativo Completo")
                st.dataframe(lista_resultados, hide_index=True)