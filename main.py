import handler

def main():
    option = ""
    while option != "0":
        print("\n------ElPlagio --------")
        print("1) Cargar textos ")
        print("2) Mostrar textos cargados")
        print("3) Comparar textos")
        print("0) Salir")
        
        option = input("Elegí una opción: ")

        if option == "1":
            handler.load_text()
        elif option == "2":
            handler.show_texts()
        elif option == "3":
            handler.start_comparison()
        elif option == "0":
            print("Saliendo del sistema ElPlagio...")
        else:
            print("Opción inválida. Por favor, ingresá 1 o 0.")

main()