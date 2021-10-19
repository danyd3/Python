
fecha_Nacimiento = input("Digite su año de nacimiento: ")
diferencia = (2021 - int(fecha_Nacimiento))

if diferencia >= 18:
    print("El usuario tiene", diferencia," es mayor de edad")
else:
    print("El usuario tiene ",diferencia, "es menor de edad")
