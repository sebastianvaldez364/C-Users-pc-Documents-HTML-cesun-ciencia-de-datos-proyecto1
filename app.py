import streamlit as st

from lectura_datos import leer_datos

from calculos import (
    calcular_pendiente,
    calcular_interseccion,
    calcular_recta,
    calcular_error_cuadratico,
    calcular_r_cuadrado
)

from graficas import crear_grafica


# --------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# --------------------------------------------------

st.set_page_config(
    page_title="Regresión Lineal",
    page_icon="📊",
    layout="centered"
)


# --------------------------------------------------
# TÍTULO
# --------------------------------------------------

st.title("Regresión Lineal por Mínimos Cuadrados")

st.write(
    "Aplicación para calcular una recta de ajuste mediante "
    "el método de regresión lineal por mínimos cuadrados."
)


# --------------------------------------------------
# LECTURA DE DATOS
# --------------------------------------------------

try:

    # Leer automáticamente el archivo datos.csv
    datos, x, y = leer_datos("datos.csv")


    # --------------------------------------------------
    # MOSTRAR DATOS
    # --------------------------------------------------

    st.subheader("Datos de entrada")

    st.dataframe(
        datos,
        use_container_width=True
    )

    st.write(
        "Número de muestras:",
        len(datos)
    )


    # --------------------------------------------------
    # CÁLCULOS
    # --------------------------------------------------

    m = calcular_pendiente(x, y)

    b = calcular_interseccion(
        x,
        y,
        m
    )

    y_recta = calcular_recta(
        x,
        m,
        b
    )

    error = calcular_error_cuadratico(
        y,
        y_recta
    )

    r_cuadrado = calcular_r_cuadrado(
        y,
        y_recta
    )


    # --------------------------------------------------
    # RESULTADOS
    # --------------------------------------------------

    st.subheader("Resultados")

    columna1, columna2 = st.columns(2)

    with columna1:
        st.metric(
            "Pendiente (m)",
            f"{m:.4f}"
        )

    with columna2:
        st.metric(
            "Intercepto (b)",
            f"{b:.4f}"
        )


    # --------------------------------------------------
    # ECUACIÓN
    # --------------------------------------------------

    st.write("### Ecuación de la recta")

    if b >= 0:
        st.latex(
            f"y = {m:.4f}x + {b:.4f}"
        )

    else:
        st.latex(
            f"y = {m:.4f}x - {abs(b):.4f}"
        )


    # --------------------------------------------------
    # INFORMACIÓN DEL AJUSTE
    # --------------------------------------------------

    st.write("### Información del ajuste")

    st.write(
        f"Error cuadrático total: **{error:.4f}**"
    )

    st.write(
        f"Coeficiente de determinación R²: "
        f"**{r_cuadrado:.4f}**"
    )


    # --------------------------------------------------
    # GRÁFICA
    # --------------------------------------------------

    st.subheader("Gráfica")

    figura = crear_grafica(
        x,
        y,
        y_recta,
        m,
        b
    )

    st.pyplot(figura)


    # --------------------------------------------------
    # INTERPRETACIÓN
    # --------------------------------------------------

    st.subheader("Interpretación")

    st.write(
        f"La pendiente obtenida es {m:.4f}. "
        "Este valor representa el cambio aproximado "
        "de Y por cada unidad que aumenta X."
    )

    st.write(
        f"El intercepto es {b:.4f}, que representa "
        "el valor estimado de Y cuando X es igual a 0."
    )

    st.write(
        f"El valor de R² obtenido es {r_cuadrado:.4f}. "
        "Este indicador permite observar qué tan bien "
        "se ajusta la recta a los datos proporcionados."
    )


# --------------------------------------------------
# MANEJO DE ERRORES
# --------------------------------------------------

except Exception as error:

    st.error(
        f"Error al procesar datos.csv: {error}"
    )