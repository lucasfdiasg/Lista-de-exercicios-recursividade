def inverter_string(texto):
    if len(texto) == 0:
        return ""
    else:
        return texto[-1] + inverter_string(texto[:-1])
