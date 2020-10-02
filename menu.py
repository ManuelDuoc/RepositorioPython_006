#crear menu con 3 opciones 
import os 
def Numeros():
    mayor=0
    menor=0
    igual=0

    cantidad=int(input("ingrese cantidad de números a ingresar: "))

    for i in cantidad:
        n=int(input(str(i)+".- Ingresa un número "))

        if (n>0):
            mayor+=1
        elif (n<0):
            menor+=1
        else:
            igual+=1
    print("cantidad de números positivos: "+str(mayor))
    print("cantidad de números negativos: "+str(menor))
    print("cantidad de 0: "+str(igual))
    tecla = input("Digite cualquier tecla para continuar: ")

def Personas():
    sumita=0
    contadorcito=0

    n=int(input("cantidad de personas a ingresar: "))

    for i in range (n):
        nombre=input("ingrese nombre: ")
        edad=int(input("ingrese edad: "))
        contadorcito+=1    
        sumita+=edad

    print("promedio de las edades: "+str(sumita/contadorcito))

    pausa=input("Presione enter.")

seguir=True 
while (seguir):
    os.system('cls')
    print("1. Numeros ")
    print("2. Datos Personales")
    print("3. Finalizar")
    op=int(input("Digite opción 1,2,3: "))
    if (op==1):
        Numeros()       #invocamos a un metodo
    if (op==2):
        Personas()
    if (op==3):
        print("Programa Finalizado")
        tecla = input("Digite cualquier tecla para continuar: ")
        break