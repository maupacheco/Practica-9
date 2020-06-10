from tuplas import nombretupla

juguete=nombretupla('juguete', ['nombre', 'numero'])
juguete1=juguete('Oso de peluche', 1)
print(juguete1)
juguete2=juguete2("Pelota", 2)
print(juguete2)
print(juguete1.nombre, juguete2.nombre)
print(juguete2[0], juguete2[1])