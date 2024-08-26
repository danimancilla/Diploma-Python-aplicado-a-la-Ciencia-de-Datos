# str -> int
# costoTotalPaciente(rut), entregue el costo total de las atenciones del paciente.



def costoTotalPaciente(rut):
    archivo=open("atenciones.txt", "r")
    costo=0
    for linea in archivo:
        lista=linea.split(":")
        if lista[0]==rut:
            costo += int(lista[2])
    return costo
    


# int, int, int -> lista[str]
#pacientesDia(dia,mes,anno)  entrega una lista con los nombres de los pacientes que se atendieron en la fecha señalada.


def pacientesDia(dia,mes,anno):
    atenciones=open("atenciones.txt", "r")
    pacientes=open("pacientes.txt", "r")
    reporte=open("reporte1.txt", "w")
    #creamos la fecha como string
    if dia < 10:
        dia="0"+str(dia)
    else:
        dia=str(dia)
    if mes < 10:
        mes="0"+str(mes)
    else:
        mes=str(mes)
    anno=str(anno)
    fecha=dia+"-"+mes+"-"+anno
    
    #recorremos atenciones buscando la fecha
    for atencion in atenciones:
        L1= atencion.split(":")
        if L1[1] == fecha:
            pacientes=open("pacientes.txt", "r")
            for paciente in pacientes:
                L2 = paciente.split(":")
                if L2[0] == L1[0]:
                    reporte.write(L2[1]+"\n")              
    reporte.close()

    
#separarPacientes(), tal que genere dos reportes:
#uno con los datos de los pacientes menores de 30 años, y otro con los pacientes mayores de 60.


def separarPacientes(archivo):
    pacientes=open("pacientes.txt", "r")
    reporte1=open("reporteMen30.txt", "w")
    reporte2=open("reporteMay60.txt", "w")
    for paciente in pacientes:
        Lista= paciente.split(":")
        if int(Lista[2]) < 30:
            reporte1.write(paciente)
        elif int(Lista[2]) > 60:
            reporte2.write(paciente)
    reporte1.close()
    reporte2.close()
            
        
    

#gananciasPorMes(), tal que genere un reporte con el total de ganancias en cada mes.


def gananciasPorMes(archivo):
    atenciones=open(archivo, "r")
    reporte=open("ganancias.txt", "w")
    ganancias=0
    for atencion in atenciones:
        Lista= atencion.split(":")
        ganancias += int(Lista[2])
    reporte.write("Ganancias: "+ str(ganancias))
    reporte.close()
