def calculate_similarity(list1, list2):
    """
    Objetivo: Calcular el porcentaje de similitud entre dos textos
    Parametros: dos listas de palabras
    Salida: numero flotante con el porcentaje
    """
    # TODO:  Acá hay que sacar el porcentaje real (0 a 100).
    # Como el alcance pide usar conjuntos, pueden convertir las listas a set()
    # y sacar la intersección para ver cuánto se parecen.
    new_list_1 = []
    for word in list1:
        if word not in new_list_1:
            new_list_1.append(word)
    
    new_list_2 = []
    for word in list2:
        if word not in new_list_2:
            new_list_2.append(word)
    
    #Si ambas listas están vacias, son iguales
    if len(new_list_1) == 0 and len(new_list_2) == 0:
        return 100.0
    
    #Contar palabras en común
    words_in_common = 0
    for word in new_list_1:
        if word in new_list_2:
            words_in_common += 1
    
    #Contar palabras unicas entre ambas listas
    total_words = len(new_list_1)
    for word in new_list_2:
        if word not in new_list_1:
            total_words += 1
    
    #Calcular porcentaje de similitud
    similarity_percentage = (words_in_common / total_words) * 100
    return round(similarity_percentage, 2)  # Redondeo a 2 decimales

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