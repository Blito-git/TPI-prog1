from colorama import Fore, Style, init
init(autoreset=True)
from utils import mostrar_paises_paginados

def ordenar_paises(paises):
    print("Opciones de ordenamiento:")
    print("1. Por nombre")
    print("2. Por población")
    print("3. Por superficie")

    opcion = input("Seleccione una opción: ").strip()
    orden = input("Ascendente (A) o Descendente (D): ").strip().lower()
    reverse = True if orden == "d" else False

    if opcion == "1":
        key_func = lambda p: p["name"]["common"]
    elif opcion == "2":
        key_func = lambda p: p.get("population", 0)
    elif opcion == "3":
        key_func = lambda p: p.get("area", 0)
    else:
        print(Fore.RED + "Opción inválida." + Style.RESET_ALL)
        return

    paises_ordenados = sorted(paises, key=key_func, reverse=reverse)
    mostrar_paises_paginados(paises_ordenados)
