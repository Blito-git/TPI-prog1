from colorama import Fore, Style, init
init(autoreset=True)
from utils import mostrar_paises_paginados

def buscar_pais(paises):
    termino = input(Fore.CYAN + "Ingrese el nombre del país (o parte del nombre): " + Style.RESET_ALL).lower()
    resultados = [p for p in paises if termino in p["name"]["common"].lower()]

    if not resultados:
        print(Fore.RED + "\nNo se encontraron coincidencias.\n" + Style.RESET_ALL)
        return

    # 🔹 Si hay pocos resultados, mostrar directamente sin paginación
    if len(resultados) <= 5:
        print(Fore.YELLOW + f"\nSe encontraron {len(resultados)} país(es):\n" + Style.RESET_ALL)
        for pais in resultados:
            nombre = pais.get("name", {}).get("common", "Desconocido")
            poblacion = pais.get("population", "N/A")
            region = pais.get("region", "N/A")
            print(f"{nombre:<30} | Población: {poblacion:<10} | Región: {region}")
        print()
    else:
        mostrar_paises_paginados(resultados)
