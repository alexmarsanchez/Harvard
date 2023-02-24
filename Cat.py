# Este programa debe imprimir en pantalla 3 veces "Meow" en la pantalla
#print ("Meow")
#print ("Meow")
#print ("Meow")
# Así como está arriba funcionará, pero es un programa pobre en programación. Usemos el condicional WHILE
#i = 0
#while i < 3: #(no usar <= porque desde cero hasta 3 hay 4 meows) si lo dejo hasta aqui y corro el programa, perderé el control del pc, porque siempre será 3, y entrará  en loop eterno el pc.
    # deberás presionar CTRL + C para interrumpir el loop y no tener que apagar el pc
#    i += 1 # es lo mismo que i = i + 1
#    print ("Meow")
# while, for, list
# ester puede no ser la mejor manera pero tambien funciona for i in [0,1,2]: print ("Meow")
# ¿por qué no es la mejor manera? porque si es una lista de valores de 1millón, no harás hacer desde el 0 hasta el 1millon

#for i in range(3): # de esta manera sólo colocas en paréntesis la cantidad que necesitas
#    print("Meow")

#print ("Meow\n" * 3, end="") #el "\n" es para dar saltos de líneas y no se imprima meowmeowmeow ***para que el cursor no se mueva a la proxima linea se debe colocar end=""
def main():
    number = get_number() #get_number no existe pero abajo la crearemos
    meow(number)


def get_number():
    while True: #al principio siempre será verdadero el valor, es para que comience a evaluar
        n = int(input("What's n? ")) #lo que te diga el usuario será el valor de N
        if n > 0:
            break #para que rompa el loop
    return n #para que guarde el valor de n, dado por el usuario


def meow(n):
    for _ in range(n):
        print("Meow")
main()
