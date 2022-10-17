lista=[1,2,5,10,20,81,33,28,5,3,9,83,94,81,2,97,84,1]
def modificar(lista):
    nueva_lista=[]
    for i in lista:
        if not i in nueva_lista:
            nueva_lista.append(i)
            nueva_lista=[nueva_lista.sort(reverse=True)]
            nueva_lista.append(i % 2==0)
            sum(nueva_lista)
        return nueva_lista
nueva_lista=modificar(lista)
print(nueva_lista[0]==sum(nueva_lista[1:]))


