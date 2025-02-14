def validar_correo(correo):
    #patron para validar el email
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$'
    
    if re.match(patron, correo):
        return True
    else:
        return False

#Crear Función Para validar Correo

nombre = input("Por favor, ingresa tu nombre: ")
correo = input("Por favor, ingresa tu correo electrónico: ")

if validar_correo(correo):
    print("Hola {}, tu correo electrónico {} es válido.".format(nombre, correo))
else:
    print("Lo siento {}, el correo electrónico {} no es válido.".format(nombre, correo))

