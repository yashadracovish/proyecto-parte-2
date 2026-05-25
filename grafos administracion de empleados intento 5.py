class NodoEmpleado:
    def __init__(self, nombre, nacimiento, cedula, direccion, telefono, correo, cuenta):
        self.nombre = nombre
        self.nacimiento = nacimiento
        self.cedula = cedula
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.cuenta = cuenta

    def __str__(self):
        return (f"  Nombre   : {self.nombre}\n"
                f"  Cédula   : {self.cedula}\n"
                f"  Teléfono : {self.telefono}\n"
                f"  Correo   : {self.correo}\n"
                f"  Dirección: {self.direccion}\n"
                f"  Cuenta   : {self.cuenta}\n"
                f"  Nac.     : {self.nacimiento}")


class NodoArea:
    def __init__(self, Codigo, nombre):
        self.Codigo = Codigo
        self.nombre = nombre
        self.empleados = {}
        self.adyacentes = []


class GrafoEmpleados:

    def __init__(self):
        self.areas = {}

    def agregar_area(self, Codigo, nombre):
        if Codigo in self.areas:
            print(f"  [!] Ya existe el área '{Codigo}'.")
            return
        self.areas[Codigo] = NodoArea(Codigo, nombre)
        print(f"  [OK] Área '{nombre}' ({Codigo}) agregada.")

    def eliminarArea(self, Codigo):
        if Codigo not in self.areas:
            print(f"  [!] Área '{Codigo}' no encontrada.")
            return
        for area in self.areas.values():
            if Codigo in area.adyacentes:
                area.adyacentes.remove(Codigo)
        nombre = self.areas[Codigo].nombre
        del self.areas[Codigo]
        print(f"  [OK] Área '{nombre}' ({Codigo}) eliminada junto con sus conexiones.")

    def buscar_area(self, Codigo):
        area = self.areas.get(Codigo)
        if area is None:
            print(f"  [!] Área '{Codigo}' no encontrada.")
            return None
        print(f"\n  Área: {area.nombre} (código: {area.Codigo})")
        print(f"  Conectada con: {area.adyacentes if area.adyacentes else 'ninguna'}")
        print(f"  Empleados ({len(area.empleados)}):")
        if area.empleados:
            for emp in area.empleados.values():
                print(f"    - {emp.nombre} | Cédula: {emp.cedula}")
        else:
            print("    (sin empleados)")
        return area

    def mostrar_areas(self):
        if not self.areas:
            print("  No hay áreas registradas.")
            return
        print(f"\n  {'CÓDIGO':<12} {'NOMBRE':<25} {'EMPLEADOS':>10}  CONECTADA CON")
        print("  " + "-"*65)
        for area in self.areas.values():
            print(f"  {area.Codigo:<12} {area.nombre:<25} {len(area.empleados):>10}  {area.adyacentes}")

    def conectar_areas(self, codigo1, codigo2):
        if codigo1 not in self.areas or codigo2 not in self.areas:
            print("  [!] Una o ambas áreas no existen.")
            return
        if codigo2 not in self.areas[codigo1].adyacentes:
            self.areas[codigo1].adyacentes.append(codigo2)
        if codigo1 not in self.areas[codigo2].adyacentes:
            self.areas[codigo2].adyacentes.append(codigo1)
        print(f"  [OK] Áreas '{codigo1}' y '{codigo2}' conectadas.")

    def desconectarAreas(self, codigo1, codigo2):
        if codigo1 not in self.areas or codigo2 not in self.areas:
            print("  [!] Una o ambas áreas no existen.")
            return
        if codigo2 in self.areas[codigo1].adyacentes:
            self.areas[codigo1].adyacentes.remove(codigo2)
        if codigo1 in self.areas[codigo2].adyacentes:
            self.areas[codigo2].adyacentes.remove(codigo1)
        print(f"  [OK] Conexión entre '{codigo1}' y '{codigo2}' eliminada.")

    def insertar_empleado(self, codigoArea, Nombre, nacimiento, cedula,
                          Direccion, telefono, correo, cuenta):
        if codigoArea not in self.areas:
            print(f"  [!] Área '{codigoArea}' no existe. Crea el área primero.")
            return
        area = self.areas[codigoArea]
        if cedula in area.empleados:
            print(f"  [!] Ya existe un empleado con cédula {cedula} en esta área.")
            return
        for a in self.areas.values():
            if cedula in a.empleados:
                print(f"  [!] La cédula {cedula} ya está registrada en el área '{a.nombre}'.")
                return
        area.empleados[cedula] = NodoEmpleado(
            Nombre, nacimiento, cedula, Direccion, telefono, correo, cuenta)
        print(f"  [OK] Empleado '{Nombre}' agregado al área '{area.nombre}'.")

    def eliminarEmpleado(self, cedula):
        for area in self.areas.values():
            if cedula in area.empleados:
                Nombre = area.empleados[cedula].nombre
                del area.empleados[cedula]
                print(f"  [OK] Empleado '{Nombre}' (cédula: {cedula}) eliminado del área '{area.nombre}'.")
                return
        print(f"  [!] No se encontró ningún empleado con cédula {cedula}.")

    def buscar_empleado(self, cedula):
        for area in self.areas.values():
            if cedula in area.empleados:
                emp = area.empleados[cedula]
                print(f"\n  Empleado encontrado en área: {area.nombre} ({area.Codigo})")
                print(emp)
                return emp
        print(f"  [!] No se encontró ningún empleado con cédula {cedula}.")
        return None

    def mostrarEmpleadosDeArea(self, codigoArea):
        if codigoArea not in self.areas:
            print(f"  [!] Área '{codigoArea}' no existe.")
            return
        area = self.areas[codigoArea]
        print(f"\n  Empleados del área '{area.nombre}':")
        if not area.empleados:
            print("    (sin empleados)")
        else:
            for emp in area.empleados.values():
                print(f"\n{emp}")

    def bfs(self, nodoInicio):
        if nodoInicio not in self.areas:
            print(f"  [!] Área '{nodoInicio}' no existe.")
            return
        visitados = set()
        Cola = [nodoInicio]
        visitados.add(nodoInicio)
        print(f"\n  BFS desde '{nodoInicio}':")
        while Cola:
            codigo = Cola.pop(0)
            area = self.areas[codigo]
            print(f"    -> {area.nombre} ({codigo}) | {len(area.empleados)} empleado(s)")
            for vecino in area.adyacentes:
                if vecino not in visitados:
                    visitados.add(vecino)
                    Cola.append(vecino)

    def dfs(self, nodoInicio, visitados=None):
        if nodoInicio not in self.areas:
            print(f"  [!] Área '{nodoInicio}' no existe.")
            return
        if visitados is None:
            visitados = set()
            print(f"\n  DFS desde '{nodoInicio}':")
        visitados.add(nodoInicio)
        area = self.areas[nodoInicio]
        print(f"    -> {area.nombre} ({nodoInicio}) | {len(area.empleados)} empleado(s)")
        for vecino in area.adyacentes:
            if vecino not in visitados:
                self.dfs(vecino, visitados)

    def ruta_entre_areas(self, nodo_origen, nodo_destino):
        if nodo_origen not in self.areas or nodo_destino not in self.areas:
            print("  [!] Una o ambas áreas no existen.")
            return
        if nodo_origen == nodo_destino:
            print("  Son la misma área.")
            return
        visitados = set()
        Cola = [(nodo_origen, [nodo_origen])]
        visitados.add(nodo_origen)
        while Cola:
            actual, ruta = Cola.pop(0)
            for vecino in self.areas[actual].adyacentes:
                if vecino == nodo_destino:
                    ruta_final = ruta + [vecino]
                    nombres = [f"{self.areas[c].nombre}({c})" for c in ruta_final]
                    print(f"  [OK] Ruta encontrada: {' -> '.join(nombres)}")
                    return
                if vecino not in visitados:
                    visitados.add(vecino)
                    Cola.append((vecino, ruta + [vecino]))
        print(f"  [!] No existe ruta entre '{nodo_origen}' y '{nodo_destino}'.")


