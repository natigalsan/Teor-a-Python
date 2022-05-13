nombre = "Macarena"
edad = 15
lenguajes_fav = ['Python', 'C', 'JS']


print ("hello geeks "+ nombre + "tengo", edad, "Y mis lenguajes favoritos son:", lenguajes_fav)
print (f" hola mi nombre es {nombre} tengo {edad} y mis leng favor son {lenguajes_fav}")

persona = {
    "nombre": "Macarena",
    "edad": 26,
    "leg fav": ['Python', 'C', 'JS']
}
print(persona["leg fav"])

# # Sentencia condicional:------------------------------------------------

if (edad >17):
    print ("hola")
elif(edad==15):
    print("adios, no puedes beber así que para casita!!!") 
else: 
    print("no deberías pensar en eso")

# #Sentencias cíclicas: ---------------------------------------------------

contador = 0
while (contador <11):
    print(contador)
    contador+=1

#------------------trabajar con FOR: -------------------------------------------

poema = "las rosas son rojas"
for char in poema:
    print(char)


for uno in range (5):
    print(uno)

for cuatro in range (0, 10, 2): #comienzo en 0 quiero llegar hasta el 10 y que avance de 2 en 2:
    print(cuatro) #--> for (let i =0)

for cinco in range (18,3,-3):
    print(tres) #for (let i=18, i>3, i-=3)// si 18 es > que 3 sigue restando (-3)
#----------------------ARRAYS------------------------------------------------------------------------------
personas = ["ore", "abril", "nati"]

# array.push(elemento) / agregar elementos
personas.append("pablo")
print(personas)

#para eliminar a elementos en array
personas.pop(0) #elimino a ore y no al ultimo por eso le tengo que poner la posición 
print(personas)

personas.remove("abril") #aqui elmino por parámetros no por posición como con el .POP
print(personas)

#para imprimir de una lista de array unos cuantos solo puedo hacer lo siguietne: 
print(personas[1:3]) #me imprime abril y nati
print(personas[:-2]) #me imprime ore, es decir desde el comienzo menos la ultima persona(si pongo -1 me incluye la ultima persona xk esta es siempre n-1)
print(len("hola que tal"))#"para medir la longitud de un string"
print(len(personas)) #para medir objetos u array








