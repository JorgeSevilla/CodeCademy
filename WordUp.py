pyg = 'ay'
original = raw_input('Enter a word: ')
word = original.lower()
first = word[0]

if len(original) > 0 and original.isalpha():
    print original
else:
    print 'empty'

print word
print first