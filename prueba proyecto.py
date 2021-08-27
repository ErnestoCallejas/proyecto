insect_1=("bacteria")
insect_2=("virus")
insect_3=("larba")

pregunta1=str(input("¿las hojas tienen hoyos?  "))

if pregunta1=="si":
    pregunta2=str(input("¿la planta está caida?  "))
    if pregunta2=="si":
        pregunta3=str(input("¿sus hojas tienen manchas?  "))
        if pregunta3=="si":
            pregunta4=float(input("En una escala del 1 al 5, donde 5 son todas las hojas y 0 ninguna ¿Cuantas hojas tienen manchas? "))
            porcentaje=((pregunta4*100)/5)
            
            print("tu planta tiene: ",insect_2,",con un porcentaje estimado de infeccion del ",porcentaje,"%")
