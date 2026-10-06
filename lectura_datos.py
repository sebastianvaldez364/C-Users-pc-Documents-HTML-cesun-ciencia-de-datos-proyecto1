import pandas as pd


def leer_datos(archivo):
    """
    Lee un archivo CSV y verifica que contenga
    las columnas necesarias para realizar la regresión.
    """
    datos = pd.read_csv(archivo)

    # Verificar que existan las columnas x e y
    if "x" not in datos.columns or "y" not in datos.columns:
        raise ValueError(
            "El archivo CSV debe contener las columnas 'x' y 'y'."
        )

    # Eliminar filas que tengan valores vacíos
    datos = datos.dropna(subset=["x", "y"])

    # Verificar que existan datos suficientes
    if len(datos) < 2:
        raise ValueError(
            "El archivo debe contener al menos dos muestras."
        )

    # Convertir las columnas a valores numéricos
    datos["x"] = pd.to_numeric(datos["x"], errors="coerce")
    datos["y"] = pd.to_numeric(datos["y"], errors="coerce")

    # Eliminar datos que no pudieron convertirse a números
    datos = datos.dropna(subset=["x", "y"])

    if len(datos) < 2:
        raise ValueError(
            "No existen suficientes datos numéricos para realizar el cálculo."
        )

    x = datos["x"].to_numpy()
    y = datos["y"].to_numpy()

    return datos, x, y