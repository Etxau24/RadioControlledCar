# 
# motor.c
# 
# Motor relationed function and objects.
# Created: May 2020
#

# LIBRERIAS
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

# MOTORES
motorDA = 16
motorDB = 18
motorDE = 18

motorIA = x
motorIB = x
motorIE = x

## MOTOR 1
GPIO.setup(motorDA, GPIO.OUT)
GPIO.setup(motorDB, GPIO.OUT)
GPIO.setup(motorDE, GPIO.OUT)

## MOTOR 2
GPIO.setup(motorIA, GPIO.OUT)
GPIO.setup(motorIB, GPIO.OUT)
GPIO.setup(motorIE, GPIO.OUT)

# LLAMADAS EXTERNAS
def acelerar():
    alanteMotor(1)
    alanteMotor(2)
def frenar():
    atrasMotor(1)
    atrasMotor(2)
def girarIzda():
    alanteMotor(1)
    GPIO.output(motorIE,GPIO.LOW)
def girarDcha():
    alanteMotor(2)
    GPIO.output(motorDE,GPIO.LOW)

# LLAMADAS INTERNAS
def alanteMotor(motor):
    if motor==1:
        GPIO.output(motorDA,GPIO.HIGH)
        GPIO.output(motorDB,GPIO.LOW)
        GPIO.output(motorDE,GPIO.HIGH)
    elsif motor==2:
        GPIO.output(motorIA,GPIO.HIGH)
        GPIO.output(motorIB,GPIO.LOW)
        GPIO.output(motorIE,GPIO.HIGH)

def atrasMotor(motor):
    if motor==1:
        GPIO.output(motorDA,GPIO.LOW)
        GPIO.output(motorDB,GPIO.HIGH)
        GPIO.output(motorDE,GPIO.HIGH)
    elsif motor==2:
        GPIO.output(motorIA,GPIO.LOW)
        GPIO.output(motorIB,GPIO.HIGH)
        GPIO.output(motorIE,GPIO.HIGH)

