#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class BaseDatos:
    def guardar(self, datos):
        raise NotImplementedError("Este método debe ser implementado por las clases hijas.")

    def leer(self):
        raise NotImplementedError("Este método debe ser implementado por las clases hijas.")
