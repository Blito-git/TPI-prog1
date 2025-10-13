def filtrar_por_continente(paises):
    continente = input("Ingrese el continente (Africa, Americas, Asia, Europe, Oceania): ").capitalize()
    filtrados = [p for p in paises if p.get("region") == continente]

    if filtrados:
        for p in filtrados:
            print(f"- {p['name']['common']} | {p['region']}")
    else:
        print("No se encontraron países en ese continente.")

def filtrar_por_poblacion(paises):
    try:
        minimo = int(input("Población mínima: "))
        maximo = int(input("Población máxima: "))
        filtrados = [p for p in paises if minimo <= p.get("population", 0) <= maximo]

        if filtrados:
            for p in filtrados:
                print(f"- {p['name']['common']} | Población: {p['population']}")
        else:
            print("No se encontraron países en ese rango.")
    except ValueError:
        print("Error: Ingrese valores numéricos.")

def filtrar_por_superficie(paises):
    try:
        minimo = float(input("Superficie mínima (km²): "))
        maximo = float(input("Superficie máxima (km²): "))
        filtrados = [p for p in paises if minimo <= p.get("area", 0) <= maximo]

        if filtrados:
            for p in filtrados:
                print(f"- {p['name']['common']} | Superficie: {p.get('area', 'N/A')} km²")
        else:
            print("No se encontraron países en ese rango.")
    except ValueError:
        print("Error: Ingrese valores numéricos.")