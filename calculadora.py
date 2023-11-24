def suma(num1, num2):
    # Realiza la operación de suma
    return num1 + num2

def resta(num1, num2):
    # Realiza la operación de resta
    return num1 - num2

def multiplicacion(num1, num2):
    # Realiza la operación de multiplicación
    return num1 * num2

def division(num1, num2)
    # Verifica que el divisor no sea cero
    if num2 != 0:
        # Realiza la operación de división
        return num1 / num2
    else:
        # Lanza una excepción en caso de división entre cero
        raise ValueError("No se puede dividir entre cero.")

def calcular(operacion, num1, num2):
    # Verifica el tipo de operación y llama a la función correspondiente
    if operacion == 'suma':
        return suma(num1, num2)
    elif operacion == 'resta':
        return resta(num1, num2)
    elif operacion == 'multiplicacion':
        return multiplicacion(num1, num2)
    elif operacion == 'division':
        return division(num1, num2)
    else:
        # Lanza una excepción en caso de operación no soportada
        raise ValueError("Operación no soportada.")
