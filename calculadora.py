print('***** Calculadora en Python *****')
operando1 = operando2 = resultado =0 #Definimos las variables
salir = False
while not salir:
    print(f'''Operaciones que puedes realizar:
    1. Suma
    2. Resta 
    3. Multiplicacion
    4. Division
    5. Salir''')
    opcion = int(input('Escoje una opcion: '))
    #Solicitamos los operandos
    #if opcion >= 1 and opcion <= 4:
    if 1 <= opcion <= 4:
        operando1 = float(input('Dame el primer numero: '))
        operando2 = float(input('Dame el segundo numero: '))

        #Revisamos el tipo de operacion a realizar
    if opcion == 1: # Suma
        resultado = operando1 + operando2
        print(f' La suma de {operando1} y {operando2} es: {resultado: .2f}\n')
    elif opcion == 2: # Resta
        resultado = operando1 - operando2
        print(f' La resta de {operando1} y {operando2} es: {resultado: .2f}\n')
    elif opcion == 3: # Multiplicacion
        resultado = operando1 * operando2
        print(f' La multiplicacion de {operando1} y {operando2} es: {resultado: .2f}\n')
    elif opcion == 4: # Division
        resultado = operando1 / operando2
        print(f' La division de {operando1} y {operando2} es: {resultado: .2f}\n')
    elif opcion == 5: # Salir
        salir = True
        print('Saliendo del programa Calculadora. Hasta pronto!')
    else:
        print('Opcion invalida, selecciona otra opcion...\n')