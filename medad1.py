#
#Fecha       :19_10_2021
#Author      :Daniel Alberto De Jesus (danyd3)
#<dany7214dj@gmail.com
#

fecha_Nacimiento = input("Digite su año de nacimiento: ")
diferencia = (2021 - int(fecha_Nacimiento))

if diferencia >= 18:
    print("El usuario tiene", diferencia," es mayor de edad")
else:
    print("El usuario tiene ",diferencia, "es menor de edad")
