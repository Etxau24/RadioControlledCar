#!/usr/bin/env python3
#
# main.c
#
# Main program file, first one to be executed.
# RPi acts as server for receiving commands.
#
# Created: May 2020
#

# LIBRERIAS
import socket

from camera     import *
from motor      import *
from servo      import *
from wireles    import *

# VARIABLES GLOBALES


# CREAR SOCKET DE CONEXION PARA RECIBIR COMANDOS DE APP
printStatus("Creando socket de conexion")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 50000
s.bind(('', PORT))
s.listen(5)
men = b""

# BUCLE PRINCIPAL: RECOGER COMANDOS CONSTANTEMENTE
printStatus("Iniciando bucle principal")
while True:
	s2, _ = s.accept()

	while True:
        # SE GUARDA EN MEN EL COMANDO RECIBIDO
		men = s2.recv(1024)
        x = "Comando recibido (", men, ")" 
        printStatus(x)

        # QUE HACEMOS EN BASE AL COMANDO
		if   men == "TRNON":
        elif men == "TRNOF":
            break
        elif men == "ACLRR":
            acelerar()
        elif men == "FRENR":
            frenar()
        elif men == "GIRIZ":
            girarIzda()
        elif men == "GIRDE":
            girarDcha()
        elif men == "CAMIZ":
            girarCamIzda()
        elif men == "CAMDE":
            girarCamDcha()
        
        GPIO.cleanup()
	s2.close()

printStatus("Cerrando socket")
s.close()
print("Programa finalizado.")
exit(0)

# FUNCIONES INTERNAS
def printStatus(men):
    print("STATUS: ", men, "...")
