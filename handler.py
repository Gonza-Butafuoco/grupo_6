import utils
import text_storage
import actions


    
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

    texts = text_storage.get_all_texts()

    if len(texts) >= 2:
        print("Ya hay 2 textos cargados.")
        print("Actualmente solo se pueden comparar 2 textos.")
        return

    name = input("Ingresá un nombre para el texto: ")

    text = read_multiline_text()

    if len(text.strip()) == 0:
        print("Error: El texto no puede estar vacío.")
        return

    text_storage.save_text(name, text)

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

    texts = text_storage.get_all_texts()

    if len(texts) < 2:
        print("Necesitás cargar 2 textos antes de compararlos.")
        return

    loaded_texts = list(texts.values())

    text1 = loaded_texts[0]
    text2 = loaded_texts[1]

    start_comparison(text1, text2)        
    
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

    if len(text1.strip()) == 0 or len(text2.strip()) == 0:
        print("Error: Uno o ambos textos están vacíos.")
        return

    data_of_text1 = utils.process_text(text1)
    data_of_text2 = utils.process_text(text2)

    matches = actions.find_matches(
        data_of_text1["normalized_text"],
        data_of_text2["normalized_text"]
    )

    similarity = actions.calculate_similarity(matches)

    print("\n+------------------------------+")
    print("|          RESULTADO           |")
    print("+------------------------------+")
    print(f"| Palabras en común: {matches['count_total_matches']} |")
    print(f"| Similitud: {similarity}%")
    print("+------------------------------+")
    
    # TODO: Mejorar el print de las coincidencias y armar
    # bien la logica del porcentaje en actions.py.    