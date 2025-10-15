import os

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_menu():
    print("===== MENÚ PRINCIPAL =====")
    print("1. Buscar país por nombre")
    print("2. Filtrar países por continente")
    print("3. Filtrar países por rango de población")
    print("4. Filtrar países por rango de superficie")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Salir")
import csv

def guardar_paises_csv(paises, nombre_archivo="paises.csv"):
    if not paises:
        print("\n No hay datos para guardar.\n")
        return

    try:
        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
            campos = ["name", "population", "area", "region"]
            writer = csv.DictWriter(archivo, fieldnames=campos)
            writer.writeheader()

            for pais in paises:
                writer.writerow({
                    "name": pais.get("name", "N/A"),
                    "population": pais.get("population", "N/A"),
                    "area": pais.get("area", "N/A"),
                    "region": pais.get("region", "N/A")
                })

        print(f"\n Datos guardados automáticamente en '{nombre_archivo}'.\n")

    except Exception as e:
        print(f"\n Error al guardar el archivo CSV: {e}\n")
