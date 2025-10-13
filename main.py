from api import obtener_todos_paises
from busquedas import buscar_pais
from filtros import filtrar_por_continente, filtrar_por_poblacion, filtrar_por_superficie
from ordenamientos import ordenar_paises
from estadisticas import mostrar_estadisticas
from utils import limpiar_pantalla, mostrar_menu
from validaciones import validar_opcion

def main():
    paises = obtener_todos_paises()
    if not paises:
        print("No se pudieron obtener los datos.")
        return

    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if not validar_opcion(opcion):
            input("Opción inválida. Presione Enter para continuar...")
            continue

        limpiar_pantalla()

        if opcion == "1":
            buscar_pais(paises)
        elif opcion == "2":
            filtrar_por_continente(paises)
        elif opcion == "3":
            filtrar_por_poblacion(paises)
        elif opcion == "4":
            filtrar_por_superficie(paises)
        elif opcion == "5":
            ordenar_paises(paises)
        elif opcion == "6":
            mostrar_estadisticas(paises)
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        
        input("\nPresione Enter para volver al menú...")

if __name__ == "__main__":
    main()
    