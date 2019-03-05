#!/usr/bin/env   python
#__*__  coding:utf-8  __*__
def main():
     print("COVERTIR GRADOS CELSIUS A GRADOS FAHERENHEIT")
     numero_1 = float(input("Escriba un número: "))
     media = numero_1 *9/5+32
     print("El paso de grados celsius a grados faherenheit es " + str(numero_1) + " es "+ str(media))
     #otra forma
     print("El paso de grados celsius a grados faherenheit " ,numero_1," es ",media)
     #otra forma
     print("El paso de grados celsius a grados faherenheit {} es {}" .format(numero_1,media))

if __name__ == "__main__":
     main()
