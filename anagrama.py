def main():
    palabra1 = input("Escriba una palabra: ")
    palabra2 = input("Escriba otra palabra: ")

    if es_anagrama(palabra1.lower(), palabra2.lower()):
        print("Las palabras son anagramas")
    else:
        print("No son anagramas")


def es_anagrama(p1, p2):
    for l in p1:
        if l in p2:
            pass
        else:
            return False
    for l in p2:
        if l in p1:
            pass
        else:
            return False
    if len(p1) == len(p2):
        return True


if __name__ == "__main__":
    main()