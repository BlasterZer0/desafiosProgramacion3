#Ingresar números
i = 0
number = []
while i < 9:
    try:
        val = int(input("Ingresar valor: "))
        number.append(val)
        i += 1
    except:
        print("Solo números")
#Imprimir array inicial
a = 0
b = 1
print("Arreglo")
while a < 3:
    print(number[a*3:b*3])
    a += 1
    b += 1
#Imprimir Array ordenado
print(" ")
print("Arreglo ordenado")
a = 0
b = 1
while a < 3:
    if a != 1:
        print(number[a*3:b*3])
    else:
        print(number[a*3:b*3][::-1])
    a += 1
    b += 1
