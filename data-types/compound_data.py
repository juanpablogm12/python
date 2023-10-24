# se puede modificar
list = ["juan", True, 132]
print(list[0])


# no se puede mutar
tupla = ("juan", True, 132)
print(tupla[0])

tupla = ("prueba")

# conjunto (set) no puedo acceder por el indice, tampoco se puede mutar no repite valores
conjunto = {"juan", True, 132}


#  diccionario (dict)
diccionario = {
    "nombre": "juan",
    "edad": 27
}