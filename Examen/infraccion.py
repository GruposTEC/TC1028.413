#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 11:58:59 2020

@author: avmejia
"""

def calculo_multa(velocidad,cumple):

    if not cumple:
        if velocidad <= 60:
            return 0
        elif velocidad > 60 and velocidad <= 80:
            return 1
        else:
            return 2
    else:
        if velocidad <= 65:
            return 0
        elif velocidad > 65 and velocidad <= 85:
            return 1
        else:
            return 2
