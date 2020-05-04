#!/usr/bin/env python3
#
# main.c
#
# Main program file, first one to be executed.
# RPi acts as server for receiving commands.
#
# Created: May 2020
#

import socket
from camera     import *
from motor      import *
from servo      import *
from wireles    import *

# CREAR SOCKET DE CONEXION PARA RECIBIR COMANDOS DE APP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 50000
s.bind(('', PORT))
s.listen(5)
men = b""

# BUCLE PRINCIPAL: RECOGER COMANDOS CONSTANTEMENTE
while True:
	s2, _ = s.accept()

	while True:
        # SE GUARDA EN MEN EL COMANDO RECIBIDO
		men = s2.recv(1024)

        # QUE HACEMOS EN BASE AL COMANDO
		if men == "TRNON":
            print('Received: ', men)
        elif men == "TRNOF":
            print('Received: ', men)
	s2.close()

s.close()
exit(0)
