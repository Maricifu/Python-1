print ("Programa para identificar el riesgo de una enfermedad coronaria según su IMS")
est= float(input("Ingrese su estatura en metros: "))
pes= float(input("Ingrese su peso corporal en kilogramos: "))
edad= int (input("Ingrese su edad: "))

imc= float(pes/est**2)

if edad<45:
    if imc<22.0:
        print ("El riesgo de padecer una enfermedad coronaria es bajo")
    elif imc>=22.0:
        print("El riego de padecer una enfermedad coronaria es medio")
elif edad>=45:
    if imc<22.0:
        print("El riesgo de padecer una enfermedad coronaria es medio")
    elif imc>=22.0:
        print("El riesgo de padecer una enfermedad coronaria es alto")
else:
    print ("Introduzca correctamente su edad")