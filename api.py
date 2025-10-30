from colorama import Fore, Style, init
init(autoreset=True)
import requests
import csv
import os
import ast

ARCHIVO_CSV = "paises.csv"
BASE_URL = "https://restcountries.com/v3.1/all?fields=name,region,population,area"


def obtener_todos_paises():
    if os.path.exists(ARCHIVO_CSV):
        print(Fore.YELLOW + "📂 Cargando datos desde el archivo CSV local..." + Style.RESET_ALL)
        paises = leer_paises_csv()
        if paises:
            return paises
        else:
            print(Fore.RED + "⚠️ Error al leer el CSV. Intentando obtener datos desde la API..." + Style.RESET_ALL)

    print(Fore.YELLOW + "🌐 Descargando datos desde la API..." + Style.RESET_ALL)
    paises = obtener_datos_api()
    if paises:
        guardar_paises_csv(paises)
    return paises


def obtener_datos_api():
    try:
        response = requests.get(BASE_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        print(Fore.GREEN + "✅ Datos descargados correctamente desde la API." + Style.RESET_ALL)
        return data
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"❌ Error al obtener datos de la API: {e}" + Style.RESET_ALL)
        return []


def guardar_paises_csv(paises):
    try:
        with open(ARCHIVO_CSV, mode="w", newline="", encoding="utf-8") as archivo:
            campos = ["name", "population", "area", "region"]
            writer = csv.DictWriter(archivo, fieldnames=campos)
            writer.writeheader()

            for p in paises:
                nombre = "Desconocido"
                if isinstance(p.get("name"), dict):
                    nombre = p["name"].get("common", "Desconocido")
                elif isinstance(p.get("name"), str):
                    nombre = p["name"]

                writer.writerow({
                    "name": nombre,
                    "population": int(p.get("population", 0)),
                    "area": float(p.get("area", 0)),
                    "region": p.get("region", "Desconocido")
                })

        print(Fore.GREEN + f"💾 Datos guardados correctamente en '{ARCHIVO_CSV}'." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"❌ Error al guardar el archivo CSV: {e}" + Style.RESET_ALL)


def leer_paises_csv():
    paises = []
    try:
        with open(ARCHIVO_CSV, mode="r", encoding="utf-8") as archivo:
            reader = csv.DictReader(archivo)
            for fila in reader:
                nombre = fila.get("name", "Desconocido").strip()

                if nombre.startswith("{") and nombre.endswith("}"):
                    try:
                        parsed = ast.literal_eval(nombre)
                        if isinstance(parsed, dict) and "common" in parsed:
                            nombre = parsed["common"]
                        else:
                            nombre = str(parsed)
                    except Exception:
                        nombre = "Desconocido"

                pais = {
                    "name": {"common": nombre},
                    "population": int(float(fila.get("population", 0))),
                    "area": float(fila.get("area", 0)),
                    "region": fila.get("region", "Desconocido").strip()
                }
                paises.append(pais)

        return paises
    except Exception as e:
        print(Fore.RED + f"❌ Error al leer el archivo CSV: {e}" + Style.RESET_ALL)
        return []
