import json
import sys

VERSION = "versión 1.2"

class SingletonLectorJSON:
    """
    Implementación del patrón singleton para la lectura de un archivo JSON.
    """
    def __new__(cls, path_archivo):
        if not hasattr(cls, '_instancia'):
            cls._instancia = super().__new__(cls)
            cls._instancia.path_archivo = path_archivo
            cls._instancia.datos_bancos = cls._instancia._cargar_datos_bancos()
        return cls._instancia

    def _cargar_datos_bancos(self):
        try:
            with open(self.path_archivo, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
            objeto_json = json.loads(contenido)
            return objeto_json.get("bancos", {})
        except FileNotFoundError:
            print(f"Error: No se pudo encontrar el archivo {self.path_archivo}.")
            sys.exit(1)
        except json.JSONDecodeError:
            print("Error: El formato del archivo JSON no es válido.")
            sys.exit(1)

    def obtener_datos_bancos(self):
        """
        Obtención de la información de los bancos.
        """
        return self.datos_bancos


class EntidadBancaria:
    def __init__(self, nombre, saldo_inicial, token):
        self.nombre = nombre
        self.saldo = saldo_inicial
        self.token = token

    def puede_realizar_pago(self, monto):
        """
        Verificación de si se puede procesar el pago.
        """
        return self.saldo >= monto

    def realizar_pago(self, monto):
        """
        Ejecución del procesamiento del pago.
        """
        if self.puede_realizar_pago(monto):
            self.saldo -= monto
            return True
        return False

    def obtener_datos_pago(self, monto):
        """
        Retorna la información del pago.
        """
        return {
            'nombre_banco': self.nombre,
            'monto': monto,
            'token': self.token
        }

    def __str__(self):
        return f"Banco {self.nombre} - Saldo: {self.saldo} - Token: {self.token}"


class Transaccion:
    def __init__(self, numero_orden, nombre_banco, monto, token):
        self.numero_orden = numero_orden
        self.nombre_banco = nombre_banco
        self.monto = monto
        self.token = token

    def __str__(self):
        return (f"Orden {self.numero_orden}: Banco {self.nombre_banco}, "
                f"Monto {self.monto}, Token {self.token}")


class RegistroPagos:
    """
    Clase para gestionar el historial de pagos.
    """
    def __init__(self):
        self.transacciones = []

    def agregar_transaccion(self, transaccion):
        self.transacciones.append(transaccion)

    def __iter__(self):
        return iter(self.transacciones)


class GestorPagos:
    def __init__(self, entidad_bancaria, sucesor=None):
        self.entidad_bancaria = entidad_bancaria
        self.sucesor = sucesor

    def manejar_pago(self, monto, numero_orden, registro_pagos):
        """
        Interacción con la entidad bancaria actual.
        """
        if self.entidad_bancaria.realizar_pago(monto):
            datos_pago = self.entidad_bancaria.obtener_datos_pago(monto)
            transaccion = Transaccion(numero_orden, datos_pago['nombre_banco'], monto, datos_pago['token'])
            registro_pagos.agregar_transaccion(transaccion)
            print(f"El pago de ${monto} fue procesado exitosamente por el banco {self.entidad_bancaria.nombre}. El saldo actual es: ${self.entidad_bancaria.saldo}")
            return True
        if self.sucesor is not None:
            return self.sucesor.manejar_pago(monto, numero_orden, registro_pagos)
        print(f"Error: No se pudo procesar su pago de ${monto} debido a saldo insuficiente.")
        return False


class CadenaEntidadesBancarias:
    def __init__(self, entidades_bancarias):
        self.cadena = None
        for entidad_bancaria in entidades_bancarias:
            self.cadena = GestorPagos(entidad_bancaria, self.cadena)

    def procesar_pago(self, monto, numero_orden, registro_pagos):
        """
        Ejecución del procesamiento del pago.
        """
        if self.cadena is not None:
            return self.cadena.manejar_pago(monto, numero_orden, registro_pagos)
        print("Error: No hay bancos disponibles para procesar el pago.")
        return False


class Aplicacion:
    def __init__(self, cadena_entidades_bancarias, registro_pagos):
        """
        Constructor de la clase Aplicación.
        """
        self.cadena_entidades_bancarias = cadena_entidades_bancarias
        self.registro_pagos = registro_pagos
        self.numero_orden = 0

    def ejecutar(self, opcion, monto=None):
        """
        Método principal de la aplicación.
        """
        try:
            if opcion == "auto":
                if monto is None:
                    print("Error: Es necesario especificar un monto para la opción 'auto'")
                    sys.exit(1)
                self.numero_orden += 1
                self.cadena_entidades_bancarias.procesar_pago(float(monto), self.numero_orden, self.registro_pagos)
            elif opcion == "lista":
                ejecutar_multiples_pagos(self)
            else:
                print("Error: Opción no válida.")
                mostrar_uso()
                sys.exit(1)
        except Exception as err:
            print(f"Error de la aplicación: {err}")
            sys.exit(1)


def ejecutar_multiples_pagos(aplicacion):
    """
    Función para ejecutar múltiples pagos y almacenarlos en el registro de pagos.
    """
    try:
        for _ in range(5):
            aplicacion.numero_orden += 1
            monto = 500.0
            aplicacion.cadena_entidades_bancarias.procesar_pago(monto, aplicacion.numero_orden, aplicacion.registro_pagos)
    except ValueError:
        print("Error: El monto ingresado no es válido.")


def mostrar_uso():
    """
    Función que muestra las instrucciones de uso de la aplicación.
    """
    print("Modo de uso: py programa.py <archivo_json> <opcion> [<monto>]")
    print("Opciones:")
    print("auto: Selecciona automáticamente un banco para procesar el pago basado en el monto especificado")
    print("lista: Ejecuta múltiples pagos y los almacena en el registro")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == '-v':
        print(f"Aplicación: {VERSION}")
        sys.exit(0)

    if len(sys.argv) == 2 and sys.argv[1] == '-h':
        mostrar_uso()
        sys.exit(0)

    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Error de la aplicación: argumentos no válidos.")
        mostrar_uso()
        sys.exit(1)

    path_archivo_json = sys.argv[1]
    opcion = sys.argv[2]
    monto_transaccion = sys.argv[3] if len(sys.argv) == 4 else None

    try:
        bancoA = EntidadBancaria("Banco Nacion", 1000.0, "token1")
        bancoB = EntidadBancaria("Santander", 2000.0, "token2")

        cadena_entidades_bancarias = CadenaEntidadesBancarias([bancoA, bancoB])

        registro_pagos = RegistroPagos()

        aplicacion = Aplicacion(cadena_entidades_bancarias, registro_pagos)
        aplicacion.ejecutar(opcion, monto_transaccion)
    except Exception as err:
        print(f"Error de la aplicación: {err}")
        sys.exit(1)
