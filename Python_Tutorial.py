age = 20
price = 19.20
print (age)
#Aqui se estan estableciendo una variables, y ala vez imprimiendo la vairiable
name = input("Cual es tu nombre?")
print ("Hola " +name)
#Aqui estamos creando una variable "name" para que el usuario introduzca el dato y que se gurde en la varible "name"
ano_nacimiento = input("En que año naciste?")
age = 2023 - int(ano_nacimiento)
print("Tu edad es: " + str(age))
#Aca se establecieron 2 varibales y se usaron las 2 para hacer una operacion y asi imprimirla
primero = input("Primer Numero: ")
segundo = input("Segundo Numero: ")
sum= int(primero)+ int(segundo)
print("La suma es: " + str(sum))
print("-----------------------------------------")
#Se establecieron 2 variables y como se utilizo el "input" tenemos que especificar que lo que se ingrese sea int
print(10+30)#Suma
print(10-30)#Resta
print(10*30)#Multiplicacion
print(10**30)#Elevar ala potencia
print(10//30)#Redondea el resultado
print(10%30)#Te da el residual de la división
x = (10 + 30) * 2
print(x)#Aqui se estan juntando dos tipos de operaciones
print("-----------------------------------------")
b = 3 < 4
print(b)
c = 3 > 4
print(c)
d = 3 <= 4
print(d)
e = 3 >= 4
print(e)
f = 3 == 4
print(f)
g = 3 != 4
print(g)
print("-----------------------------------------")
#Aqui se esta estableciendo si el resultado de ser cierto o no imprimirlo
temperatura = input("Cual es la temperatura: ")
if int(temperatura) > 30:
    print("Esta haciedo calor")
    print("Toma bastante agua")
elif int(temperatura) > 20:
    print("Es un buen dia")
elif int(temperatura) > 10:
    print("Hace un poco de frio")
else:
    print("Hace mucho frio, abrigate bien")
print("Listo.")
print("-----------------------------------------")
peso =int(input("Cual es tu peso: "))
unidad = (input("(K)g o (L)bs:"))
if unidad.upper() == "K":
    convertir = peso / 0.45
    print("Tu peso en Lbs: " + str(convertir))
else:
    convertir = peso * 0.45
    print("Tu peso en Kg: " + str(convertir))
    print("Gracias")
print("-----------------------------------------")
i = 1
while i <= 5:
    print(i)
    i = i + 1
i = 1
print("-----------------------------------------")
i = 1
while i <= 10:
    print(i* "*")
    i = i + 1
print("-----------------------------------------")
nombres = ["Pedro", "Jhon", "Bob", "Erick", "Maria"]
print(nombres)
nombres[0] = ("Efrain")
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[2])
print(nombres[3])
print(nombres[-1])
print(nombres[0:4])
print(nombres[0:2])
print(nombres[2:4])
print("-----------------------------------------")
numbers =[1, 2, 3, 4, 5]
numbers.insert(6, 6)
numbers.insert(0, -1)
print(numbers)
numbers.remove(4)
print(numbers)
numbers.clear()
print(numbers)
print(3 in numbers)
print(10 in numbers)
print(len(numbers))
for item in numbers:
    print(item)
print("-----------------------------------------")
num = range(5)
print(num)
mun = range(1,11)
for nu in mun:
    print(nu)
unm = range(1,11,2)
for m in unm:
    print(m)
print("-----------------------------------------")
for numero in range(5):
    if numero == 3:
        break
    print (numero)
print("-----------------------------------------")
for numero in range(5):
    if numero == 3:
        continue
    print (numero)
print("-----------------------------------------")
for numero in range(1, 5):
    if numero <= 3:
        #aqui no pasa nada y el bucle sigue trabajando
        pass
    else:
        print("El siguiente valor es mayor a 3: ")
    print (numero)
