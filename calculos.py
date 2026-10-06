import numpy as np


def calcular_pendiente(x, y):
    """
    Calcula la pendiente m utilizando
    el método de mínimos cuadrados.
    """
    promedio_x = np.mean(x)
    promedio_y = np.mean(y)

    numerador = np.sum(
        (x - promedio_x) * (y - promedio_y)
    )

    denominador = np.sum(
        (x - promedio_x) ** 2
    )

    if denominador == 0:
        raise ValueError(
            "No se puede calcular la regresión porque "
            "todos los valores de x son iguales."
        )

    m = numerador / denominador

    return m


def calcular_interseccion(x, y, m):
    """
    Calcula el intercepto b de la recta.
    """
    promedio_x = np.mean(x)
    promedio_y = np.mean(y)

    b = promedio_y - (m * promedio_x)

    return b


def calcular_recta(x, m, b):
    """
    Calcula los valores estimados de y
    utilizando la ecuación y = mx + b.
    """
    y_recta = (m * x) + b

    return y_recta


def calcular_error_cuadratico(y, y_recta):
    """
    Calcula el error cuadrático total entre
    los valores reales y los valores estimados.
    """
    error = np.sum((y - y_recta) ** 2)

    return error


def calcular_r_cuadrado(y, y_recta):
    """
    Calcula el coeficiente de determinación R².
    """
    promedio_y = np.mean(y)

    suma_total = np.sum(
        (y - promedio_y) ** 2
    )

    suma_residuos = np.sum(
        (y - y_recta) ** 2
    )

    if suma_total == 0:
        return 1.0

    r_cuadrado = 1 - (suma_residuos / suma_total)

    return r_cuadrado