def menu():
    grafo = GrafoEmpleados()

    grafo.agregar_area("TI", "Tecnología e Innovación")
    grafo.agregar_area("RH", "Recursos Humanos")
    grafo.agregar_area("FIN", "Finanzas")
    grafo.agregar_area("OPS", "Operaciones")
    grafo.conectar_areas("TI", "RH")
    grafo.conectar_areas("RH", "FIN")
    grafo.conectar_areas("FIN", "OPS")
    grafo.conectar_areas("TI", "OPS")
    grafo.insertar_empleado("TI", "Ana Torres", "1990-05-12", "1001",
                            "Cra 10 #20-30", "3101234567", "ana@empresa.com", "001-123")
    grafo.insertar_empleado("TI", "Luis Pérez", "1988-03-22", "1002",
                            "Calle 5 #8-15", "3209876543", "luis@empresa.com", "001-456")
    grafo.insertar_empleado("RH", "María Gómez", "1992-07-01", "1003",
                            "Av 30 #45-60", "3154567890", "maria@empresa.com", "002-789")
    grafo.insertar_empleado("FIN", "Carlos Ruiz", "1985-11-30", "1004",
                            "Calle 1 #2-3", "3001112233", "carlos@empresa.com", "003-321")

    while True:
       
        print("  SISTEMA DE GESTIÓN DE EMPLEADOS — GRAFO")
        
        print("   ÁREAS (VÉRTICES) ")
        print("   1. Agregar área")
        print("   2. Eliminar área")
        print("   3. Buscar área")
        print("   4. Mostrar todas las áreas")
        print("   CONEXIONES (ARISTAS) ")
        print("   5. Conectar dos áreas")
        print("   6. Desconectar dos áreas")
        print("   EMPLEADOS ")
        print("   7. Insertar empleado en área")
        print("   8. Eliminar empleado por cédula")
        print("   9. Buscar empleado por cédula")
        print("  10. Mostrar empleados de un área")
        print("  RECORRIDOS ")
        print("  11. Recorrido BFS desde un área")
        print("  12. Recorrido DFS desde un área")
        print("  13. Buscar ruta entre dos áreas")
        print("   SALIR ")
        print("   0. Salir")
        print("═"*55)

        try:
            op = int(input("  Seleccione opción: "))
        except ValueError:
            print("   Ingrese un número válido.")
            continue

        if op == 0:
            print("  saliendo.")
            break

        elif op == 1:
            Codigo = input("  Código del área: ").strip().upper()
            nombre = input("  Nombre del área: ").strip()
            grafo.agregar_area(Codigo, nombre)

        elif op == 2:
            Codigo = input("  Código del área a eliminar: ").strip().upper()
            grafo.eliminarArea(Codigo)

        elif op == 3:
            Codigo = input("  Código del área: ").strip().upper()
            grafo.buscar_area(Codigo)

        elif op == 4:
            grafo.mostrar_areas()

        elif op == 5:
            c1 = input("  Código área 1: ").strip().upper()
            c2 = input("  Código área 2: ").strip().upper()
            grafo.conectar_areas(c1, c2)

        elif op == 6:
            c1 = input("  Código área 1: ").strip().upper()
            c2 = input("  Código área 2: ").strip().upper()
            grafo.desconectarAreas(c1, c2)

        elif op == 7:
            codigoArea = input("  Código del área: ").strip().upper()
            Nombre = input("  Nombre del empleado: ").strip()
            nacimiento = input("  Fecha de nacimiento: ").strip()
            cedula = input("  Cédula: ").strip()
            Direccion = input("  Dirección: ").strip()
            telefono = input("  Teléfono: ").strip()
            correo = input("  Correo: ").strip()
            cuenta = input("  Cuenta bancaria: ").strip()
            grafo.insertar_empleado(codigoArea, Nombre, nacimiento, cedula,
                                    Direccion, telefono, correo, cuenta)

        elif op == 8:
            cedula = input("  Cédula del empleado: ").strip()
            grafo.eliminarEmpleado(cedula)

        elif op == 9:
            cedula = input("  Cédula a buscar: ").strip()
            grafo.buscar_empleado(cedula)

        elif op == 10:
            codigoArea = input("  Código del área: ").strip().upper()
            grafo.mostrarEmpleadosDeArea(codigoArea)

        elif op == 11:
            nodoInicio = input("  Código del área de inicio: ").strip().upper()
            grafo.bfs(nodoInicio)

        elif op == 12:
            nodoInicio = input("  Código del área de inicio: ").strip().upper()
            grafo.dfs(nodoInicio)

        elif op == 13:
            nodo_origen = input("  Código área origen: ").strip().upper()
            nodo_destino = input("  Código área destino: ").strip().upper()
            grafo.ruta_entre_areas(nodo_origen, nodo_destino)

        else:
            print("  [!] Opción inválida.")


if __name__ == "__main__":
    menu()
