import matplotlib.pyplot as plt


def crear_grafica(x, y, y_recta, m, b):
    """
    Genera la gráfica de dispersión de los datos
    y muestra la recta obtenida mediante mínimos cuadrados.
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    # Dibujar las muestras originales
    ax.scatter(
        x,
        y,
        label="Datos originales",
        s=60
    )

    # Dibujar la recta de regresión
    ax.plot(
        x,
        y_recta,
        label="Recta de ajuste",
        linewidth=2
    )

    # Mostrar la ecuación dentro de la gráfica
    ecuacion = f"y = {m:.4f}x + {b:.4f}"

    ax.text(
        0.05,
        0.95,
        ecuacion,
        transform=ax.transAxes,
        fontsize=12,
        verticalalignment="top"
    )

    ax.set_title(
        "Regresión Lineal por Mínimos Cuadrados"
    )

    ax.set_xlabel("Variable X")
    ax.set_ylabel("Variable Y")

    ax.legend()
    ax.grid(True)

    fig.tight_layout()

    return fig