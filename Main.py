#Para pruebas 

from beneficio import Beneficio

#Nombre, Apellido, Cedeula, Edad, Dinero ahorrado en la cuenta
persona = Beneficio("Nelson", "Bolaños","123456789", 22, 1000000) 

print("-----------------------------------")
print(persona.detalle()) #Muestra los detalles del cliente
print("-----------------------------------")
print(persona.ingresar(100000)) #cantidad de dinero que va a meter a la cuenta
print("-----------------------------------")
print(persona.retirar(50000)) #cantidad de dinero que va a retirar
print("-----------------------------------")
print(persona.retirar(-10)) #Valida que la cantidad a retirar sea mayor de 0
print("-----------------------------------")
print(persona.retirar(5000000)) #Valida que no se pueda retirar una cantidad mayor a la que hay en la cuenta 
print("-----------------------------------")
print(persona.ingresar(-5000000)) #Valida que la cantidad a meter en la cuenta sea mayor de 0
print("-----------------------------------")
print(persona.mostrar()) #Muestra los datos que pide el programa: subtotal, interes generado y total
print("-----------------------------------")
print("Presentado por: \nJuan Diego Jojoa M.\nNelson Fernando Bolaños E.")
print("-----------------------------------")
