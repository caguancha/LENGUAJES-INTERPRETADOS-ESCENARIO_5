# ESCENARIO 5: Script de Consulta Segura con .get()
mppt_phocos = {
    "0x10": {
        "hardware_source": "PV_ARRAY",
        "max_safe_value": 150.0,
        "system_flag": True
    },
    "0x11": {
        "hardware_source": "BATTERY",
        "max_safe_value": 60.0,
        "system_flag": True
    },
    "0x15": {
        "hardware_source": "LOAD_RELAY",
        "max_safe_value": 20.0,
        "system_flag": False
    }
}

# Control numérico del ciclo para evitar desbordamientos o bucles infinitos
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    print(f"\n--- Sistema de Consulta MPPT (Intento {intentos + 1}/{max_intentos}) ---")
    direccion = input("Ingrese la dirección hexadecimal (ej. 0x10, 0x11, 0x15): ").strip()
    
    # Método seguro .get() para evitar excepciones de claves inexistentes
    registro = mppt_phocos.get(direccion)
    
    if registro:
        print(f"[ÉXITO] Registro encontrado en {direccion}:")
        print(f"  - Hardware Source: {registro.get('hardware_source')}")
        print(f"  - Max Safe Value: {registro.get('max_safe_value')}")
        print(f"  - System Flag: {registro.get('system_flag')}")
        break  # Rompe el ciclo si la consulta es exitosa
    else:
        print(f"[ERROR CONTROLADO] La dirección '{direccion}' no existe en la memoria.")
        
    intentos += 1
    if intentos == max_intentos:
        print("\n[ALERTA] Límite de intentos alcanzado. Cerrando canal de consulta por seguridad.")
        