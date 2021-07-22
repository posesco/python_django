def busca_pais(paises, pais):
    try:
        return paises[pais]
    except KeyError as e:
        print(f'Este es el error: {e}')
        return None