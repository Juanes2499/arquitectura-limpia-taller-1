#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from BaseDatos import BaseDatos

class MongoDB(BaseDatos):
    def guardar(self, datos):
        print("Guardando datos en MongoDB:", datos)
    
    def leer(self):
        return "Datos leídos de MongoDB"

