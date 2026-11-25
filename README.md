# Dashboard de rotación laboral — IBM HR Analytics

## Descripción del proyecto

Este proyecto tiene como propósito comunicar los resultados del análisis exploratorio de datos realizado en la Tarea 3, mediante un dashboard interactivo desarrollado en Python y Streamlit. La aplicación permite explorar la rotación laboral, los ingresos mensuales y la experiencia de los empleados mediante filtros, indicadores y visualizaciones estadísticas.

Para el desarrollo se utilizó el dataset IBM HR Analytics Employee Attrition, compuesto por 1.470 registros y 35 variables. Se seleccionó este conjunto de datos porque permite identificar factores asociados con la rotación laboral y comprender las características de los empleados, facilitando la toma de decisiones en la gestión del talento humano.

## Captura de pantalla del dashboard funcionando

![Dashboard funcionando](dashboard_publicado.png)

## Dashboard publicado en Streamlit Community Cloud

Acceder al dashboard interactivo (https://tarea4-rotacion-laboral.streamlit.app/)

## Hallazgos principales del EDA

- De los 1.470 empleados analizados, 237 presentan rotación laboral, lo que representa el 16,12 %.
- Los empleados con rotación presentan un ingreso mensual promedio inferior al de los empleados sin rotación.
- Existe una relación positiva entre el nivel laboral y el ingreso mensual, con una correlación de 0,9503.
- Los años de experiencia laboral presentan una relación positiva con el ingreso mensual, con una correlación de 0,773.
- El departamento de ventas presenta una rotación laboral del 20,63 %. Las asociaciones identificadas no implican causalidad.

## Instrucciones de instalación y ejecución local

1. Instalar Python en el equipo.
2. Descargar o clonar el repositorio de GitHub.
3. Abrir la carpeta del proyecto.
4. Abrir una terminal desde la carpeta donde se encuentra el archivo app.py.
5. Instalar las librerías necesarias ejecutando:

   `python -m pip install -r requirements.txt`

6. Ejecutar el dashboard mediante el siguiente comando:

   `python -m streamlit run app.py`

7. Abrir el navegador e ingresar a:

   http://localhost:8501/

## Información académica

- **Estudiante:** Oscar David Salcedo Ruiz.
- **Grupo:** 08.
- **Curso:** Programación para el análisis de datos.
- **Código del curso:** 203008069.
- **Universidad:** Universidad Nacional Abierta y a Distancia (UNAD).
- **Fecha:** Noviembre de 2026.

