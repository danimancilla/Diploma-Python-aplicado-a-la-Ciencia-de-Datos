"""Como profesor, acaba de concluir la revisión de los exámenes
correspondientes a su curso de programación. Sin embargo,
durante la evaluación del último examen, se percató de que los
puntajes asignados a las preguntas presentan un error en la distribución.
Esto conlleva a que la nota máxima alcanzable por un estudiante se
limite a un 6.3. Para no revisar todas las pruebas nuevamene,
ha decidido otorgar un incremento de 0.7 puntos como bonificación
a todos los estudiantes. Suponiendo que tiene las notas actuales
de los estudiantes en la lista L y, usando las funciones Map, Filter o Reduce:
• Defina una nueva lista L_corregida con las notas de los estudiantes más los 0.7 puntos faltantes.
• Defina una nueva lista L_aprobados con los estudiantes que aprobaron el curso, es decir, que
tengan nota mayor o igual a 4.0.
• Calcule el promedio del curso. Para esto, pondere cada nota por 1/len(L) y sume.
"""

from functools import reduce

L = [5.0, 4.5, 6.3, 6.0, 5.4, 3.0]

L_corregida = list(map(lambda x: round(x+0.7, 1),L))
L_aprobados = list(filter(lambda x: x >= 4.0 , L_corregida))
promedio = round(reduce(lambda x,y: x+y , list(map(lambda x: x/len(L), L_corregida)) , 0),1)


