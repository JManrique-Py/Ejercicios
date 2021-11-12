#Cree una lista con números multiplos de 3 hasta el 100, imprimalos en pantalla
# invierta la lista
# Elimine los ultimos 3 elementos de la anterior lista
# cree una copia de la lista, elimine el ultimo valor y agregue su edad en esta misma posición
lista = [i for i in range(3,100,3)]
print(lista)

listaReverse = lista.copy()
listaReverse.reverse()
print(listaReverse)

listaReverse = listaReverse[0:-3]
print(listaReverse)

listaCopia = listaReverse.copy()
listaCopia.pop()
listaCopia.append(16)
print(listaCopia)
