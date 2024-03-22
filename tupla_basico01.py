#una tupla es un conjunto de valores
#es inmutable, esto es, lo elementos particulares no se pueden modificar
#pero si las tuplas se puede operar
t = (8,4)
print(t)
print(len(t))
r = t
print(t+r)
r += t
r += (9, 10)
print(r)

