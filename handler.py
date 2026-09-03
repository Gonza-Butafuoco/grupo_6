import utils
import actions

def start_comparison():
    """
    Objetivo: Gestionar la carga de textos y orquestar la comparación
    Parametros: Ninguno
    Salida: Ninguna
    """
    print("\n--- Carga de Textos ---")
    text1 = input("Pegá el primer texto: ")
    text2 = input("Pegá el segundo texto: ")

    if len(text1) == 0 or len(text2) == 0:
        print("Error: Uno o ambos textos están vacíos.")
        return 

    list1 = utils.process_text(text1)
    list2 = utils.process_text(text2)
    
    matches = actions.find_matches(list1, list2)
    similarity = actions.calculate_similarity(list1, list2)
    
    print(f"\nSe encontraron {len(matches)} palabras en común.")
    print(f"Palabras: {matches}")
    print(f"Porcentaje de similitud: {similarity}%")
    
    # TODO: Mejorar el print de las coincidencias y armar
    # bien la logica del porcentaje en actions.py.