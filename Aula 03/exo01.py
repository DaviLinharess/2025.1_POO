x = 1 #usando while
while x <= 10:
    print (x, end = " ")
    x += 1

for x in range (1,11): #usando for 
    print (x, end = " ")
print ()

def imprimir_numero(x,limite): #usando função recursiva
    if x == limite: return
    print (x, end = " ")
    imprimir_numero(x + 1,limite)

imprimir_numero(1,11)

print()