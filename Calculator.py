def funcion1():
    print ("esto es una suma")
    try:    
        numero_uno = int(input("ingresa un numero"))
    except:
        numero_uno = 0
    try:    
        numero_dos = int(input("ingresa un numero"))
    except:
        numero_dos = 0

    resultado = numero_uno + numero_dos
    print(resultado)
funcion1()
