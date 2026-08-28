def loadUserTexts():
    first_text = str(input("Ingresá el primer texto: "))
    second_text = str(input("Ingresá el segundo texto: "))

    while first_text == "" or second_text == "":
        if first_text == "":
            first_text = str(input("Ingresá el primer texto: "))
        else:
            second_text = str(input("Ingresá el segundo texto: "))

    return [first_text, second_text]


def main():
    print("1) Cargar texto")

    texts = loadUserTexts()

    print(texts[0], texts[1])


main()