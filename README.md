# TITANIC
Este proyecto analiza la información disponible de los pasajeros del Titanic para identificar características asociadas con la supervivencia.
Análisis de pasajeros del Titanic
Descripción del proyecto
Este proyecto consiste en realizar un análisis exploratorio de los datos de los pasajeros del Titanic utilizando Python. El propósito es identificar algunas características relacionadas con la supervivencia, mediante la limpieza de datos, la creación de nuevas variables y la visualización de resultados.
Integrantes:
•	Palacios Conejo David Alejandro
•	María Fernanda Rosales Sánchez
Asignatura: Manejo Masivo de Datos
 Dataset
•	Nombre: Titanic - Machine Learning from Disaster
•	Archivo utilizado: train.csv
•	Fuente: Titanic - Machine Learning from Disaster | Kaggle
El dataset contiene información de 891 pasajeros, incluyendo edad, sexo, clase, tarifa, familiares a bordo y supervivencia.
Objetivo
Analizar la información de los pasajeros del Titanic para identificar características asociadas con la supervivencia, aplicando técnicas básicas de análisis exploratorio, limpieza y visualización de datos.
Este proyecto no incluye modelos de Machine Learning.
Tecnologías utilizadas
•	Python
•	Pandas
•	Matplotlib
•	Seaborn
•	Git y GitHub
Estructura del proyecto
TITANIC/
│
├── data/
│   └── train.csv
│
├── outputs/
│
├── src/
│   └── Analysis.py
│
├── .gitignore
├── README.md
└── requirements.txt
Requisitos
Para ejecutar este proyecto se necesita:
•	Python 3 instalado.
•	Git instalado.
•	Las dependencias incluidas en requirements.txt.
Instalación
1. Clonar el repositorio
git clone https://github.com/ElTalGunshy/TITANIC.git
2. Entrar a la carpeta del proyecto
cd TITANIC
3. Crear un entorno virtual
python -m venv .venv
4. Activar el entorno virtual
En Windows:
.venv\Scripts\Activate.ps1
5. Instalar las dependencias
pip install -r requirements.txt
Ejecución del proyecto
Una vez instalado el entorno y las dependencias, ejecutar el siguiente comando desde la carpeta principal:
python src/Analysis.py
El programa carga el dataset, realiza la limpieza y el análisis de los datos, muestra los resultados en la terminal y genera las gráficas de supervivencia.
Análisis realizados
1. Exploración inicial
Se revisó la información general del dataset, incluyendo:
•	Número de pasajeros y columnas.
•	Nombres y tipos de variables.
•	Valores faltantes.
•	Registros duplicados.
•	Estadísticas descriptivas.
2. Limpieza y preprocesamiento
Se realizaron las siguientes transformaciones:
•	Los valores faltantes de Age se reemplazaron por la mediana.
•	Los valores faltantes de Embarked se reemplazaron por la moda.
•	Se creó la variable HasCabin para identificar si el pasajero tenía información de cabina.
•	Se creó FamilySize para calcular el tamaño de la familia a bordo.
•	Se creó Alone para identificar a los pasajeros que viajaban solos.
•	Se creó AgeGroup para clasificar a los pasajeros por grupos de edad.
3. Análisis de supervivencia
Se analizaron los siguientes aspectos:
•	Porcentaje general de supervivencia.
•	Supervivencia según el sexo.
•	Supervivencia según la clase del pasajero.
•	Supervivencia según si viajaba solo o acompañado.
También se generaron visualizaciones para comparar la supervivencia por sexo, clase y grupo de edad.
Resultados y conclusiones
A partir del análisis realizado se obtuvieron los siguientes resultados:
•	El porcentaje general de supervivencia fue de aproximadamente 38.38%.
•	La supervivencia fue mayor entre las mujeres, con aproximadamente 74.20%, mientras que entre los hombres fue de 18.89%.
•	La primera clase presentó una supervivencia aproximada de 62.96%, superior a la de las otras clases.
•	Se identificaron diferencias en la supervivencia según el grupo de edad y las características familiares de los pasajeros.
En conclusión, los resultados muestran que el sexo y la clase del pasajero estuvieron relacionados con diferencias importantes en la supervivencia. El análisis permitió explorar estas características y representarlas mediante gráficas, sin necesidad de utilizar modelos de Machine Learning.
Reproducibilidad
Este proyecto utiliza Git y GitHub para almacenar y compartir el código, además de requirements.txt para facilitar la instalación de las dependencias.
Cualquier persona puede clonar el repositorio, crear un entorno virtual e instalar las bibliotecas necesarias para ejecutar el análisis siguiendo las instrucciones de este README.
Repositorio de GitHub: https://github.com/ElTalGunshy/TITANIC
