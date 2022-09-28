
def suma(num1, num2):
    return num1+num2

def resta(num1, num2):
    return num1-num2

def multi(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2

if __name__ == '__main__':
    message=f"Calculadora:\n  Elige la opcion\n 1=Suma\n  2=Resta\n  3=Multiplicacion\n 4=Divison\n 5=Para salir\n"
    while True:
        option=int(input(message))
        #compara cada opcion y llama a la funcion correspondiente 
        num1=int(input("Ingresa un numero "))
        num2=int(input("Ingresa un segundo numero "))
        if option == 1:
            resultado_suma=suma(num1,num2)
            print("el resultado de la suma es ", resultado_suma)
        elif option== 2:
            resultado_resta=resta(num1,num2)
            print("el resultado de la resta es ", resultado_resta)
        if option==3:
            resultado_multi=multi(num1,num2)
            print("el resultado de la multiplicacion es ", resultado_multi)
        if option==4:
            resultado_div=div(num1,num2)
            print("el resultado de la division es ", resultado_div)
        elif option == 5:
            print("BYE")
            break
        else:
            print ("Opcion incorrecta")