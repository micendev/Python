# Función que cuenta el número de veces que aparece cada palabra en un texto.

def count_words(text):

    text = text.split()
    words = {}
    for i in text:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words

def most_repeated(words):
    max_word = ''
    max_freq = 0
    for word, freq in words.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq
    return max_word, max_freq

text = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'

def result():
    print(count_words(text))
    print(most_repeated(count_words(text)))

if __name__ == "__main__":
    result()

# {'Como': 1, 'quieres': 1, 'que': 4, 'te': 1, 'quiera': 3, 'si': 1, 'el': 1, 'quiero': 2, 'me': 3, 'no': 1, 'quiere': 1, 'como': 1}
# ('que', 4)