
from exceptions import (
    EmptyTextError,
    NotEnoughTextsError,
    TextLimitError,
    TextNotFoundError,
)


texts = {}

def save_text(name , text):
    """
    Objetivo: Guardar un texto en el diccionario de textos
    Parametros: nombre del texto (string), texto a guardar (string)
    Salida: Ninguna
    """
    if not isinstance(text, str) or not text.strip():
        raise EmptyTextError("El texto no puede estar vacío.")

    if len(texts) >= 2 and name not in texts:
        raise TextLimitError("Solo se pueden guardar dos textos.")

    texts[name] = text
    
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
    """Obtiene los dos textos cargados como una tupla desempaquetable."""
    if len(texts) < 2:
        raise NotEnoughTextsError(
            "Necesitás cargar 2 textos antes de compararlos."
        )

    return tuple(texts.values())

def delete_text(name):
    """
    Objetivo: Eliminar un texto del diccionario de textos
    Parametros: nombre del texto (string)
    Salida: Ninguna
    """
    if name not in texts:
        raise TextNotFoundError(f"No existe un texto llamado '{name}'.")

    del texts[name]




















