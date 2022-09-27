from email import message


def suma(num1, num2):
    return num1+num2

def resta(num1, num2):
    return num1-num2

def multi(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2

if __name__ == '__main__':
    message=f"Calculadora:  Elige la opcion 1=Suma,  2=Resta,  3=Multiplicacion, 4=Divison, 5=Para salir "
    while True:
        option=int(input(message))
        if option == 5:
            print("BYE")
            break