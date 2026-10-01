import utils
import text_storage
import actions
from exceptions import EmptyTextError, NotEnoughTextsError, TextLimitError, TextNotFoundError


    
def read_multiline_text():
    """
    Objetivo: Permitir al usuario ingresar un texto de varias líneas
    Parametros: Ninguno
    Salida: texto ingresado (string)
    """
    print("\nPega el texto.")
    print('cuando termunes de escribir el texto , ingresa la palabra FIN en una linea separada: \n')
    
    lines = []
    
    line = input() 
    
    while line.strip() != 'FIN':
        lines.append(line)
        line = input()
        
    return "\n".join(lines)

def load_text():
    """
    Objetivo: Gestionar la carga de un texto y guardarlo en el diccionario de textos
    Parametros: Ninguno
    Salida: Ninguna
    """

    name = input("Ingresá un nombre para el texto: ")
    text = read_multiline_text()

    try:
        text_storage.save_text(name, text)
    except (EmptyTextError, TextLimitError) as error:
        print(f"Error: {error}")
    else:
        print(f"Texto '{name}' cargado exitosamente.")
    
def show_texts():
    texts = text_storage.get_all_texts()
    
    if len(texts) == 0:
        print("No hay textos cargados.")
        return
    
    print("\n--- Textos Cargados ---")
    
    for name , text in texts.items():
        print('Nombre del texto:')
        print(f"- {name}")
        print("Texto:")
        print(f"- {text}")
        print("------------------------------")
        
def compare_loaded_texts():
    """
    Objetivo: Comparar los dos textos previamente cargados
    Parametros: Ninguno
    Salida: Ninguna
    """

    try:
        text1, text2 = text_storage.get_texts_for_comparison()
    except NotEnoughTextsError as error:
        print(f"Error: {error}")
        return

    start_comparison(text1, text2)


def delete_loaded_text():
    """Elimina uno de los textos cargados por su nombre."""
    name = input("Ingresá el nombre del texto a eliminar: ")

    try:
        text_storage.delete_text(name)
    except TextNotFoundError as error:
        print(f"Error: {error}")
    else:
        print(f"Texto '{name}' eliminado correctamente.")
    
def compare_texts_now():
    """
    Objetivo: Cargar dos textos y compararlos directamente sin guardarlos
    Parametros: Ninguno
    Salida: Ninguna
    """

    print("\n--- Primer texto ---")
    text1 = read_multiline_text()

    print("\n--- Segundo texto ---")
    text2 = read_multiline_text()

    start_comparison(text1, text2)


def start_comparison(text1, text2):
    """
    Objetivo: Orquestar la comparación entre dos textos.
    Parametros:
        text1: primer texto a comparar
        text2: segundo texto a comparar
    Salida: Ninguna
    """

    try:
        data_of_text1 = utils.process_text(text1)
        data_of_text2 = utils.process_text(text2)
    except (TypeError, ValueError) as error:
        print(f"Error procesando los textos: {error}")
        return

    matches = actions.find_matches(
        data_of_text1["normalized_text"],
        data_of_text2["normalized_text"]
    )

    similarity = actions.calculate_similarity(matches)
    summary = actions.build_comparison_summary(matches, similarity)
    common_words, unique_words, similarity_percentage = summary

    print("\n+------------------------------+")
    print("|          RESULTADO           |")
    print("+------------------------------+")
    print(f"| Palabras en común: {common_words} |")
    print(f"| Palabras únicas: {unique_words} |")
    print(f"| Similitud: {similarity_percentage}%")
    print(f"| Solo en texto 1: {', '.join(sorted(matches['only_text1'])) or '-'}")
    print(f"| Solo en texto 2: {', '.join(sorted(matches['only_text2'])) or '-'}")
    print("+------------------------------+")
