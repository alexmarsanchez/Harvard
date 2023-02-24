#students = ["Hermione", "Harry", "Ron"] #este programa creará una lista de estudiantes

#print(students[0]) #Como comienza a contar desde el cero, mostrará al estudiante en la  posición 1
#print(students[1])
#print(students[2])
#necesitaremos un loop que no solo muestra numeros sino strings, cadenas de caracteres
#for students in students:
#    print(students)
#Otra manera de hacerlo;
#for i in range(len(students)): #La funcion LEN permite mostrar la posición o la cantidad de la cadena de caracteres en una lista de datos
    # ya sabemos que la variable i comenzará a contar desde cero, pero para mostrarle al usuario que el primero es el uno a i se le suma 1
#    print(i+1, students[i])

#dict permite asociar un valor a otro, como un diccionario, es más poderoso que una LISTA
#DICT lleva los corchetes
#lista lleva corchetes
# dict se usa para conectar o relacionar datos de una columna a otra, se causa desastre cuando son muchos datos
# las llaves o key, son los que esté más a la derecha, el dato que nos permitirá obtener el de la derecha
students = {
    "Hermione" : "Gryffindor", #me faltaba la coma, sino da error
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin"
            }

for student in students: #Guarda en STUDENT los datos de la llave de cada una de las posiciones de la lista de datos
    print(student, students[student], sep=", ") #Aqui lo que dice es muestra la llave y luego el valor de la derecha
