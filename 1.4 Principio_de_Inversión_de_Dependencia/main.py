#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ManejadorDatos import ManejadorDatos
from MySQL import MySQL
from MongoDB import MongoDB

# Prueba en el archivo main.py
if __name__ == "__main__":
    # Instanciar un objeto de cada clase y probar su método procesar
    manejador = ManejadorDatos()
    mysql = MySQL()
    mongodb = MongoDB()

    print("Procesando datos con MySQL:")
    manejador.procesar(mysql)

    print("\nProcesando datos con MongoDB:")
    manejador.procesar(mongodb) 