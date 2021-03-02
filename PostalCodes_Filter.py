#Alumno : GONZALEZ VITALI ARIEL
# 1° Ingenieria en Informatica
#Turno Mañana
# 2°PARCIAL-Ejercicio 1


def filtrarCABA(escribir,leer):
    for linea in leer:
        if linea.split(';')[4]=='CABA\n':
            escribir.write(';'.join(linea.split(';')[:2])+'\n')
    return

def filtrarCODIGOS(leer2):
    codigos=[]
    for i in leer2:
        codigos.append(i.split(';')[0])
    codigos=list(set(codigos))
    codigos.sort()
    return codigos

def filtrarCALLES(codigos,leer2):
    leer2.seek(0)
    dic = dict.fromkeys(codigos,())
    for linea in leer2:
        linea=linea.rstrip('\n')
        aux=linea.split(';')
        dic[aux[0]]=dic[aux[0]]+(aux[1],)
    for i in dic:
        dic[i]=set(dic[i])
        dic[i]=list(dic[i])
        dic[i].sort()
    return dic

#programa principal
try:
    leer = open(r'codpos.txt','rt')
    escribir = open(r'filtrarCABA.txt','wt')
    filtrarCABA(escribir,leer)
    leer.close()
    escribir.close()
    leer2 = open(r'filtrarCABA.txt','rt')
    codigos=filtrarCODIGOS(leer2)
    dic=filtrarCALLES(codigos,leer2)
    for i in dic:
        calles=','.join(dic[i])
        print(f'{i:5}: {calles}')
except FileNotFoundError as error:
    print(f'Error al abrir los archivos | {error}')
except OSError as error:
    print(f'Error fatal | {error}')
finally:
    try:
        leer2.close( )
    except NameError:
        pass
