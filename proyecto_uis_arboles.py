class NodoEmpleado:
    def __init__(self, nombre, nacimiento, cedula, direccion, telefono, correo, cuenta):
        self.nombre = nombre
        self.nacimiento = nacimiento
        self.cedula = cedula
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.cuenta = cuenta
        self.izquierdo = None
        self.derecho = None


class NodoSeguridad:
    def __init__(self, codigo_area, cedula):
        self.codigo_area = codigo_area
        self.cedula = cedula
        self.izquierdo = None
        self.derecho = None


class ArbolEmpleados:

    def __init__(self):
        self.raiz = None

    def insertar(self, nodo, nombre, nacimiento, cedula, direccion, telefono, correo, cuenta):
        if nodo == None:
            return NodoEmpleado(nombre, nacimiento, cedula, direccion, telefono, correo, cuenta)
        if cedula < nodo.cedula:
            nodo.izquierdo = self.insertar(nodo.izquierdo, nombre, nacimiento, cedula, direccion, telefono, correo, cuenta)
        elif cedula > nodo.cedula:
            nodo.derecho = self.insertar(nodo.derecho, nombre, nacimiento, cedula, direccion, telefono, correo, cuenta)
        else:
            print("Ya existe un empleado con esa cedula")
        return nodo

    def agregar(self, nombre, nacimiento, cedula, direccion, telefono, correo, cuenta):
        self.raiz = self.insertar(self.raiz, nombre, nacimiento, cedula, direccion, telefono, correo, cuenta)
        print("Empleado agregado")

    def buscar(self, nodo, cedula):
        if nodo == None:
            return None
        if cedula == nodo.cedula:
            return nodo
        elif cedula < nodo.cedula:
            return self.buscar(nodo.izquierdo, cedula)
        else:
            return self.buscar(nodo.derecho, cedula)

    def minimo(self, nodo):
        while nodo.izquierdo != None:
            nodo = nodo.izquierdo
        return nodo

    def eliminar(self, nodo, cedula):
        if nodo == None:
            print("Empleado no encontrado")
            return None
        if cedula < nodo.cedula:
            nodo.izquierdo = self.eliminar(nodo.izquierdo, cedula)
        elif cedula > nodo.cedula:
            nodo.derecho = self.eliminar(nodo.derecho, cedula)
        else:
            if nodo.izquierdo == None:
                print("Empleado eliminado")
                return nodo.derecho
            elif nodo.derecho == None:
                print("Empleado eliminado")
                return nodo.izquierdo
            sucesor = self.minimo(nodo.derecho)
            nodo.cedula = sucesor.cedula
            nodo.nombre = sucesor.nombre
            nodo.nacimiento = sucesor.nacimiento
            nodo.direccion = sucesor.direccion
            nodo.telefono = sucesor.telefono
            nodo.correo = sucesor.correo
            nodo.cuenta = sucesor.cuenta
            nodo.derecho = self.eliminar(nodo.derecho, sucesor.cedula)
        return nodo

    def inorden(self, nodo):
        if nodo == None:
            return
        self.inorden(nodo.izquierdo)
        print(nodo.nombre, nodo.cedula, nodo.telefono)
        self.inorden(nodo.derecho)

    def mostrar(self):
        if self.raiz == None:
            print("No hay empleados")
        else:
            self.inorden(self.raiz)


class ArbolSeguridad:

    def __init__(self):
        self.raiz = None

    def insertar(self, nodo, codigo_area, cedula):
        if nodo == None:
            return NodoSeguridad(codigo_area, cedula)
        if codigo_area < nodo.codigo_area:
            nodo.izquierdo = self.insertar(nodo.izquierdo, codigo_area, cedula)
        elif codigo_area > nodo.codigo_area:
            nodo.derecho = self.insertar(nodo.derecho, codigo_area, cedula)
        else:
            print("Ya existe ese codigo de area")
        return nodo

    def registrar(self, codigo_area, cedula):
        self.raiz = self.insertar(self.raiz, codigo_area, cedula)
        print("Registro agregado")

    def consultar_empleado(self, cedula, arbol_empleados):
        empleado = arbol_empleados.buscar(arbol_empleados.raiz, cedula)
        if empleado != None:
            print("Nombre:", empleado.nombre)
            print("Cedula:", empleado.cedula)
            print("Telefono:", empleado.telefono)
            print("Correo:", empleado.correo)
        else:
            print("Empleado no encontrado")


AE = ArbolEmpleados()
AS = ArbolSeguridad()

while True:

    print("\nMENU")
    print("1 Agregar empleado")
    print("2 Eliminar empleado")
    print("3 Mostrar empleados")
    print("4 Seguridad consultar empleado")
    print("5 Salir")

    op = int(input("Seleccione opcion: "))

    if op == 1:
        nombre = input("Nombre: ")
        nacimiento = input("Nacimiento: ")
        cedula = input("Cedula: ")
        direccion = input("Direccion: ")
        telefono = input("Telefono: ")
        correo = input("Correo: ")
        cuenta = input("Cuenta bancaria: ")
        AE.agregar(nombre, nacimiento, cedula, direccion, telefono, correo, cuenta)

    elif op == 2:
        cedula = input("Cedula del empleado a eliminar: ")
        AE.raiz = AE.eliminar(AE.raiz, cedula)

    elif op == 3:
        AE.mostrar()

    elif op == 4:
        cedula = input("Cedula a consultar: ")
        AS.consultar_empleado(cedula, AE)

    elif op == 5:
        break

    else:
        print("Opcion invalida")
