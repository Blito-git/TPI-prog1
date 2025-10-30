from colorama import Fore, Style, init
init(autoreset=True)

def mostrar_estadisticas(paises):
    poblaciones = [p.get("population", 0) for p in paises if "population" in p]
    superficies = [p.get("area", 0) for p in paises if "area" in p]

    if not poblaciones or not superficies:
        print(Fore.RED + "No hay datos suficientes." + Style.RESET_ALL)
        return

    pais_mayor_poblacion = max(paises, key=lambda p: p.get("population", 0))
    pais_menor_poblacion = min(paises, key=lambda p: p.get("population", 0))

    promedio_poblacion = sum(poblaciones) / len(poblaciones)
    promedio_superficie = sum(superficies) / len(superficies)

    print(Fore.CYAN + "📊 ESTADÍSTICAS GENERALES" + Style.RESET_ALL)
    print(f"- País con mayor población: {pais_mayor_poblacion['name']['common']} ({pais_mayor_poblacion['population']})")
    print(f"- País con menor población: {pais_menor_poblacion['name']['common']} ({pais_menor_poblacion['population']})")
    print(f"- Promedio de población: {promedio_poblacion:,.0f}")
    print(f"- Promedio de superficie: {promedio_superficie:,.0f} km²")

    continentes = {}
    for p in paises:
        region = p.get("region", "Desconocido")
        continentes[region] = continentes.get(region, 0) + 1

    print(Fore.CYAN + "\n🌍 Cantidad de países por continente:" + Style.RESET_ALL)
    for c, cantidad in continentes.items():
        print(f"- {c}: {cantidad}")