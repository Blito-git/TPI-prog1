from colorama import Fore, Style, init
init(autoreset=True)

import os
import readchar

def seleccionar_opcion_menu():
    opciones = [
        "Buscar país por nombre",
        "Filtrar países por continente",
        "Filtrar países por rango de población",
        "Filtrar países por rango de superficie",
        "Ordenar países",
        "Mostrar estadísticas",
        "Salir"
    ]
    seleccion = 0

    while True:
        limpiar_pantalla()
        print(Fore.CYAN + "===== MENÚ PRINCIPAL =====" + Style.RESET_ALL)
        for i, opcion in enumerate(opciones):
            if i == seleccion:
                print(Fore.YELLOW + f"> {i+1}. {opcion}" + Style.RESET_ALL)
            else:
                print(f"  {i+1}. {opcion}")

        tecla = readchar.readkey()

        if tecla == readchar.key.UP and seleccion > 0:
            seleccion -= 1
        elif tecla == readchar.key.DOWN and seleccion < len(opciones) - 1:
            seleccion += 1
        elif tecla == readchar.key.ENTER:
            return seleccion + 1


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_menu():
    print(Fore.CYAN + "===== MENÚ PRINCIPAL =====" + Style.RESET_ALL)
    print(Fore.YELLOW + "1." + Style.RESET_ALL + " Buscar país por nombre")
    print(Fore.YELLOW + "2." + Style.RESET_ALL + " Filtrar países por continente")
    print(Fore.YELLOW + "3." + Style.RESET_ALL + " Filtrar países por rango de población")
    print(Fore.YELLOW + "4." + Style.RESET_ALL + " Filtrar países por rango de superficie")
    print(Fore.YELLOW + "5." + Style.RESET_ALL + " Ordenar países")
    print(Fore.YELLOW + "6." + Style.RESET_ALL + " Mostrar estadísticas")
    print(Fore.RED + "7. Salir" + Style.RESET_ALL)
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
        limpiar_pantalla()
        inicio = pagina * elementos_por_pagina
        fin = inicio + elementos_por_pagina
        print(Fore.GREEN + f"\n--- Mostrando países (Página {pagina + 1} de {total_paginas}) ---\n" + Style.RESET_ALL)

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
            limpiar_pantalla()
            break
        else:
            print(Fore.RED + "Opción inválida. Intenta nuevamente." + Style.RESET_ALL)