#conversión entre tupla y listas
t = (3, 56.8, "hola", [1,2,"w",5])
q = tuple(type(i) for i in t)
s = tuple(type(i).__name__ for i in t)
m = [type(i).__name__ for i in t]
print(q)
print(s)
print(m)