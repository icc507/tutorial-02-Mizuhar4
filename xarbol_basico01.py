#Árbol binario con listas

def arbolBinario(numero):
	return [numero, [], []]

def insertaEnArbolBinario(arbol,numero):
	if arbol==[]:
		arbol+=arbolBinario(numero)
	elif numero <= arbol[0]:
		insertaEnArbolBinario(arbol[1],numero)
	else:
		insertaEnArbolBinario(arbol[2],numero)

def estaEnArbolBinario(arbol,numero):
	if arbol==[]:
		return False
	elif numero==arbol[0]:
		return True	
	elif numero<arbol[0]:
		return estaEnArbolBinario(arbol[1],numero)
	else:
		return estaEnArbolBinario(arbol[2],numero)

w = arbolBinario(50)
insertaEnArbolBinario(w,100)
insertaEnArbolBinario(w,80)
insertaEnArbolBinario(w,22)
insertaEnArbolBinario(w,44)
insertaEnArbolBinario(w,104)
insertaEnArbolBinario(w,12)

print("El árbol")
print(w)

print("Caso "+str(101)+": "+str(estaEnArbolBinario(w,101)))
print("Caso "+str(104)+": "+str(estaEnArbolBinario(w,104)))
print("Caso "+str(22)+": "+str(estaEnArbolBinario(w,22)))
print("Caso "+str(11)+": "+str(estaEnArbolBinario(w,11)))
print("Caso "+str(200)+": "+str(estaEnArbolBinario(w,200)))