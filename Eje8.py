c1= int(input("Ingrese nota certamen 1: "))
c2= int(input("Ingrese nota certamen 2: "))
lab= int(input("Ingrese nota laboratorio: "))
 
c3= int(((3*60) - (0.9*lab) - (0.7*c1) - (0.7*c2)) / (0.7)) 
print ("Necesita nota "+ str(c3) + " en el certamen 3.")