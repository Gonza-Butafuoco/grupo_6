def calculate_similarity(list1, list2):
    """
    Objetivo: Calcular el porcentaje de similitud entre dos textos
    Parametros: dos listas de palabras
    Salida: numero flotante con el porcentaje
    """
    # TODO:  Acá hay que sacar el porcentaje real (0 a 100).
    # Como el alcance pide usar conjuntos, pueden convertir las listas a set()
    # y sacar la intersección para ver cuánto se parecen.
    new_unique_list_1 = []
    for word in list1:
        if word not in new_unique_list_1:
            new_unique_list_1.append(word)
    
    new_unique_list_2 = []
    for word in list2:
        if word not in new_unique_list_2:
            new_unique_list_2.append(word)
    
    #Contar palabras en común
    words_in_common = 0
    for word in new_unique_list_1:
        if word in new_unique_list_2:
            words_in_common += 1
    
    #Contar palabras unicas entre ambas listas
    total_words = len(new_unique_list_1) + len(new_unique_list_2) - words_in_common
    
    #En caso que la división sea por cero, se retorna 0
    if total_words == 0:
        return 0.0
    
    #Calcular porcentaje de similitud
    porcentaje_similitud = (words_in_common / total_words) * 100
    
    return round(porcentaje_similitud,2)

def find_matches(list1, list2):
    """
    Objetivo: Identificar palabras que se repiten en ambos textos
    Parametros: dos listas de palabras
    Salida: Diccionario con repetidas, cuenta total de palabras repetidas y cuenta total de palabras unicas
    """
    matches = []

    for word in list1:
        if word in list2 and word not in matches:
            matches.append(word)
            
    return {
        "matches": matches,
        "count_total_matches": len(matches),
        "count_unique_words": (len(list1) + len(list2)) - len(matches)
    }