def calculate_similarity(list1, list2):
    """
    Objetivo: Calcular el porcentaje de similitud entre dos textos
    Parametros: dos listas de palabras
    Salida: numero con el porcentaje
    """
    # TODO:  Acá hay que sacar el porcentaje real (0 a 100).
    # Como el alcance pide usar conjuntos, pueden convertir las listas a set()
    # y sacar la intersección para ver cuánto se parecen.
    
    return 0.0

def find_matches(list1, list2):
    """
    Objetivo: Identificar palabras que se repiten en ambos textos
    Parametros: dos listas de palabras
    Salida: lista con palabras repetidas
    """
    matches = []
    
    for word in list1:
        if word in list2 and word not in matches:
            matches.append(word)
            
    return matches