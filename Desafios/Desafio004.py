name = str( input ('Digite algo'))

print (('é um numero ou letra?'), (name.isalnum()))
print ('é do tipo letra? {}'.format(name.isalpha()))
print ('é apenas número? {}'.format(name.isnumeric()))
print ('são letras maiusculas? {}'.format(name.isupper()))
print ('são letras pequenas? {}'.format(name.islower()))
print ('são números decimais? {}'.format(name.isdecimal()))