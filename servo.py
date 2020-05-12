# 
# servo.c
# 
# File containing servo motor functions.
# Created: May 2020
#

# LIBRERIAS
import RPi.GPIO as GPIO
from time import sleep

servo = 20
GPIO.setup(servo, GPIO.OUT)

# LLAMADAS EXTERNAS
def girarCamIzda():
    print("Girar camara a izquierda")
def girarCamDcha():
    print("Girar camara a derecha")

# LLAMADAS INTERNAS
def accionarMotor(x):
    print("Accionar motor")
