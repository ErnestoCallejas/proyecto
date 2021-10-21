"""
Proyecto en Python.
Análisis de enfermedad en plantas.
El programa realiza una serie de preguntas al usuario,
el cual puede contestar mediante si y no.
El programa acumula los puntos de cada pregunta.
Al final, el programa devuelve un posible agente
de infección, además de un porcentaje de
infección, dependiendo del caso.
"""

plaga=["Bacteria","Virus"]
puntos_iniciales=0

"""
====================Funciones acumuladoras de puntos=============================
"""   
   
def cant_puntos_1(respuesta_usuario,respuesta_esperada,puntos_iniciales):
    """Acumula los puntos registrados. Si la primera
    respuesta es afirmativa, va
    a sumar un punto a los puntos iniciales."""
    if pregunta_1=="si":
        puntos_a=puntos_iniciales+1
    else:
        puntos_a=puntos_iniciales+0
    return puntos_a

def cant_puntos_2(respuesta_usuario,respuesta_esperada,puntos_a):
    """Acumula los puntos obtenidos hasta la pregunta 2.
    Si la segunda respuesta es afirmativa, suma puntos
    a los puntos obtenidos de la función anterior."""
    if pregunta_2=="si":
        puntos_b=cant_puntos_1(pregunta_1,"si",puntos_iniciales)+1
    else:
        puntos_b=cant_puntos_1(pregunta_1,"si",puntos_iniciales)+0
    return puntos_b

def cant_puntos_3(respuesta_usuario,respuesta_esperada,puntos_b):
    """Acumula los puntos obtenidos hasta la pregunta 3.
    Si la tercera respuesta es afirmativa, se suma
    un punto a los puntos obtenidos en la función anterior."""
    if pregunta_3=="si":
        puntos_c=cant_puntos_2(pregunta_2,\
                               "si",cant_puntos_1 \
                               (pregunta_1,"si",puntos_iniciales))+1
    else:
        puntos_c=cant_puntos_2 \
                  (pregunta_2,"si",cant_puntos_1 \
                   (pregunta_1,"si",puntos_iniciales))+0
    return puntos_c

"""
====================Función de porcentaje=============================

"""
def porcentaje(pregunta_5,num_1,num_2):
    """Obtiene el porcentaje de infección
    en las hojas de las plantas."""
    valor=((pregunta_5*100)/5)
    return valor

"""
====================Parte principal del programa=============================

"""

pregunta_1=str(input("¿las hojas tienen hoyos?  "))

while pregunta_1!="si" and pregunta_1!="no":
    print("Respuesta no válida, intente de nuevo")
    pregunta_1=str(input("¿las hojas tienen hoyos?  "))

if pregunta_1=="si":
    pregunta_2=str(input("¿la planta está caida?  "))
    
    while pregunta_2!="si" and pregunta_2!="no":
        print("Respuesta no válida, intente de nuevo")
        pregunta_2=str(input("¿la planta está caida?   "))
    
elif pregunta_1=="no":
    pregunta_2=str(input("¿la planta está caída?  "))
    while pregunta_2!="si" and pregunta_2!="no":
        print("Respuesta no válida, intente de nuevo")
        pregunta2=str(input("¿la planta está caida?    "))

if pregunta_2=="si":
    pregunta_3=str(input("¿la planta tiene bolas en la raíz?  "))
    while pregunta_3!="si" and pregunta_3!="no":
        print("Respuesta no válida, intente de nuevo")
        pregunta_3=str(input("¿la planta tiene bolas en la raíz? "))

elif pregunta_2=="no":
    pregunta_3=str(input("¿¿la planta tiene bolas en la raíz?  "))
    while pregunta_3!="si" and pregunta_3!="no":
        print("Respuesta no válida, intente de nuevo")
        pregunta_3=str(input("¿la planta tiene bolas en la raíz? "))
        
if pregunta_3=="si":
    pregunta_4=str(input("¿sus hojas tienen manchas?  "))
    while pregunta_4!="si" and pregunta_4!="no":
        print("Respuesta no válida, intente de nuevo")
        pregunta_4=str(input("¿sus hojas tienen manchas?  "))

    if pregunta_4=="si":
        pregunta_5=float\
                    (input(\
                        "En una escala del 1 al 5," \
                        " donde 5 son todas las hojas y 0 ninguna"\
                        " ¿Cuantas hojas tienen manchas? "))
        while pregunta_5>5:
            print("Respuesta no válida, intente de nuevo")
            pregunta_5=float\
                        (input(\
                            "En una escala del 1 al 5,"\
                              " donde 5 son todas las hojas y 0 ninguna"\
                              " ¿Cuantas hojas tienen manchas? "))

    elif pregunta_4=="no":
        pregunta_5=0
    else:
        suma_puntos=cant_puntos_1 \
                    (pregunta_1,"si",puntos_iniciales)+cant_puntos2 \
                    (pregunta_2,"si",cant_puntos1 \
                     (pregunta_1,"si",puntos_iniciales))+cant_puntos_3 \
                     (pregunta_3,"si",cant_puntos_2 \
                      (pregunta_2,"si",(cant_puntos_1 \
                                        (pregunta_1,"si",puntos_iniciales))))

elif pregunta_3=="no":
    pregunta_5=0
    suma_puntos=cant_puntos_1 \
                 (pregunta_1,"si",puntos_iniciales)+cant_puntos_2 \
                 (pregunta_2,"si",cant_puntos_1 \
                  (pregunta_1,"si",puntos_iniciales))+cant_puntos_3 \
                  (pregunta_3,"si",cant_puntos_2 \
                   (pregunta_2,"si",(cant_puntos_1 \
                                     (pregunta_1,"si",puntos_iniciales))))
    
    
suma_puntos=cant_puntos_1 \
             (pregunta_1,"si",puntos_iniciales)+cant_puntos_2 \
             (pregunta_2,"si",cant_puntos_1 \
              (pregunta_1,"si",puntos_iniciales))+cant_puntos_3 \
              (pregunta_3,"si",cant_puntos_2 \
               (pregunta_2,"si",(cant_puntos_1 \
                                 (pregunta_1,"si",puntos_iniciales))))

if suma_puntos==2:
    print("Tu planta tiene: ",plaga[0])
else:
    print("tu planta tiene: ",plaga[1],\
          ",con un porcentaje de daño en hojas del ",\
          porcentaje(pregunta_5,100,5),"%")

   
