from functools import reduce
import re

def process_text(text):
    """
    Objetivo: Normalizar el texto sacando mayúsculas y signos
    Parametros: texto a limpiar (string)
    Salida: Diccionario con lista de palabras finales y diccionario de la cantidad de veces que se repite las palabras
    """

    repeated_words = {}
    
    words = text.lower().split()

    # Expresion regular que cumpla con los caracteres
    patron = r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]'
    textoNormalizado=re.sub(patron,'', words)
    
    # filter y lambda descartan los elementos que quedaron vacíos
    final_words = list(filter(lambda w: len(w) > 0, textoNormalizado))

    for word in final_words:
        repeated_words[word] = repeated_words.get[word, 0] + 1

    return {
        "normalized_text": final_words,
        "repeated_words": repeated_words
    }


def sum_total_words(list1, list2):
    """
    Objetivo: Obtener la cantidad de palabras de ambos textos usando reduce
    Parametros: las dos listas de palabras ya procesadas
    Salida: cantidad total de palabras (entero)
    """
    amounts = [len(list1), len(list2)]
    
    # reduce aplica el lambda acumulativamente para sumar los elementos
    total = reduce(lambda a, b: a + b, amounts)
    
    return total