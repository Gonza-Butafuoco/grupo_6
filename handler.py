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
    name = input("Ingresá un nombre para el texto: ")
    
    text = read_multiline_text()
    
    text_storage.save_text(name, text)
    
    print(f"Texto '{name}' cargado exitosamente.")
    
def show_texts():
    texts = text_storage.getall_texts()
    
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


def start_comparison():
    """
    Objetivo: Gestionar la carga de textos y orquestar la comparación
    Parametros: Ninguno
    Salida: Ninguna
    """
    #utilizar load Text ahora que ya tenemos la funcion para cargar textos
    
    # print("\n--- Carga de Textos ---")
    # text1 = input("Pegá el primer texto: ")
    # text2 = input("Pegá el segundo texto: ")

    # if len(text1) == 0 or len(text2) == 0:
    #     print("Error: Uno o ambos textos están vacíos.")
    #     return 

    dataOfText1 = utils.process_text(text1)
    dataOfText2 = utils.process_text(text2)
    
    matches = actions.find_matches(dataOfText1["normalized_text"], dataOfText2["normalized_text"])

    #TODO: ahora calculate_similarity, deberia de recibir 'matches' tambien ya que hace toda la logica de deduplicacion
    similarity = actions.calculate_similarity(matches)
    
    print("\n+------------------------------+")
    print("|       RESULTADO             |")
    print("+------------------------------+")
    print(f"| Palabras en común: {matches["count_total_matches"]} |")
    print(f"Similitud: {similarity}%")
    print("+------------------------------+")
    
    # TODO: Mejorar el print de las coincidencias y armar
    # bien la logica del porcentaje en actions.py.    