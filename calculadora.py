def sumar (a, b):
    c= a+b
    return c
    
def restar(a, b):
    return a-b

def multiplicar(a, b):
    return a*b

def div_entera(a, b):
    if b==0:
        print("error division sobre cero")
        return
    return a/b

def division(a, b):
    if b==0:
        print("error division sobre cero")
        return
    return a/b

def modulo(a, b):
    if b==0:
        print("error division sobre cero")
        return
    return a%b

def potencia(a,b):
    return a**b


def main():
    print("ingresa dos valores")
    x= int(input())
    y= int(input())

    print("1. sumar\n 2.Restar\n 3.Division entera\n 4.division\n")
    print("5.Modulo\n 6.Potencia\n 7.multipiclar")
    op =int(input())

    if op ==1:
        print(sumar(x,y))
    elif op==2:
        print(restar(x,y))
    elif op==3:
        print(div_entera(x,y))
    elif op==4:
        print(division(x,y))
    elif op==5:
        print(modulo(x,y))
    elif op==6:
        print(potencia(x,y))
    elif op==7:
        print(multiplicar(x,y)) 
    else:
        print("Opcion no valida")
            
if __name__== "__main__":
    main()