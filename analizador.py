def calcular_cantidad(datos):
    """Calcula la cantidad de datos."""
    return len(datos)


def calcular_promedio(datos):
    """Calcula el promedio de los datos."""
    return sum(datos) / len(datos)


def calcular_minimo(datos):
    """Obtiene el valor mínimo de los datos."""
    return min(datos)


def calcular_maximo(datos):
    """Obtiene el valor máximo de los datos."""
    return max(datos)


def main():
    """Ejecuta el análisis de los datos."""
    datos = [10, 20, 30, 40, 50]

    print("Cantidad de datos:", calcular_cantidad(datos))
    print("Promedio:", calcular_promedio(datos))
    print("Valor mínimo:", calcular_minimo(datos))
    print("Valor máximo:", calcular_maximo(datos))


if __name__ == "__main__":
    main()