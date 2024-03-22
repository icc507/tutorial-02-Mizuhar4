#conversión entre tupla y listas
t = (3, 56.8, "hola", [1,2,"w",5])
k = list(t)
print(k)
s = tuple(k)
print(s)
print(int(t[1]))

try:
	print(int(t[3]))
except:
	print("No pude calcular int de "+str(type(t[3])))