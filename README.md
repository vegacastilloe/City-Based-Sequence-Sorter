# City-Based Sequence Sorter
![License: MIT](https://img.shields.io/badge/License-MIT-cyan.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![Last Updated](https://img.shields.io/github/last-commit/vegacastilloe/City-Based-Sequence-Sorter)
![Language](https://img.shields.io/badge/language-español-darkred)

#
---
- 🌟 --- CAN YOU SOLVE THIS - EXCEL CHALLENGE 804 ---
- 🌟 **Author**: Excel (Vijay A. Verma) BI
 
    - Create the group of cities sorted in alphabetical order.
 
 🔰 Este script procesa datos de nombres y ciudades desde un archivo Excel.
 
 🔗 Link to Excel file:
 👉 https://lnkd.in/d3kDs9wU

**My code in Python** 🐍 **for this challenge**

 🔗 https://github.com/vegacastilloe/City-Based-Sequence-Sorter/blob/main/city-based_sequence_sorter.py

---
---
# 🧮 City-Based Sequence Sorter

Este script en Python utiliza `pandas` para procesar datos de nombres y ciudades desde un archivo Excel. Su objetivo es asignar una secuencia por ciudad, reorganizar los datos y validar el resultado contra un conjunto de columnas esperadas.

## 📦 Requisitos

- Python 3.7+
- pandas
- Archivo Excel con la siguiente estructura:
  - Columna 1: `Names`
  - Columna 2: `City`
  - Columnas 4 en adelante: datos esperados para comparación

## 🚀 Cómo funciona

1. **Carga de datos**  
   Se lee el archivo Excel ignorando la primera fila (`header=1`) y se extraen las dos primeras columnas (`Names`, `City`).

2. **Ordenamiento inicial**  
   Se ordena el DataFrame por ciudad y nombre para establecer un orden lógico.

3. **Asignación de secuencia (`seq`)**  
   Se agrupa por ciudad y se asigna una secuencia que se reinicia en cada grupo usando `groupby().cumcount() + 1`.

4. **Reordenamiento final**  
   Se ordena por secuencia y ciudad para mostrar los primeros de cada ciudad juntos, luego los segundos, etc.  
   La columna `seq` se elimina para dejar el DataFrame listo para presentación.

5. **Comparación con columnas esperadas**  
   Se extraen las columnas esperadas desde la cuarta en adelante, se renombra eliminando `.1` si existe, y se comparan celda por celda con el resultado procesado.

6. **Resultado final**  
   Se concatena todo en un solo DataFrame que incluye:
   - Datos procesados (`Names`, `City`)
   - Columnas esperadas
   - Columna `Comparison` que indica si cada fila coincide (`True` o `False`)

## 📤 Salida

El script imprime un DataFrame con:

- `Names` y `City` ordenados por secuencia
- Columnas esperadas desde el Excel
- Columna `Comparison` con valores `True` o `False`

---

## 🛠️ Personalización
Puedes adaptar el script para:

- Leer otros rangos de columnas
- Exportar el resultado a Excel o CSV
- Aplicar otras reglas de agrupamiento o validación

## 🚀 Ejecución
```bash
pip install pandas openpyxl
```
```python
city-based_sequence_sorter.py
```

## 📄 Licencia

Este proyecto está bajo ![License: MIT](https://img.shields.io/badge/License-MIT-cyan.svg). Puedes usarlo, modificarlo y distribuirlo libremente.

---

