
texts = {}

def save_text(name , text):
    """
    Objetivo: Guardar un texto en el diccionario de textos
    Parametros: nombre del texto (string), texto a guardar (string)
    Salida: True si se guardó el texto, False si no cumple las validaciones
    """
    if type(text) != str or not text.strip():
        return False

    if len(texts) >= 2 and name not in texts:
        return False

    texts[name] = text
    return True
    
def get_text(name):
    """
    Objetivo: Obtener un texto del diccionario de textos
    Parametros: nombre del texto (string)
    Salida: texto (string) o None si no existe
    """
    return texts.get(name)
        
def get_all_texts():
    """
    Objetivo: Obtener todos los textos del diccionario de textos
    Parametros: Ninguno
    Salida: diccionario de textos
    """
    return texts


def get_texts_for_comparison():
    """Devuelve los textos disponibles; el handler maneja los índices faltantes."""
    return tuple(texts.values())

def delete_text(name):
    """
    Objetivo: Eliminar un texto del diccionario de textos
    Parametros: nombre del texto (string)
    Salida: True si se eliminó el texto, False si el nombre no existe
    """
    if name in texts:
        del texts[name]
        return True

    return False




















