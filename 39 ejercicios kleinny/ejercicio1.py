#A) Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. Finalizar al ingresar el número 0, el cual no debe guardarse.
#B) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
#C) Recorrer la lista para imprimir la sumatoria de todos los elementos.
#D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
#E) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]

def sumatoria_kmdt(lista):
    suma_kmdt=0
    for n in lista:
        suma_kmdt+=n
    return suma_kmdt

def NumerosMenores_kmdt(lista, limite):
    nueva_kmdt=[]
    for n in lista:
        if n<limite:
            nueva_kmdt.append(n)
    return nueva_kmdt

def frecuencias_kmdt(lista):
    nueva_kmdt1=[]
    for n in lista:
        if [n, lista.count(n)] not in nueva_kmdt1:
            nueva_kmdt1.append([n, lista.count(n)])
    return nueva_kmdt1

#A
numeros_kmdt=[]
nro=int(input("Número: "))
while nro!=0:
    numeros_kmdt.append(nro)
    nro=int(input("Número: "))
#B
print("Sumatoria de los números:", sumatoria_kmdt(numeros_kmdt))
eliminar_kmdt=int(input("Número a eliminar: "))
#C
if eliminar_kmdt in numeros_kmdt:
    numeros_kmdt.remove(eliminar_kmdt)
else:
    print("Ese número no está entre los ingresados")
#D
limite=int(input("Filtrar números menores a: "))
for n in NumerosMenores_kmdt(numeros_kmdt, limite):
    print(n)
#E
print("Frecuencias:")
for tupla in frecuencias_kmdt(numeros_kmdt):
    print(tupla[0],"aparece",tupla[1],"veces.")