# -*- coding: utf-8 -*-
pyg = 'ay'
original = raw_input('Enter a word: ')

if len(original) > 0 and original.isalpha():
    # Convierte en minúscula
    word = original.lower()
    # Asigna la posición
    first = word[0]
    # Agrega cadena con el sufijo 'ay'
    new_word = word + first + pyg
    # Lee la cadena omitiendo la primera letra
    new_word = new_word[1:len(new_word)]
    # Imprime resultado
    print original
    print new_word
else:
    print 'empty'

# Pruebas Unitarias
#print word
#print first
#print new_word

