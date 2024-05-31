calificacion_menor_a_50=0
calificacion_menor_a_70=0
calificacion_menor_a_80=0
calificacion_mayor_a_80=0
for estudiantes in range ( 1,5):
    calificacion_estudiantes=int(input(f"Ingrese calificacion estudiante {estudiantes}: "))
    if calificacion_estudiantes < 50: 
        calificacion_menor_a_50 +=1
    elif calificacion_estudiantes >=50 and calificacion_estudiantes < 70 :
        calificacion_menor_a_70+=1
    elif calificacion_estudiantes >=70 and calificacion_estudiantes < 80 :
        calificacion_menor_a_80+=1
    elif calificacion_estudiantes >=80: 
        calificacion_mayor_a_80 +=1
    
print(f"La cantidad de estudiantes que obuvieron una calificación menor a 50 fueron:{calificacion_menor_a_50}")
print(f"La cantidad de estudiantes que obuvieron una calificación de 50 pero menor a 70 fueron:{calificacion_menor_a_70}")
print(f"La cantidad de estudiantes que obuvieron una calificación de 70 pero menor a 80 fueron:{calificacion_menor_a_80}")
print(f"La cantidad de estudiantes que obuvieron una calificación de 80 o mas  fueron:{calificacion_mayor_a_80}")


