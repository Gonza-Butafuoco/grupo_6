import handler

def main():
    while True:
        print("\n--- TextCompare ---")
        print("1) Cargar textos para comparar")
        print("2) Salir")
        
        option = input("Elegí una opción: ")

        if option == "1":
            handler.start_comparison()
        elif option == "2":
            print("Saliendo del sistema TextCompare...")
            break
        else:
            print("Opción inválida. Por favor, ingresá 1 o 2.")

main()