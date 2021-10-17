''' ▬▬▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄HOJA DE TRABAJO 2▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    INTEGRANTES: 
        1.  Alvaro Emmanuel Socop Pérez     202000194
        2.  Eduardo Enrique Zepeda Juárez   201612386
        3.  Juan Antonio Gaitan Álvarez     201700888
    REPOSITORIO EN GITHUB TAMBIEN:

'''
#        GRAMATICA:
#*      '''*
#*      A' ->  , FAC1 
#*      	| . FAC2
#*      	| EPSILON
#*      						
#*      FAC1 -> , , C A'
#*      	| D A'
#*      	
#*      FAC2 -> .D A'
#*      	| C A'
#*      
#*      C -> x
#*      D -> b
#*      F -> m
#*      '''
#!     ANALIZADOR LÉXICO SIMULADO

#? ,,,x  |  ,b
#? ..b  |   .x,,,x

listaTokens=[]     # ! , , , X . . b
listaTokens.append({'lexema':','  ,'tipo':'coma','linea':1,'columna':1})
listaTokens.append({'lexema':','  ,'tipo':'coma','linea':1,'columna':2})
listaTokens.append({'lexema':','  ,'tipo':'coma','linea':1,'columna':3})
listaTokens.append({'lexema':'x'  ,'tipo':'ekis','linea':1,'columna':4})
listaTokens.append({'lexema':'.'  ,'tipo':'punto','linea':1,'columna':5})
listaTokens.append({'lexema':'.'  ,'tipo':'punto','linea':1,'columna':6})
listaTokens.append({'lexema':'b'  ,'tipo':'be','linea':1,'columna':7})

for t in listaTokens:
    print(t['lexema'])

#ANALIZADOR SINTÁCTICO
tokenActual=0

def fac2be(indiceToken):
    if indiceToken < len(listaTokens):
        if listaTokens[indiceToken]['tipo']=='be':
            return aprima(indiceToken+1)
        else:
            print('Error sintáctico: Se esperaba una "b" y se recibió: ', listaTokens[indiceToken]['tipo']," en la Línea: ", listaTokens[indiceToken]['linea']," y Columna: ", listaTokens[indiceToken]['columna'])
            return False

def fac2(indiceToken):
    if indiceToken < len(listaTokens):
        if listaTokens[indiceToken]['tipo']=='punto':
            return fac2be(indiceToken+1)
        elif listaTokens[indiceToken]['tipo']=='ekis':
            return aprima(indiceToken+1)            
        else:
            print('Error sintáctico: Se esperaba un punto o Equis y se recibió: ', listaTokens[indiceToken]['tipo']," en la Línea: ", listaTokens[indiceToken]['linea']," y Columna: ", listaTokens[indiceToken]['columna'])
            return False

def fac1coma2(indiceToken):
    if indiceToken < len(listaTokens):
        if listaTokens[indiceToken]['tipo']=='ekis':
            return aprima(indiceToken+1)
        else:
            print('Error sintáctico: Se esperaba una "x" y se recibió: ', listaTokens[indiceToken]['tipo']," en la Línea: ", listaTokens[indiceToken]['linea']," y Columna: ", listaTokens[indiceToken]['columna'])
            return False
    
def fac1coma1(indiceToken):
    if indiceToken < len(listaTokens):
        if listaTokens[indiceToken]['tipo']=='coma':
            return fac1coma2(indiceToken+1)        
        else:
            print('Error sintáctico: Se esperaba una "x" y se recibió: ', listaTokens[indiceToken]['tipo']," en la Línea: ", listaTokens[indiceToken]['linea']," y Columna: ", listaTokens[indiceToken]['columna'])
            return False

def fac1(indiceToken):
    if indiceToken < len(listaTokens):
        if listaTokens[indiceToken]['tipo']=='coma':
            return fac1coma1(indiceToken+1)
        elif listaTokens[indiceToken]['tipo']=='be':
            return aprima(indiceToken+1)            
        else:
            print('Error sintáctico: Se esperaba una coma o "b" y se recibió: ', listaTokens[indiceToken]['tipo']," en la Línea: ", listaTokens[indiceToken]['linea']," y Columna: ", listaTokens[indiceToken]['columna'])
            return False

def aprima(indiceToken):
    if indiceToken < len(listaTokens):
        if listaTokens[indiceToken]['tipo']=='coma':
            return fac1(indiceToken+1)
        elif listaTokens[indiceToken]['tipo']=='punto':
            return fac2(indiceToken+1)
        else:
            print('Error sintáctico:  Se esperaba un punto, coma o epsilon y se recibió: ', listaTokens[indiceToken]['tipo']," en la Línea: ", listaTokens[indiceToken]['linea']," y Columna: ", listaTokens[indiceToken]['columna'])
            return False
    else:
        return True

def inicio(indiceToken):
    analisis = aprima(indiceToken)
    if analisis:
        print('analisis bien hecho (ACEPTADO): ', analisis)
    else:
        print('El analisis fracasó: ', analisis)

print('▬▬▬▬▬▬▬▬▬▬  Analizador sintactico  ▬▬▬▬▬▬▬▬▬▬▬▬')
inicio(tokenActual)