# api_handler.py

def buscar_postos_proximos(latitude , longitude):
    """
    Esta função SIMULA uma chamada de API.
    Ela não acessa a internet, apenas retorna uma lista fixa de postos.
    """
    print(f'--- Simulando busca de posto para LAT: {latitude} e LON: {longitude} ---')
    return{
        "resultados":[
            {
                "name": "Posto Ipiranga (Mock)",
                "vicinity": "Avenida Brasil, 123, Rio de Janeiro",
                "geometry": {"location": {"lat": -22.9068, "lng": -43.1729}},
            },
            {
                "name": "Posto Shell (Mock)",
                "vicinity": "Rua Augusta, 456, São Paulo",
                "geometry": {"location": {"lat": -23.5505, "lng": -46.6333}},
            },
            {
                "name": "Posto BR (Mock)",
                "vicinity": "Praça da Sé, 789, Salvador",
                "geometry": {"location": {"lat": -12.9747, "lng": -38.4767}},
            }
        ],
        "status":"OK"
    }
# api_handler.py
from math import radians, sin, cos, sqrt, atan2

def calcular_distancia(lat1, lon1, lat2, lon2):
    # Raio da Terra em km
    R = 6371.0

    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)

    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distancia = R * c
    return distancia