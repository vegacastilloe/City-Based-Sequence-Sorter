import pandas as pd
from tabulate import tabulate

# 🧩 Datos originales
df_raw = pd.read_excel(xl, header=1)
df_raw.columns = df_raw.columns.str.strip()
df_input = df_raw.iloc[:, :2].dropna(how='all')
# 📥 Renombrar columnas opcional
#df_input.columns = ['Names',	'City']

def compare_with_expected(df_actual, df_expected_raw):
    df_expected = df_expected_raw.dropna(how='all').rename(columns=lambda x: x.replace('.1', '')).fillna('')
    comparison = df_actual.eq(df_expected.reset_index(drop=True)).all(axis=1)
    return pd.concat([df_actual, df_expected, comparison.rename('Match')], axis=1)

# Paso 1: Ordenar por ciudad y nombre
df_sorted = df_input.sort_values(['City', 'Names']).reset_index(drop=True)

# Paso 2: Asignar secuencia por ciudad
df_sorted['seq'] = df_sorted.groupby('City').cumcount() + 1

# Paso 3: Reordenar por secuencia y ciudad
df_final = df_sorted.sort_values(['seq', 'City']).reset_index(drop=True).drop(columns=['seq'])

# Paso 4: Comparación con columnas esperadas
test = df_raw.iloc[:, 3:].copy()
df_final = compare_with_expected(df_final, test)

print(tabulate(df_final.values, headers=df_final.columns, tablefmt='fancy'))

# 💾 Exportación opcional
# df_final.to_excel("river_vowel_sorter_output.xlsx", index=False)
