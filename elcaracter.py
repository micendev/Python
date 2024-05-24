
#  * Crea una función que reciba dos cadenas de texto casi iguales,
#  * a excepción de uno o varios caracteres. 
#  * La función debe encontrarlos y retornarlos en formato lista/array.
#  * - Ambas cadenas de texto deben ser iguales en longitud.
#  * - Las cadenas de texto son iguales elemento a elemento.
#  * - No se pueden utilizar operaciones propias del lenguaje
#  *   que lo resuelvan directamente.

def infiltrated_characters(first_text: str, second_text:str) -> list:

    characters = []

    if len(first_text) == len(second_text):
        
        for i in range(0, len(first_text)):
            if first_text[i] != second_text[i]:
                characters.append(second_text[i])
                
    else:
        print("Las cadenas de texto deben ser iguales")

    return characters


print(infiltrated_characters("Me llamo Pablo Perez", "Me llemo Pablo Peres"))
print(infiltrated_characters("Una playa linda", "Una playa linde "))
 
 