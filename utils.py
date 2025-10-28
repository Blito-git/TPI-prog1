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
def mostrar_paises_paginados(paises, elementos_por_pagina=10):
    if not paises:
        print("\nNo hay países para mostrar.\n")
        return

    total = len(paises)
    pagina = 0
    total_paginas = (total - 1) // elementos_por_pagina + 1

    while True:
        inicio = pagina * elementos_por_pagina
        fin = inicio + elementos_por_pagina
        print(f"\n--- Mostrando países (Página {pagina + 1} de {total_paginas}) ---\n")

        for i, pais in enumerate(paises[inicio:fin], start=inicio + 1):
            nombre = pais.get("name", {}).get("common", "Desconocido")
            poblacion = pais.get("population", "N/A")
            region = pais.get("region", "N/A")
            print(f"{i}. {nombre:<30} | Población: {poblacion:<10} | Región: {region}")

        print("\nOpciones:")
        if pagina > 0:
            print(" [A] Anterior")
        if pagina < total_paginas - 1:
            print(" [S] Siguiente")
        print(" [Q] Salir de la lista")

        opcion = input("Elige una opción: ").strip().lower()

        if opcion == "s" and pagina < total_paginas - 1:
            pagina += 1
        elif opcion == "a" and pagina > 0:
            pagina -= 1
        elif opcion == "q":
            break
        else:
            print("Opción inválida. Intenta nuevamente.")