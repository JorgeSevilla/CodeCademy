the_string = "Hello"
the_string = the_string.lower()

pyg = 'ay'
original = raw_input('Enter a word: ')
word = original.lower()
first = word[0]
new_word = first + word + pyg

if len(original) > 0 and original.isalpha():
    print original
else:
    print 'empty'

print word
print first
print new_word
