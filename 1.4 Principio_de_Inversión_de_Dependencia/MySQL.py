#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from BaseDatos import BaseDatos

class MySQL(BaseDatos):
    def guardar(self, datos):
        print("Guardando datos en MySQL:", datos)
    
    def leer(self):
        return "Datos leídos de MySQL"