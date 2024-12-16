# Gestor de Tareas - Proyecto en Python

## Descripción

Este proyecto es un **gestor de tareas** que permite a los usuarios crear, gestionar y actualizar el estado de sus tareas. El sistema utiliza el paradigma de **Programación Orientada a Objetos** (POO) y está construido en Python.

### Características

- Los usuarios pueden crear tareas con una descripción, un estado inicial y una fecha límite.
- Los usuarios pueden ver todas sus tareas.
- Los usuarios pueden cambiar el estado de las tareas entre "pendiente", "en progreso", y "completa".
- El sistema permite la gestión de tareas de forma simple y eficiente.

## Tecnologías Utilizadas

- Python 3.x
- Programación Orientada a Objetos (POO)

## Instalación

1. **Clona este repositorio** en tu máquina local:
    ```bash
    git clone https://github.com/tuusuario/gestor-tareas.git
    ```

2. **Accede al directorio del proyecto**:
    ```bash
    cd gestor-tareas
    ```

3. **Instala Python 3** si no lo tienes instalado. Puedes verificar la instalación con:
    ```bash
    python --version
    ```

4. No es necesario instalar dependencias adicionales, ya que el proyecto solo depende de Python.

## Uso

1. **Crear un usuario**: Para crear un usuario, crea un objeto de la clase `Usuario` con el nombre del usuario.
    ```python
    usuario1 = Usuario("Juan")
    ```

2. **Crear tareas**: Crea tareas usando la clase `Tarea` y define el nombre, descripción, estado y fecha límite de la tarea.
    ```python
    tarea1 = Tarea("Estudiar matemáticas", "Repasar ecuaciones de segundo grado", "pendiente", "2024-12-16")
    ```

3. **Agregar tareas al usuario**: Una vez que tienes una tarea, puedes agregarla a la lista de tareas del usuario.
    ```python
    usuario1.agregar_tarea(tarea1)
    ```

4. **Ver tareas**: Puedes ver todas las tareas del usuario con el siguiente comando:
    ```python
    usuario1.ver_tareas()
    ```

5. **Cambiar el estado de una tarea**: Para actualizar el estado de una tarea (por ejemplo, marcarla como "completa"), usa el siguiente comando:
    ```python
    usuario1.cambiar_estado_tarea("Estudiar matemáticas", "completa")
    ```

## Ejemplo de Código

Aquí tienes un ejemplo de cómo usar el sistema de gestión de tareas:

```python
# Crear el usuario Juan
usuario1 = Usuario("Juan")

# Crear las tareas
tarea1 = Tarea("Estudiar matemáticas", "Repasar ecuaciones de segundo grado", "pendiente", "2024-12-16")
tarea2 = Tarea("Comprar alimentos", "Ir al supermercado y comprar alimentos para la semana", "pendiente", "2024-12-20")

# Agregar las tareas al usuario
usuario1.agregar_tarea(tarea1)
usuario1.agregar_tarea(tarea2)

# Ver las tareas de Juan
usuario1.ver_tareas()

# Cambiar el estado de la tarea de "Estudiar matemáticas" a "completa"
usuario1.cambiar_estado_tarea("Estudiar matemáticas", "completa")

# Ver las tareas de Juan después de actualizar el estado
usuario1.ver_tareas()
