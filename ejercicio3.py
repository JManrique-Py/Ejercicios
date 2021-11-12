poema = """
Arde en tus ojos un misterio, virgen
esquiva y compañera.
No sé si es odio o es amor la lumbre
inagotable de tu aliaba negra.

Conmigo irás mientras proyecte sombra
mi cuerpo y quede a mi sandalia arena.
-¿Eres la sed o el agua en mi camino?-
Dime, virgen esquiva y compañera.

"""
# determinar el numero de veces que se repite a,e,i,o,u
# reemplace la palabra amor por hambre, ojos por deintes
# coloque todas las letras en mayuscula
# revierta el texto
n = poema.count('a') + poema.count('e') + poema.count('i') + poema.count('o') + poema.count('u') + poema.count('á')
print(n)
poema = poema.replace('amor','hambre')
poema = poema.replace('ojos','dientes')

poema = poema.upper()
a=''
for i in range (0,len(poema)):
    a=a+poema[len(poema)-1-i]

print(a)
