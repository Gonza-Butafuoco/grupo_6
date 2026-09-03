import handler

def main():
    option = ""
    while option != "0":
        print("\n--- TextCompare ---")
        print("1) Cargar textos para comparar")
        print("0) Salir")
        
        option = input("Elegí una opción: ")

        if option == "1":
            handler.start_comparison()
        elif option == "0":
            print("Saliendo del sistema TextCompare...")
        else:
            print("Opción inválida. Por favor, ingresá 1 o 0.")

main()