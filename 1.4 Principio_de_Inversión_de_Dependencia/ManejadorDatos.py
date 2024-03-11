#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ManejadorDatos:
    def procesar(self, base_datos):
        
        # Guardar datos
        base_datos.guardar("Datos a guardar")
        
        # Leer datos
        datos_leidos = base_datos.leer()
        print("Datos leídos:", datos_leidos)