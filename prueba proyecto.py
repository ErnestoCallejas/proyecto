#Este es el programa con la correción del error de la entrega pasada, los condicionales siguen igual ya que estos si funcionaban.#
#Las preguntas se responden mediante si y no, para la pregunta de la escala si se usan valores numéricos#

plaga=["Virus","Bacteria"]
puntos_iniciales=0

def cant_puntos1(respuesta_usuario,respuesta_esperada,puntos_iniciales):
    if pregunta1=="si":
        puntos_a=puntos_iniciales+1
    else:
        puntos_a=puntos_iniciales+0
    return puntos_a

def cant_puntos2(respuesta_usuario,respuesta_esperada,puntos_a):
    if pregunta2=="si":
        puntos_b=cant_puntos1(pregunta1,"si",puntos_iniciales)+1
    else:
        puntos_b=cant_puntos1(pregunta1,"si",puntos_iniciales)+0
    return puntos_b

def cant_puntos3(respuesta_usuario,respuesta_esperada,puntos_b):
    if pregunta3=="si":
        puntos_c=cant_puntos2(pregunta2,"si",cant_puntos1(pregunta1,"si",puntos_iniciales))+1
    else:
        puntos_c=cant_puntos2(pregunta2,"si",cant_puntos1(pregunta1,"si",puntos_iniciales))+0
    return puntos_c

def porcentaje(pregunta5,num1,num2):
    valor=((pregunta5*100)/5)
    return valor


pregunta1=str(input("¿las hojas tienen hoyos?  "))

while pregunta1!="si" and pregunta1!="no":
    print("Respuesta no válida, intente de nuevo")
    pregunta1=str(input("¿las hojas tienen hoyos?  "))

if pregunta1=="si":
    pregunta2=str(input("¿la planta está caida?  "))
    
    while pregunta2!="si" and pregunta2!="no":
        print("Respuesta no válida, intente de nuevo")
        pregunta2=str(input("¿la planta está caida?   "))
    
elif pregunta1=="no":
    pregunta2=str(input("¿la planta está caída?  "))
    while pregunta2!="si" and pregunta2!="no":
        print("Respuesta no válida, intente de nuevo")
        pregunta2=str(input("¿la planta está caida?    "))

if pregunta2=="si":
    pregunta3=str(input("¿la planta tiene bolas en la raíz?  "))
    while pregunta3!="si" and pregunta3!="no":
        print("Respuesta no válida, intente de nuevo")
        pregunta3=str(input("¿la planta tiene bolas en la raíz? "))

elif pregunta2=="no":
    pregunta3=str(input("¿¿la planta tiene bolas en la raíz?  "))
    while pregunta3!="si" and pregunta3!="no":
        print("Respuesta no válida, intente de nuevo")
        pregunta3=str(input("¿la planta tiene bolas en la raíz? "))
        
if pregunta3=="si":
    pregunta4=str(input("¿sus hojas tienen manchas?  "))
    while pregunta4!="si" or pregunta4!="si":
        print("Respuesta no válida, intente de nuevo")
        pregunta4=str(input("¿sus hojas tienen manchas?  "))

    if pregunta4=="si":
        pregunta5=float(input("En una escala del 1 al 5, donde 5 son todas las hojas y 0 ninguna ¿Cuantas hojas tienen manchas? "))
        while pregunta5>5:
            print("Respuesta no válida, intente de nuevo")
            pregunta5=float(input("En una escala del 1 al 5, donde 5 son todas las hojas y 0 ninguna ¿Cuantas hojas tienen manchas? "))

    elif pregunta4=="no":
        pregunta5=0
    else:
       suma_puntos=cant_puntos1(pregunta1,"si",puntos_iniciales)+cant_puntos2(pregunta2,"si",cant_puntos1(pregunta1,"si",puntos_iniciales))+cant_puntos3(pregunta3,"si",cant_puntos2(pregunta2,"si",(cant_puntos1(pregunta1,"si",puntos_iniciales))))

elif pregunta3=="no":
    pregunta5=0
    suma_puntos=cant_puntos1(pregunta1,"si",puntos_iniciales)+cant_puntos2(pregunta2,"si",cant_puntos1(pregunta1,"si",puntos_iniciales))+cant_puntos3(pregunta3,"si",cant_puntos2(pregunta2,"si",(cant_puntos1(pregunta1,"si",puntos_iniciales))))
    
suma_puntos=cant_puntos1(pregunta1,"si",puntos_iniciales)+cant_puntos2(pregunta2,"si",cant_puntos1(pregunta1,"si",puntos_iniciales))+cant_puntos3(pregunta3,"si",cant_puntos2(pregunta2,"si",(cant_puntos1(pregunta1,"si",puntos_iniciales))))
if suma_puntos==2:
    print("tu planta tiene: ",plaga[0],)
else:
    print("tu planta tiene: ",plaga[1],",con un porcentaje de daño en hojas del ",porcentaje(pregunta5,100,5),"%")
   
