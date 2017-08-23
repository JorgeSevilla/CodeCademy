# Write an if statement that verifies that the string has characters.
# Add an if statement that checks that len(original) is greater than zero.
# Don't forget the : at the end of the if statement!
# If the string actually has some characters in it, print the user's word.
# Otherwise (i.e. an else: statement), please print "empty".
# Use and to add a second condition to your if statement.
# In addition to your existing check that the string contains characters, you should also use .isalpha()
# to make sure that it only contains letters.
# Don't forget to keep the colon at the end of the if statement!


name = raw_input("Ingrese su nombre: ")
# x = "J123"
# x.isalpha()

if len(name) > 0 and name.isalpha():
    print name
else:
    print "Necesita ingresar numeros"
