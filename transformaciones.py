def transformar_mayusculas(df, columna):
    df[columna] = df[columna].str.upper()
    return df


def transformar_minusculas(df, columna):
    df[columna] = df[columna].str.lower()
    return df


def extraer_fecha(df, columna, campo):
    if campo == "dia":
        return df[columna].dt.day
    elif campo == "mes":
        return df[columna].dt.month
    elif campo == "anio":
        return df[columna].dt.year
