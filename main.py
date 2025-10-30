from colorama import Fore, Style, init
init(autoreset=True)

from api import obtener_todos_paises
from busquedas import buscar_pais
from filtros import filtrar_por_continente, filtrar_por_poblacion, filtrar_por_superficie
from ordenamientos import ordenar_paises
from estadisticas import mostrar_estadisticas
from utils import limpiar_pantalla, guardar_paises_csv, seleccionar_opcion_menu


def main():
    paises = obtener_todos_paises()
    guardar_paises_csv(paises)

    if not paises:
        print(Fore.RED + "❌ No se pudieron obtener los datos." + Style.RESET_ALL)
        return

    while True:
        opcion = seleccionar_opcion_menu()
        limpiar_pantalla()

        if opcion == 1:
            buscar_pais(paises)
        elif opcion == 2:
            filtrar_por_continente(paises)
        elif opcion == 3:
            filtrar_por_poblacion(paises)
        elif opcion == 4:
            filtrar_por_superficie(paises)
        elif opcion == 5:
            ordenar_paises(paises)
        elif opcion == 6:
            mostrar_estadisticas(paises)
        elif opcion == 7:
            print(Fore.RED + "\n👋 Saliendo del programa..." + Style.RESET_ALL)
            break

        input(Fore.CYAN + "\nPresione Enter para volver al menú..." + Style.RESET_ALL)


if __name__ == "__main__":
    main()
