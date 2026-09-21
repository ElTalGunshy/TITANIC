# TITANIC
Este proyecto analiza la información disponible de los pasajeros del Titanic para identificar características asociadas con la supervivencia.
Análisis de pasajeros del Titanic
# Análisis de pasajeros del Titanic

## 1. Descripción del proyecto

Este proyecto consiste en realizar un análisis exploratorio de los datos de los pasajeros del Titanic utilizando Python. El propósito es identificar características relacionadas con la supervivencia mediante la limpieza de datos, la creación de nuevas variables y la visualización de resultados.

**Integrantes:**

* Palacios Conejo David Alejandro
* María Fernanda Rosales Sánchez

**Asignatura:** Big Data

---

## 2. Dataset

* **Nombre:** Titanic - Machine Learning from Disaster
* **Archivo utilizado:** `train.csv`
* **Fuente:** [Kaggle - Titanic](https://www.kaggle.com/c/titanic/data)

El dataset contiene información de 891 pasajeros, incluyendo edad, sexo, clase, tarifa, familiares a bordo y supervivencia.

---

## 3. Objetivo

Analizar la información de los pasajeros del Titanic para identificar características asociadas con la supervivencia, aplicando técnicas básicas de análisis exploratorio, limpieza y visualización de datos.

Este proyecto no incluye modelos de Machine Learning.

---

## 4. Tecnologías utilizadas

* Python
* Pandas
* Matplotlib
* Seaborn
* Git
* GitHub

---

## 5. Estructura del proyecto

La organización de los archivos del proyecto es la siguiente:

```text
TITANIC/
├── data/
│   └── train.csv
├── outputs/
├── src/
│   └── Analysis.py
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 6. Requisitos

Para ejecutar este proyecto se necesita tener instalado:

* Python 3
* Git
* Las dependencias incluidas en el archivo `requirements.txt`

---

## 7. Instalación

### Paso 1. Clonar el repositorio

```bash
git clone https://github.com/ElTalGunshy/TITANIC.git
```

### Paso 2. Entrar a la carpeta del proyecto

```bash
cd TITANIC
```

### Paso 3. Crear un entorno virtual

```bash
python -m venv .venv
```

### Paso 4. Activar el entorno virtual

En Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

### Paso 5. Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

## 8. Ejecución del proyecto

Una vez instalado el entorno virtual y las dependencias, ejecutar el siguiente comando desde la carpeta principal del proyecto:

```bash
python src/Analysis.py
```

El programa carga el dataset, realiza la limpieza y el análisis de los datos, muestra los resultados en la terminal y genera gráficas de supervivencia.

---

## 9. Análisis realizados

### 9.1 Exploración inicial

Se revisó la información general del dataset, incluyendo:

* Número de pasajeros y columnas.
* Nombres de las variables.
* Tipos de datos.
* Valores faltantes.
* Registros duplicados.
* Estadísticas descriptivas.

### 9.2 Limpieza y preprocesamiento

Se realizaron las siguientes transformaciones:

* Los valores faltantes de `Age` se reemplazaron por la mediana.
* Los valores faltantes de `Embarked` se reemplazaron por la moda.
* Se creó la variable `HasCabin` para identificar si el pasajero tenía información de cabina.
* Se creó `FamilySize` para calcular el tamaño de la familia a bordo.
* Se creó `Alone` para identificar a los pasajeros que viajaban solos.
* Se creó `AgeGroup` para clasificar a los pasajeros por grupos de edad.

### 9.3 Análisis de supervivencia

Se analizaron los siguientes aspectos:

* Porcentaje general de supervivencia.
* Supervivencia según el sexo.
* Supervivencia según la clase del pasajero.
* Supervivencia según si viajaba solo o acompañado.

---

## 10. Visualizaciones

Se generaron gráficas utilizando Matplotlib y Seaborn para representar y comparar la supervivencia de los pasajeros.

Las visualizaciones realizadas fueron:

1. Supervivencia según el sexo.
2. Supervivencia según la clase del pasajero.
3. Supervivencia según el grupo de edad.

---

## 11. Resultados y conclusiones

A partir del análisis realizado se obtuvieron los siguientes resultados:

* El porcentaje general de supervivencia fue de aproximadamente 38.38%.
* La supervivencia fue mayor entre las mujeres, con aproximadamente 74.20%, mientras que entre los hombres fue de 18.89%.
* La primera clase presentó una supervivencia aproximada de 62.96%, superior a la de las otras clases.
* Se identificaron diferencias en la supervivencia según el grupo de edad y las características familiares de los pasajeros.

En conclusión, los resultados muestran que el sexo y la clase del pasajero estuvieron relacionados con diferencias importantes en la supervivencia. El análisis permitió explorar estas características y representarlas mediante gráficas, sin utilizar modelos de Machine Learning.

---

## 12. Reproducibilidad

Este proyecto utiliza Git y GitHub para almacenar y compartir el código, además de `requirements.txt` para facilitar la instalación de las dependencias.

Cualquier persona puede clonar el repositorio, crear un entorno virtual e instalar las bibliotecas necesarias para ejecutar el análisis siguiendo las instrucciones de este README.

De esta manera, el proyecto puede ejecutarse en un entorno nuevo sin necesidad de recibir archivos adicionales fuera del repositorio.

---

## 13. Repositorio

**GitHub:** https://github.com/ElTalGunshy/TITANIC