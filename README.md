🏦 PROYECTO 4: EDA BANK MARKETING DATASET
Este proyecto consiste en la realización de un Análisis Exploratorio de Datos (EDA) sobre un conjunto de datos de campañas de marketing bancario y un dataset complementario con información demográfica de los clientes.

🗂️ Estructura del proyecto
├── bank.py # Limpieza y análisis del dataset bancario
├── customer.py # Análisis del dataset demográfico
├── cruce_archivos.py # Integración de ambos datasets
├── README.md # Documentación del proyecto
├── bank_limpio.csv
├── bank_customer_merge.xlsx

🧩 Instalación y requisitos
Visual Studio Code
Python 3.x
Instalación de librerías:
pip install pandas
pip install matplotlib
pip install openpyxl
pip install seaborn


📊 Qué he trabajado en este proyecto

Dataset Bank Marketing
•	Carga y exploración inicial de datos.
•	Revisión de estructura y tipos de datos.
•	Identificación de valores nulos.
•	Limpieza y transformación de variables.
•	Análisis estadístico descriptivo.
•	Estudio de la variable objetivo (contratación del depósito).
•	Segmentación por edad y profesión.
•	Creación de visualizaciones.
•	Exportación del dataset limpio.

Dataset Customer Details
•	Carga de las 3 hojas del archivo Excel.
•	Unificación de los datos en un único DataFrame.
•	Comprobación de valores nulos y duplicados.
•	Eliminación de columnas innecesarias.
•	Análisis descriptivo de ingresos, composición familiar y actividad web.
•	Creación de histogramas, gráficos de barras y boxplots.
•	Análisis de correlación entre variables.

Integración de datasets
•	Cruce de ambos datasets mediante el identificador único del cliente.
•	Análisis de la relación entre características demográficas y contratación del depósito.
•	Comparación de ingresos medios, actividad web y composición familiar según la contratación.


🤝 Resultados y conclusiones

Dataset bancario
•	El dataset presenta un fuerte desbalanceo:
o	88,7 % → No contrataron.
o	11,3 % → Sí contrataron.
•	Los clientes mayores de 60 años muestran las mayores tasas de contratación.
•	Los estudiantes y jubilados presentan mejores resultados que otros perfiles profesionales.
•	Fue necesario realizar tareas de limpieza y corrección de datos antes del análisis.

Dataset demográfico
•	Se analizaron 43.170 clientes.
•	Los ingresos oscilan entre 5.841 € y 180.802 €.
•	La distribución de ingresos es prácticamente uniforme.
•	La composición familiar está equilibrada entre hogares con 0, 1 y 2 hijos.
•	No se encontraron correlaciones significativas entre ingresos, hijos, adolescentes y visitas web.

Análisis conjunto
Tras integrar ambos conjuntos de datos se observó que:
•	El nivel de ingresos no influye de forma significativa en la contratación del depósito.
•	El número de hijos y adolescentes tampoco muestra relación con la contratación.
•	La frecuencia de visitas al sitio web es prácticamente igual entre clientes que contrataron y los que no contrataron.
•	Las variables demográficas analizadas no parecen ser determinantes para explicar la contratación del producto financiero.


🚀 Resultado final
Se obtuvo un conjunto de datos limpio, integrado y preparado para:
•	Análisis avanzado.
•	Visualización de datos.
•	Modelos predictivos.
•	Machine Learning.


✒️ Autor
David Merín
damefer-code
