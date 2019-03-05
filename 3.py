#!/usr/bin/bash   pyhton 3.py
# __*__   coding:utf-8  __*__
def main():
    print("ORDENAR 3 NÚMEROS")
    lista= []

    lista.append( int(input("Introduzca el primer número:")) )
    lista.append( int(input("Introduzca el primer número:")) )
    lista.append( int(input("Introduzca el primer número:")) )

    lista.sort()

    print(lista)

if__name__== "__main__":
    main()

