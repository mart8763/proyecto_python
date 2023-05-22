

numero = [10,50,100,155,500]
#append = agregar un objto en la ultima posicion 
numero.append(1000)
print(numero)
#estend = agrega un arreglo al final de nuetra lista
extra=[75,350,999]
numero.extend(extra)
print(numero)
#insert = agregar valor en posicion especifica
numero.insert(6,5000)
print(numero)
#remove = entrega valor, se busca y se borra
numero.remove(50)
print(numero)
#pop = elimina el ultimo registro
#pop (i) = elimina la posicion del numero 
numero.pop()
print(numero)
numero.pop(3)
print(numero)
#reverse = invierte orden de la lista
numero.reverse()
print(numero)
#sort = ordena los valores de menor a mayor 
#sort(reverse=true) = ordena los valores de mayor a menor 
numero.sort()
print(numero)
numero.sort(reverse=True)
print(numero)