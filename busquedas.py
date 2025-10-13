def buscar_pais(paises):
    termino = input("Ingrese el nombre del país (o parte del nombre): ").lower()
    resultados = [p for p in paises if termino in p["name"]["common"].lower()]

    if resultados:
        for p in resultados:
            print(f"- {p['name']['common']} | {p.get('region', 'Sin región')} | Población: {p.get('population', 'N/A')}")
    else:
        print("No se encontraron coincidencias.")