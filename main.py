def lower_text(text):
    new_text = text.lower()
    
    return new_text


def new_diccionario(lista_words):
    new_dict = dict()
    palabras = set(lista_words)
    
    for i in lista_words:
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1
       
    return new_dict

def diccionario_sort(diccionario):
    new_diccionario = {}
        
    for i in diccionario:
        if i == 'a' or i == 'b' or i == 'c' or i == 'd' or i == 'e' or i == 'f' or i == 'g' or i == 'h' or i == 'i' or i == 'j' or i == 'k' or i == 'l' or i == 'm' or i == 'n' or i == 'o' or i == 'p' or i == 'q' or i == 'r' or i == 's' or i == 't' or i == 'u' or i == 'v' or i == 'w' or i == 'x' or i == 'z':
            if i in new_diccionario:
                new_diccionario[i] += 1
            else:
                new_diccionario[i] = 1
       
    return new_diccionario
        
def  printeo(resultado,conteo):
    print("--- Begin report of books/frankenstein.txt ---")
    print(conteo, "words found in the document")
    print("\n")
    for key in resultado:
        print(f"The '{key}' character was found {resultado[key]} times")
       
    print("\n--- End report ---")

def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()

    low_text = lower_text(file_contents)

    lista_words = low_text.split()
    lista_letras = list(low_text)
    lista_let = diccionario_sort(lista_letras)

    printeo(lista_let,len(lista_words))
    
main()








