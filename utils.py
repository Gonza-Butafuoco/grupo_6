from functools import reduce
import re

def process_text(text):
    """
    Objetivo: Normalizar el texto sacando mayúsculas y signos
    Parametros: texto a limpiar (string)
    Salida: Diccionario con palabras y sus cantidades, o None si el texto es inválido
    """

    # Validación del texto
    if type(text) != str or not text.strip():
        return None

    repeated_words = {}
    
    #Pasamos a minuscula el texto
    text = text.lower()

    # Expresion regular que cumpla con los caracteres
    patron = r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]'
    textoNormalizado=re.sub(patron,'', text)

    #Separamos el texto
    words = textoNormalizado.split()
    
    # filter y lambda descartan los elementos que quedaron vacíos
    final_words = list(filter(lambda w: len(w) > 0, words))

    for word in final_words:
        repeated_words[word] = repeated_words.get(word, 0) + 1

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
