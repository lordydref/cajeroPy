import datetime
import os
class Cajero:
    def menu(self):
        self.cuentas = {}
        self.movimientos = {}
        while True:
            print('''
            1. Crear una nueva cuenta
            2. Realizar transacción
            3. Retiro de efectivo
            4. Consultar saldo
            5. Consultar estado de cuenta
            6. Guardar datos y salir
            ''')
            opcion=input('Indique la operación que desea realizar: ')
            if opcion == '1':
                self.nuevacuenta()
            elif opcion == '2':
                self.depositar()
            elif opcion == '3':
                self.retirar()
            elif opcion == '4':
                self.consultarsaldo()
            elif opcion == '5':
                self.consultarestado()
            elif opcion == '6':
                self.guardardatos()
                print('Gracias por su confianza. Hasta luego.')
                break
            else:
                print('Opción no válida')
    def nuevacuenta(self):
        tipo = input('¿Qué tipo de cuenta desea crear (monetaria o ahorro)?: ').strip().lower()
        numero = input('Introduzca el número de cuenta creada: ')
        if numero in self.cuentas:
            print('Ese número de cuenta ya existe')
        else:
            self.cuentas[numero] = {'tipo': tipo, 'saldo': 0}
            self.movimientos[numero] = []
            print(f'Su cuenta de tipo {tipo} fue creada con éxito. Número de cuenta: {numero}')
    def depositar(self):
        numero = input('Coloque el número de cuenta donde depositará: ')
        if numero in self.cuentas:
            try:
                cantidad = float(input('Cantidad a depositar en Q: '))
                if cantidad > 0:
                    self.cuentas[numero]['saldo'] += cantidad
                    self.registrar(numero, 'Depósito', cantidad)
                    print(f'Su depósito de Q{cantidad:.2f} ha sido completado')
                else:
                    print('Por favor, ingresar un monto positivo')
            except ValueError:
                print('Monto inválido')
        else:
            print('La cuenta no está en existencia')
    def retirar(self):
        numero = input('Número de cuenta para realizar retiro: ')
        if numero in self.cuentas:
            try:
                cantidad = float(input('Cantidad a retirar en Q: '))
                if 0 < cantidad <= self.cuentas[numero]['saldo']:
                    self.cuentas[numero]['saldo'] -= cantidad
                    self.registrar(numero, 'Retiro', -cantidad)
                    print(f'Su retiro de Q{cantidad:.2f} ha sido completado')
                elif cantidad > self.cuentas[numero]['saldo']:
                    print('Fondos insuficientes')
                else:
                    print('Por favor, ingresar un monto positivo')
            except ValueError:
                print('Monto inválido')
        else:
            print('La cuenta no está en existencia')
    def consultarsaldo(self):
        numero = input('Ingrese el número de cuenta para ver el saldo: ')
        if numero in self.cuentas:
            saldo = self.cuentas[numero]['saldo']
            print(f'Su saldo de la cuenta {numero} es de: Q{saldo:.2f}')
        else:
            print('La cuenta no está en existencia')
    def consultarestado(self):
        numero = input('Ingrese el número de cuenta para ver historial: ')
        if numero in self.cuentas:
            print(f"\nHistorial de la cuenta {numero}:\n")
            print('Fecha y hora\t\tMovimiento\tCantidad (Q)')
            for mov in sorted(self.movimientos[numero], key=lambda x: x[0]):
                fecha, tipo, cantidad = mov
                print(f"{fecha}\t{tipo}\tQ{cantidad:.2f}")
        else:
            print('La cuenta no está en existencia')
    def registrar(self, numero, tipo, cantidad):
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.movimientos[numero].append((fecha, tipo, cantidad))
    def guardardatos(self):
        with open('cuentas.txt', 'w') as f:
            for numero, cuenta in self.cuentas.items():
                f.write(f"{numero} {cuenta['tipo']} {cuenta['saldo']}\n")
        
        with open('movimientos.txt', 'w') as f:
            for numero, movs in self.movimientos.items():
                for mov in movs:
                    fecha, tipo, cantidad = mov
                    f.write(f"{numero} {fecha} {tipo} {cantidad}\n")
        print('Sus datos han sido guardados exitosamente')
cajero = Cajero()
cajero.menu()