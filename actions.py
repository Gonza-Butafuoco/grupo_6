def calculate_similarity(dataOfMatches):
    """
    Objetivo: Calcular el porcentaje de similitud entre dos textos
    Parametros: diccionario con la cantidad de palabras en común y la cantidad de palabras únicas.
    Salida: numero flotante con el porcentaje
    """
    # TODO:  Acá hay que sacar el porcentaje real (0 a 100).
    # Como el alcance pide usar conjuntos, pueden convertir las listas a set()
    # y sacar la intersección para ver cuánto se parecen.
    total_matches = dataOfMatches["count_total_matches"]
    total_unique_words = dataOfMatches["total_unique_words"]
    
    if total_unique_words == 0:
        return 0.0
    
    similarity_percentage = (total_matches / total_unique_words) * 100
    return round(similarity_percentage, 2)

def find_matches(text1, text2):
    """
    Objetivo: Identificar palabras que se repiten en ambos textos
    Parametros: dos listas de palabras
    Salida: Diccionario con repetidas, cuenta total de palabras repetidas y cuenta total de palabras unicas
    """
    set_of_text1 = set(text1)
    set_of_text2 = set(text2)
    matches = set_of_text1.intersection(set_of_text2)
    only_text1 = set_of_text1.difference(set_of_text2)
    only_text2 = set_of_text2.difference(set_of_text1)
    unique_words = set_of_text1.union(set_of_text2)
            
    return {
        "matches": matches,
        "only_text1": only_text1,
        "only_text2": only_text2,
        "count_total_matches": len(matches),
        "list_unique_words": unique_words,
        "total_unique_words": len(unique_words)
    }


def build_comparison_summary(matches, similarity):
    """Devuelve una tupla inmutable con el resumen de una comparación."""
    return (
        matches["count_total_matches"],
        matches["total_unique_words"],
        similarity,
    )
