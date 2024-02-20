#Autores: David Alejandro Roa, Juan Pablo González
#Pontificia Universidad Javeriana
#Facultad de Ingeniería
#Departamento de Ingeniería de Sistemas
#Análisis de Algoritmos
#Taller 2
#Bogotá, Febrero de 2024
import random


def AdivinarNumero(rango):
    inicio, fin = rango
    while inicio <= fin:
        if inicio == fin:
            return inicio
        numero_adivinado = CalcularNumeroMedio(inicio, fin)
        print(f"¿Es {numero_adivinado} tu número?")
        respuesta = PreguntarAlPensador()
        if respuesta == "igual":
            return numero_adivinado
        elif respuesta == "mayor":
            inicio = numero_adivinado + 1  # Corregido: ahora ajusta el inicio
        else:
            fin = numero_adivinado - 1  # Corregido: ahora ajusta el fin


def CalcularNumeroMedio(inicio, fin):
    return (inicio + fin) // 2


def PreguntarAlPensador():
    respuesta = input("Escribe 'menor', 'mayor', o 'igual'").lower()
    while respuesta not in ["mayor", "menor", "igual"]:
        print("Respuesta no válida. Por favor, responde con 'mayor', 'menor' o 'igual'.")
        respuesta = input("Escribe 'menor', 'mayor', o 'igual'").lower()
    return respuesta

print("Piensa en un número entre 1 y 100")
numero_adivinado = AdivinarNumero((1, 100))
print("El numero es ", numero_adivinado)
