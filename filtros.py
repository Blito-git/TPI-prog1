from colorama import Fore, Style, init
init(autoreset=True)

from utils import mostrar_paises_paginados

def filtrar_por_continente(paises):
    continente = input(Fore.CYAN + "Ingrese el continente (Africa, Americas, Asia, Europe, Oceania): " + Style.RESET_ALL).capitalize()
    filtrados = [p for p in paises if p.get("region") == continente]

    if filtrados:
        mostrar_paises_paginados(filtrados)
    else:
        print(Fore.RED + "No se encontraron países en ese continente." + Style.RESET_ALL)

def filtrar_por_poblacion(paises):
    try:
        minimo = int(input("Población mínima: "))
        maximo = int(input("Población máxima: "))
        filtrados = [p for p in paises if minimo <= p.get("population", 0) <= maximo]

        if filtrados:
            mostrar_paises_paginados(filtrados)
        else:
            print(Fore.RED + "No se encontraron países en ese rango." + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "Error: Ingrese valores numéricos." + Style.RESET_ALL)

def filtrar_por_superficie(paises):
    try:
        minimo = float(input("Superficie mínima (km²): "))
        maximo = float(input("Superficie máxima (km²): "))
        filtrados = [p for p in paises if minimo <= p.get("area", 0) <= maximo]

        if filtrados:
            mostrar_paises_paginados(filtrados)
        else:
            print(Fore.RED + "No se encontraron países en ese rango." + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "Error: Ingrese valores numéricos." + Style.RESET_ALL)
