import requests

BASE_URL = "https://restcountries.com/v3.1/all?fields=name,region,population,area,capital,subregion"

def obtener_todos_paises():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error al obtener datos:", e)
        return None