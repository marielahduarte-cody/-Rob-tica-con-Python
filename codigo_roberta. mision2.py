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
    
    # Gira 90° a la izquierda a velocidad 30
    hal.rotateDirectionRegulated('B', 'C', False, 'LEFT', 30, 90)
    
    # Avanza en línea recta hasta detectar el color AMARILLO en el Puerto 3
    hal.drive('B', 'C', False, 30)
    while True:
        if hal.getColorSensorSample('3') == 'YELLOW':
            break
        hal.waitFor(15)
        
    # Reproduce nota musical h'' (B5 / Si5)
    hal.playNote('987.767', '4')  # Negra (h'')
    
    # Avanza 7 cm adicionales
    hal.driveDistance('B', 'C', False, 30, 7)
    
    cerrar_pinza()
    
    # Detiene los motores
    hal.stopDrive('B', 'C')
    
    # Gira 90° a la izquierda a velocidad 30
    hal.rotateDirectionRegulated('B', 'C', False, 'LEFT', 30, 90)
    
    # Avanza en línea recta hasta detectar el color AZUL en el Puerto 3
    hal.drive('B', 'C', False, 30)
    while True:
        if hal.getColorSensorSample('3') == 'BLUE':
            break
        hal.waitFor(15)
        
    # Reproduce nota musical h'' (B5 / Si5)
    hal.playNote('987.767', '4')  # Negra (h'')
    
    # Avanza 5 cm adicionales
    hal.driveDistance('B', 'C', False, 30, 5)
    
    abrir_pinza()

def main():
    try:
        run()
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()