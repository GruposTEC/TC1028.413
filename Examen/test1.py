#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 09:45:50 2020

@author: Cronoxz05
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 09:19:39 2020

@author: Cronoxz05
"""

def main():
    """
    

    recibe Velocidad y lo convierte a entero
    -------
    lo manda a la funcion y al regresar imprime la multa

    """
    velocidad=input()
    velocidad=int(velocidad)
    multa=calculo_multa(velocidad)
    print(multa)
    
def calculo_multa(a):
    """
    

    Parameters
    ----------
    a : TLa velocidad 

    Regresa el numero 0, 1, 2 dependiendo su velocidad 
    -------
    int
        primero declaramos las fuinciones x y y, despues lo mandamos a ver si el cumpleaños es verdadero 
        si lo es se le agregan a los valores de x y y 5 para que asi este al mismo nivel del cumpleaños
        despues de esto solo se calcula cual seria la mumlta
        

    """

    x=60
    y=80
    if a== True:
        if a<= x+5:
            return 0
            
        elif a>x+5 and a<=y+5:
            return 1
        else:
            return 2
            
    else:
         if a<=x:
             return 0
         elif a>x and a<y:
             return 1
         else:
             return 2
             
             
            
    
main()

#primero pones la velocidad, despues pones el condicional if para saber si es su cumpleaños
#despues si es su cumpleaños entonces hacer las deciciones con un rango de 5 km/h mayor
#sino hacer las deciciones con los valores originales
    