print("-----------------------------------------")
color = input("Ingrese un color: ")
#listas
lista = [29, True, 3.1416, "Hola me llamo efrain"]
lista[2] = [1,2,3]
print(lista)
lista_nueva = [1,2,3,4,3,6]
lista_nueva.append(15)#Aqui se agrega un nuevo elemento hasta el final de la lista
print(lista_nueva)
print(lista_nueva.count(3))#Aqui se cuenta las veces que este dicho elemento en la lista
print(lista_nueva.index(4))#Se indica en la posicion en la que se ecuentra el elemento en la lista
lista_nueva.remove(3)#Se remueve la primera aparicion del elemento seleccionado
print(lista_nueva)
lista.insert(0,1)#aqui se inserta un elemento al indice seleccionado
print(lista)
lista_nueva.extend([7,8,9,10])#Aqui se extiende el numero de elementos que quieres un la lista
print(lista_nueva)
print("Hola me llamo efrain" in lista)#Aqui se busca si cierto obejto esta en la lista si esta regresa un True y si no un False
lista2 = [1,2,3,4,5]
lista3 = lista+lista2 #Aqui estamos concaenando listas osea sume las listmas para hacer una sola
print(lista3)
lista3.pop()#Aqui la funsion pop al no tener ningun paramentro remueve por si sola el ultimo elemento de la lista
print(lista3)
lista3.pop(3) #aqui elimina todo elemento que se encuentre en el indice 3
lista3.clear() #Aqui elimina todo lo que este adentro de la lista
print(lista3)
lista_nueva.reverse()#Aqui voltea la lista de atras hacia adelante o de derecha a izquierda
print(lista_nueva)
lista_nueva.sort()#Aqui la funcion sort acomoda de manera ascendente los terminos enteros
print(lista_nueva)
lista_nueva.sort(reverse=True) #Aqui ordena los numero enteros pero ahora de manera descendente
print(lista_nueva)
#del statement
StatDel = [1, 6, 8, 10, 90]
del StatDel[0:3]
print(StatDel)
#Tuplas
tuple = (4,"hola",6.50,[1,2,3],5)#La tupla es semejante a la lista solo que la tupla no se puede modificar en lo absoluto
print(tuple)
lista4 = list(tuple)#Aqui estoy convirtiendo una tupla en una lista
print(lista4)
#Conjuntos
conjunto = set()#El conjunto es una base del elementos desordenados
conjunto = {1,2,3,"Hola",4.50}
conjunto.add(5)#Aqui esta ingresando el 5 al conjunto pero de manera desordenada (random)
print(conjunto)
conjunto.discard(2)#Aqui si elimina el elemento seleccionado
print(conjunto)
conjunto.clear()
print(conjunto)
#Diccionarios
diccionario = {"azul":"blue", "rojo":"red", "verde":"green"}
#El diccionario solo se usa con llaves ya que automaticamente al ponerlas python sabe que estamos hablando de un diccionario
print(diccionario["azul"]) #Aqui se imprime el significado o el valor que le dimos en el diccionario a dicha palabra
diccionario["amarillo"] = "yellow" #Aqui estamos agregando otro valo adentro del diccionario
#tambien podriamos modificar elementos ya establecidos del diccionario con el metodo de agregar de la liena 191
del(diccionario["verde"])#Aqui estariamos eleminando todo lo de la clabe seleccionada en este caso todo lo que este adentro de verde
diccionario2 = {"Alejandro":{"edad":22, "estatura": 1.78},"Maria":[21, 1.64]}#Aqui agregamos un diccionario adentro de otro diccionario en esta caso de alejandro tiene otro diccionario que tiene edad y estatura
#ITEMS()
diccionario2.items()#aqui se mostraria los items que tendria adentro de mi diccionario pero seria tuplas
list(diccionario2.items())#haciedo una lista al diccionario ya podra acceder y modificar cada item
#ENUMARATE
frutas = ["manzana", "naranja", "melon", "sandia", "platano"]
for elemento in enumerate(frutas):
    print(elemento)
#zip #Junta las listas las combina entre si
nms = ("alejandro", "Efrain", "Alan")
cmp = ("Amazon", "Apple", "Dell")
zipped = list(zip(nms,cmp))
print(zipped)
#reversed
vocales = ("a", "e", "i", "o", "u")
vocales.__reversed__()
print(f"\nLista :{vocales}")
#Sorted
canasta = ["manzana", "narnaja", "sandia", "limon", "uva"]
for a in sorted(canasta):
    print(a)
canasta1 = ["manzana", "narnaja", "sandia", "limon", "uva", "naranja", "sandia"]
for f in sorted(set(canasta1)):
    print(f)






