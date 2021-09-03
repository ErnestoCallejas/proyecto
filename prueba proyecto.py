insect_1=("bacteria")
insect_2=("virus")
puntos_iniciales=0

def cant_puntos1(respuesta_usuario,respuesta_esperada,puntos_iniciales):
    if pregunta1=="si":
        puntos_a=puntos_iniciales+1
    else:
        puntos_a=puntos_iniciales+0
    return puntos_a

def cant_puntos2(respuesta_usuario,respuesta_esperada,cant_puntos1):
    if pregunta2=="si":
        puntos_b=cant_puntos1(pregunta1,"si",puntos_iniciales)+1
    else:
        puntos_b=cant_puntos1(pregunta1,"si",puntos_iniciales)+0
    return puntos_b

def cant_puntos3(respuesta_usuario,respuesta_esperada,cant_puntos2):
    if pregunta3=="si":
        puntos_c=cant_puntos2(pregunta2,"si",cant_puntos1(pregunta1,"si",puntos_iniciales))+1
    else:
        puntos_c=cant_puntos2(pregunta2,"si",cant_puntos1(pregunta1,"si",puntos_iniciales))+0
    return puntos_c

pregunta1=str(input("¿las hojas tienen hoyos?  "))

if pregunta1=="si":
    pregunta2=str(input("¿la planta está caida?  "))
elif pregunta1=="no":
    pregunta2=str(input("¿la planta está caída?  "))

if pregunta2=="si":
    pregunta3=str(input("¿sus hojas tienen manchas?  "))
elif pregunta2=="no":
    pregunta3=str(input("¿sus hojas tienen manchas?  "))
        
if pregunta3=="si":
    pregunta4=str(input("¿la planta tiene bolas en la raíz?  "))
elif pregunta3=="no":
    print(suma_puntos=cant_puntos1(pregunta1,"si",puntos_iniciales)+cant_puntos2(pregunta2,"si",cant_puntos1(pregunta1,"si",puntos_iniciales))+cant_puntos3(pregunta3,"si",cant_puntos2(pregunta2,"si",cant_puntos1(pregunta1,"si",puntos_iniciales))))

if pregunta4=="si":
    pregunta4=float(input("En una escala del 1 al 5, donde 5 son todas las hojas y 0 ninguna ¿Cuantas hojas tienen manchas? "))
    porcentaje=((pregunta4*100)/5)
    suma_puntos=cant_puntos1+cant_puntos+cant_puntos3
    if suma_puntos==2:
        print("tu planta tiene: ",insect_1,",con un porcentaje estimado de infeccion del ",porcentaje,"%")
    else:
        print("tu planta tiene: ",insect_2,",con un porcentaje estimado de infeccion del ",porcentaje,"%")
   
