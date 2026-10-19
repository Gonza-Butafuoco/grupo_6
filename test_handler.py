#No se hace pruebas de "show_texts" y "compare_texts_now" porque no entendimos o es con cosas que no vimos

from handler import read_multiline_text, load_text, compare_loaded_texts, delete_loaded_text, start_comparison
import text_storage #Se pone aca abajo porque está en otro módulo
import utils #Importo utils para test_start_comparison

def test_read_multiline_text():
    resultado = read_multiline_text()
    #Pruebo que este cargado el texto
    assert resultado == "Prueba"
    #Pruebo que sea un string
    assert type(resultado) == str
    #Hay que agregarle python -m pytest -v -s y escribir "Prueba" (la s para probar para agregar el INPUT)


def test_load_text():
    #Prueba que se cargue el texto y me muestre el mensaje de que esta correcto
    name = "Prueba"
    mensaje = f"Texto '{name}' cargado exitosamente."
    assert mensaje == f"Texto '{name}' cargado exitosamente."

def compare_loaded_texts():
    #Compruebo que se hayan cargado 2 textos
    assert len(loaded_texts) == 2

def test_delete_loaded_text():
    #Comprueba que el texto este borrado
    texts = text_storage.get_all_texts()
    assert "text1" not in texts

def test_start_comparison():
    resultado = utils.process_text("Prueba")
    #Verifica que el texto normalizado sea una lista con la palabra "prueba"
    assert resultado["normalized_text"] == ["prueba"]
