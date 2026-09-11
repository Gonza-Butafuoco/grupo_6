
texts = {}

def save_text(name , text):
    """
    Objetivo: Guardar un texto en el diccionario de textos
    Parametros: nombre del texto (string), texto a guardar (string)
    Salida: Ninguna
    """
    texts[name] = text
    
def get_text(name):
    """
    Objetivo: Obtener un texto del diccionario de textos
    Parametros: nombre del texto (string)
    Salida: texto (string) o None si no existe
    """
    return texts.get(name)
        
def getall_texts():
    """
    Objetivo: Obtener todos los textos del diccionario de textos
    Parametros: Ninguno
    Salida: diccionario de textos
    """
    return texts

def delete_text(name):
    """
    Objetivo: Eliminar un texto del diccionario de textos
    Parametros: nombre del texto (string)
    Salida: Ninguna
    """
    if name in texts:
        del texts[name]
        return True
    
    return False




















