# Sistema de Gestión de Empleados — Estructuras de Datos

**Universidad Industrial de Santander (UIS)**  
Asignatura: Estructuras de Datos

---

## Descripción del problema

Las empresas manejan grandes volúmenes de información sobre sus empleados y la estructura interna de sus departamentos. El objetivo de este proyecto es implementar y comparar distintas estructuras de datos para gestionar eficientemente dicha información: registrar, buscar, actualizar y eliminar registros de empleados, así como modelar las relaciones entre áreas de trabajo.

---

## Etapas del proyecto

### Etapa 1 — Lista enlazada

Implementación de una lista enlazada simple para almacenar empleados de forma secuencial.

- Inserción al inicio o al final
- Eliminación por cédula mediante recorrido lineal
- Búsqueda lineal O(n)

**Archivo:** `etapa1_lista_enlazada/lista_enlazada_empleados.py`

---

### Etapa 2 — Árbol Binario de Búsqueda (BST)

Implementación de un árbol BST donde los empleados se organizan por número de cédula, permitiendo búsquedas más eficientes que la lista enlazada.

Se incluyó además un árbol de seguridad (`ArbolSeguridad`) que relaciona códigos de área con cédulas, habilitando consultas de acceso restringido.

- Inserción ordenada por cédula
- Búsqueda O(log n) en caso promedio
- Eliminación con sucesor inorden
- Recorrido inorden para listar empleados en orden

**Archivo:** `etapa2_arbol_bst/proyecto_uis_arboles.py`

---

### Etapa 3 — Grafo (entrega final)

Implementación de un grafo no dirigido donde los vértices representan áreas o departamentos de la empresa, las aristas representan conexiones entre ellas (colaboración, dependencia jerárquica, flujo de información), y cada vértice contiene el conjunto de empleados asociados a ese departamento.

| Operación | Descripción |
|-----------|-------------|
| `agregar_area` | Inserta un vértice (área) |
| `eliminar_area` | Elimina un vértice y sus aristas |
| `buscar_area` | Muestra información de un área y sus empleados |
| `conectar_areas` | Crea una arista entre dos áreas |
| `desconectar_areas` | Elimina la arista entre dos áreas |
| `insertar_empleado` | Agrega un empleado a un área |
| `eliminar_empleado` | Elimina un empleado por cédula |
| `buscar_empleado` | Busca un empleado en todo el grafo |
| `bfs` | Recorrido en anchura desde un área |
| `dfs` | Recorrido en profundidad desde un área |
| `ruta_entre_areas` | Determina si existe ruta entre dos áreas |

**Archivo:** `etapa3_grafo/grafo_empleados.py`

---

## Comparación de eficiencias

| Operación | Lista enlazada | Arbol BST | Grafo |
|-----------|:--------------:|:---------:|:-----:|
| Insertar | O(1) / O(n) | O(log n) promedio | O(1) |
| Buscar por cedula | O(n) | O(log n) promedio | O(empleados del area) |
| Eliminar | O(n) | O(log n) promedio | O(empleados del area) |
| Relaciones entre departamentos | No | No | Si |
| Recorridos por conexiones | No | Inorden / Preorden | BFS / DFS |

### Estructura mas eficiente para el contexto

El grafo es la estructura mas adecuada para este problema por las siguientes razones:

1. Modela de forma natural la estructura organizacional de una empresa, representando tanto las entidades (areas) como sus relaciones.
2. Permite consultas de conectividad entre departamentos, utiles para auditorias, flujos de aprobacion y rutas de reporte.
3. La busqueda de empleados dentro de un area es O(1) gracias al diccionario interno.
4. Las operaciones sobre vertices y aristas son O(1) con el diccionario de areas.
5. Los recorridos BFS y DFS permiten analizar la topologia de la organizacion, algo que no es posible con las estructuras de las etapas anteriores.

---

## Como ejecutar

```bash
# Requiere Python 3.7 o superior
python etapa3_grafo/grafo_empleados.py
```

El programa carga datos de prueba automaticamente (4 areas y 4 empleados) para facilitar las demostraciones.

---

## Integrantes del grupo

| Nombre completo             | Codigo UIS |
|-----------------            |------------|
| JUAN JOSE JAUREGUI MENDOSA  | 2250920    |
| SERGIO ESTEBAN CONTRERAS    | 2250950    |
|                             |            |

---

## Estructura del repositorio

```
README.md
etapa1_lista_enlazada/
    lista_enlazada_empleados.py
etapa2_arbol_bst/
    proyecto_uis_arboles.py
etapa3_grafo/
    grafo_empleados.py
```
