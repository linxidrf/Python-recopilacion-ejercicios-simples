
alumnos_sin_derecho=0

for alumnos in range (1,3):
    print (f"Ingrese calificaciones del alumno {alumnos}:")
    promedio=0
    for calificaciones in range (1,6):
        calificaciones_alumno =int(input(f"Ingrese calificaciones {calificaciones} : "))
        promedio += calificaciones

        
    promedio = sum(calificaciones_alumno)/5
  
    if promedio <6:
        
        alumnos_sin_derecho += 1
        print(f"La cantidad de alumnos que no tienen derecho al examen de nivelación es: {alumnos_sin_derecho}")

alumnos_sin_derecho=0

for alumnos in range (1,3):
    print (f"Ingrese calificaciones del alumno {alumnos}:")
    sumaCalificaciones =0
    for calificaciones in range (1,6):
        calificaciones_alumno =int(input(f"Ingrese calificaciones {calificaciones} : "))
        sumaCalificaciones += calificaciones_alumno

        
    promedio = sumaCalificaciones /5
  
    if promedio <6:
        alumnos_sin_derecho += 1
        print(f"La cantidad de alumnos que no tienen derecho al examen de nivelación es: {alumnos_sin_derecho}")