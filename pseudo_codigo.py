def recoger_paquete():
    abrir_pinza()
    acercarse_al_paquete()
    bajar_mecanismo()
    cerrar_pinza()
    levantar_mecanismo()

def entregar_paquete():
    seguir_ruta_hasta_destino()
    bajar_mecanismo()
    abrir_pinza()
    levantar_mecanismo()

recoger_paquete()
entregar_paquete()