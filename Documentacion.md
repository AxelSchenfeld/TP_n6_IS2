Documentación del Programa
Descripción
Este programa implementa un sistema de procesamiento de pagos utilizando el patrón de diseño de cadena de responsabilidad en Python. Su objetivo es facilitar transacciones financieras entre diferentes entidades bancarias, asegurando la integridad y seguridad de las operaciones.

Uso
El programa se ejecuta desde la línea de comandos utilizando el siguiente formato:
python programa.py [archivo_json] [opcion] [<monto>]

Opciones:

auto: Permite realizar un pago automáticamente, seleccionando un banco según el monto especificado.
lista: Realiza múltiples pagos y los registra en el historial de pagos.
Ejemplo:

python programa.py archivo.json auto 15000.0

Clases Principales
SingletonLectorJSON: Implementa un patrón Singleton para leer un archivo JSON que contiene información sobre los bancos.
EntidadBancaria: Representa un banco con su nombre, saldo inicial y token de seguridad.
Transaccion: Almacena los detalles de una transacción realizada, como el número de orden, nombre del banco, monto y token.
RegistroPagos: Mantiene un historial de pagos realizados.
GestorPagos: Maneja la cadena de responsabilidad para procesar los pagos a través de los bancos disponibles.
CadenaEntidadesBancarias: Construye y maneja la cadena de responsabilidad de los bancos.
Aplicacion: Es la clase principal que interactúa con el usuario y ejecuta las acciones correspondientes.
Flujo del Programa

El programa carga la información de los bancos desde un archivo JSON.
Construye la cadena de responsabilidad de los bancos basada en la información cargada.

El usuario elige entre dos opciones: realizar un pago automático o listar múltiples pagos.
En el modo automático, el programa selecciona un banco automáticamente para procesar el pago proporcionando el monto del pago.
En el modo de lista, se realizan múltiples pagos y los detalles se registran en el historial de pagos.

Versiones
Versión actual: 1.2