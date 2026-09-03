from functools import reduce

def process_text(text):
    """
    Objetivo: Normalizar el texto sacando mayúsculas y signos
    Parametros: texto a limpiar (string)
    Salida: lista de palabras listas para comparar
    """
    words = text.lower().split()
    
    # map aplica el lambda para sacar los signos de las puntas de cada palabra
    words_without_signs = list(map(lambda w: w.strip(".,;:!?()¿¡"), words))
    
    # filter y lambda descartan los elementos que quedaron vacíos
    final_words = list(filter(lambda w: len(w) > 0, words_without_signs))
    
    return final_words

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