#EJEMPLO 2
#Un ejemplo en el cual usamos el operador lógico or sería:
#Una escuela aplica dos exámenes a sus aspirantes, por lo que
# cada uno de ellos obtiene dos calificaciones denotadas como C1 y C2.
# El aspirante que obtenga calificaciones mayores que 80 en ambos exámenes
# es aceptado; en caso contrario es rechazado.

# Nombre: Nicole Estefania García Chiquito
# Aula: 3er Semestre A1
class calificaciones1():
    def calificacionesdotadas(self):
        print("Calificaciones Denotadas de C1 y C2")
        C1=float(input("Ingrese calificacion de C1: "))
        C2=float(input("Ingrese calificacion de C2: "))
        if C1>=90:
            print("Aprobado C1",C1)
        else:
            print("Rechazado C1",C1)
            if C2>=90:
                print("Aprobado C2",C2)
            else:
                print("Rechazado C2",C2)
calificación=calificaciones1()
calificación.calificacionesdotadas()    