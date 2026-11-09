#!/usr/bin/python

from roberta.ev3 import Hal

hal = Hal()

def abrir_pinza():
    hal.regulatedDrive('B', 'C', False, 'FOREWARD', 0)
    hal.waitFor(1000)

def cerrar_pinza():
    hal.regulatedDrive('B', 'C', False, 'FOREWARD', 0)
    hal.waitFor(1000)

def run():
    abrir_pinza()
    
    # Avanza 100 cm a velocidad 30
    hal.driveDistance('B', 'C', False, 30, 100)
    
    # Gira 90° a la derecha a velocidad 20
    hal.rotateDirectionRegulated('B', 'C', False, 'RIGHT', 20, 90)
    
    # Avanza indefinidamente hasta detectar color Amarillo en Puerto 3
    hal.drive('B', 'C', False, 30)
    while True:
        if hal.getColorSensorSample('3') == 'YELLOW':
            break
        hal.waitFor(15)
    
    # Reproduce nota musical h'' (B5 / Si5)
    hal.playNote('987.767', '4')  # Negra (h'')
    
    # Avanza 10 cm adicionales
    hal.driveDistance('B', 'C', False, 30, 10)
    
    # Detiene motores
    hal.stopDrive('B', 'C')
    
    cerrar_pinza()
    
    # Avanza 98 cm a velocidad 30
    hal.driveDistance('B', 'C', False, 30, 98)
    
    # Gira 90° a la izquierda a velocidad 20
    hal.rotateDirectionRegulated('B', 'C', False, 'LEFT', 20, 90)
    
    # Avanza indefinidamente hasta detectar color Verde en Puerto 3
    hal.drive('B', 'C', False, 30)
    while True:
        if hal.getColorSensorSample('3') == 'GREEN':
            break
        hal.waitFor(15)
    
    # Reproduce nota musical h'' (B5 / Si5)
    hal.playNote('987.767', '4')  # Negra (h'')
    
    # Detiene motores
    hal.stopDrive('B', 'C')
    
    abrir_pinza()

def main():
    try:
        run()
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()