
COMANDOS = ["compra", "venta", "saldo", "reset", "fin"]
MENSAJE_ERROR = "*ERROR* Entrada inválida"


def comprobar_importe(importe: str) -> bool:

    """
    Verifica si el importe proporcionado es un número válido.

    Args:
        valor (str): Cadena que representa el importe a verificar.

    Returns:
        bool: True si el valor es un número válido (positivo, negativo o con punto decimal), False en caso contrario.
    """
    if importe .isdigit().__float__:
        return True
    else:
        return False

    


def comprobar_comando(comando: str) -> bool:

    """
    Verifica si el comando está dentro de la lista de comandos válidos.

    Args:
        comando (str): Cadena que representa el comando ingresado por el usuario.

    Returns:
        bool: True si el comando está en la lista de comandos válidos, False en caso contrario.
    """
    if comando in COMANDOS:
        return True
    else:
        return False



def mostrar_mensaje_error():
    print(MENSAJE_ERROR)
    """
    Muestra el mensaje de error por entrada inválida.
    """


def procesar_compra(saldo: float, importe: float) -> float:

    """
    Procesa una operación de compra y actualiza el saldo restando el importe.

    Args:
        saldo (float): El saldo actual.
        importe (float): El importe a restar por la compra.

    Returns:
        float: El saldo actualizado después de realizar la compra.
    """
    saldo = float(saldo) - float(importe)
    return saldo

def procesar_venta(saldo: float, importe: float) -> float:
    """
    Procesa una operación de venta y actualiza el saldo sumando el importe.

    Args:
        saldo (float): El saldo actual.
        importe (float): El importe a sumar por la venta.

    Returns:
        float: El saldo actualizado después de realizar la venta.
    """
    saldo = float(saldo) + float(importe)
    return saldo

def mostrar_saldo(saldo: float, cont_ventas: int, cont_compras: int):
    """
    Muestra el saldo actual junto con el número de compras y ventas.

    Args:
        saldo (float): El saldo actual.
        cont_compras (int): Número total de compras realizadas.
        cont_ventas (int): Número total de ventas realizadas.
    """
    print(f"Saldo actual= {saldo:.2f}€ {cont_ventas} ventas y {cont_compras} compras)")    



def resetear_saldo(saldo: float, cont_ventas: int, cont_compras: int) -> tuple[float, int, int]:
    """
    Resetea el saldo y las operaciones realizadas, mostrando antes el saldo anterior.

    Args:
        saldo (float): El saldo actual.
        cont_compras (int): Número total de compras realizadas.
        cont_ventas (int): Número total de ventas realizadas.

    Returns:
        tuple[float, int, int]: El nuevo saldo (0), número de compras (0) y número de ventas (0) después del reinicio.
    """
    print("El nuevo saldo serán 0€ con 0 ventas y 0 compras")
    return 0, 0, 0


def recuperar_comando_e_importe(linea: str) -> tuple[str, str]:

    """
    Recupera el comando y, si lo hay, el importe de una línea de entrada.
    
    Args:
        linea (str): Línea de texto introducida por el usuario.

    Returns:
        tuple: El comando (str o  None) y el importe (str o None).
    
    Ejemplos:
        >>> recuperar_comando_e_importe("compra 100")
        ('compra', '100')
        
        >>> recuperar_comando_e_importe("saldo")
        ('saldo', None)

        >>> recuperar_comando_e_importe("")
        (None, None)        
    """
    linea = input("> ")

    lista_palabras = linea.split()

    if len(lista_palabras) == 1:
        return lista_palabras[0], None
    elif len(lista_palabras) == 2:
        return lista_palabras[0], lista_palabras[1]
    else:
        return None, None


def main():

    """
    Función principal que gestiona el flujo del programa. El programa permite al usuario realizar
    operaciones de compra y venta, consultar el saldo, restablecer las operaciones y finalizar.

    Funciona a través de un bucle que sigue las instrucciones del usuario hasta que el comando "fin" es ingresado.
    El saldo y las transacciones se actualizan según los comandos introducidos.

    Comandos disponibles:
        - compra [importe]: Resta el importe del saldo.
        - venta [importe]: Suma el importe al saldo.
        - saldo: Muestra el saldo actual junto con el número de compras y ventas.
        - reset: Restablece el saldo y las transacciones a cero.
        - fin: Termina el programa.
    
    Ejemplos:
        > compra 100
        > venta 50
        > venta
        *ERROR* Entrada inválida
        > venta cincuenta euros
        *ERROR* Entrada inválida
        > compra 50€
        *ERROR* Entrada inválida
        > saldo 666
        *ERROR* Entrada inválida
        > saldo
        Saldo actual = -50.00 (1 compras y 1 ventas)
        > venta 200
        > reset
        Saldo anterior = 150.00 (1 compras y 2 ventas)
        > saldo
        Saldo actual = 0.00 (0 compras y 0 ventas)
        > fin
    """
    encuentra_fin = False
    cont_compras = 0
    cont_ventas = 0
    saldo = 0

    while not encuentra_fin:

        comando, importe = recuperar_comando_e_importe(tuple)

        if comando is None or not comprobar_comando(comando):
            mostrar_mensaje_error()

        elif comando in ("saldo", "reset", "fin") and importe is not None:
            comprobar_importe()

        elif comando == "saldo":
            mostrar_saldo(saldo, cont_ventas, cont_compras)
            
        elif comando == "reset":
            saldo, cont_compras, cont_ventas = resetear_saldo()

            
        elif comando == "fin":
            encuentra_fin = True
            
        elif importe is None or comprobar_importe(importe):
            
            if comando == "compra":
                saldo = procesar_compra(saldo, importe)
                cont_compras += 1

            elif comando == "venta":
                saldo = procesar_venta(saldo, importe)
                cont_ventas += 1

if __name__ == "__main__":
    main()
