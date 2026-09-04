def calcular_cantidad(datos):
    return len(datos)


def calcular_promedio(datos):
    return sum(datos) / len(datos)


def calcular_minimo(datos):
    return min(datos)


def calcular_maximo(datos):
    return max(datos)


datos = [10, 20, 30, 40, 50]

print("Cantidad de datos:", calcular_cantidad(datos))
print("Promedio:", calcular_promedio(datos))
print("Valor mínimo:", calcular_minimo(datos))
print("Valor máximo:", calcular_maximo(datos))
