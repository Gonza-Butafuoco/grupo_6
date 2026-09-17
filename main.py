import handler


def main():
    option = ""

    while option != "0":
        print("\n------ ElPlagio ------")
        print("1) Cargar texto")
        print("2) Mostrar textos cargados")
        print("3) Comparar textos cargados")
        print("4) Comparar textos ahora")
        print("0) Salir")

        option = input("Elegí una opción: ")

        if option == "1":
            handler.load_text()

        elif option == "2":
            handler.show_texts()

        elif option == "3":
            handler.compare_loaded_texts()

        elif option == "4":
            handler.compare_texts_now()

        elif option == "0":
            print("Saliendo del sistema ElPlagio...")

        else:
            print("Opción inválida. Por favor, ingresá una opción entre 0 y 4.")


main()