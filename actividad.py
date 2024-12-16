# Clase Tarea
class Tarea:
    def __init__(self, nombre, fecha_vencimiento):
        self.nombre = nombre
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = "Pendiente"
    
    def marcar_completada(self):
        self.estado = "Completada"
    
    def __str__(self):
        return f"Tarea: {self.nombre}, Vencimiento: {self.fecha_vencimiento}, Estado: {self.estado}"

# Clase GestorDeTareas
class GestorDeTareas:
    def __init__(self):
        self.tareas = []
    
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
    
    def eliminar_tarea(self, nombre_tarea):
        for tarea in self.tareas:
            if tarea.nombre == nombre_tarea:
                self.tareas.remove(tarea)
                return f"Tarea '{nombre_tarea}' eliminada."
        return "Tarea no encontrada."
    
    def mostrar_tareas(self):
        if not self.tareas:
            return "No hay tareas."
        return "\n".join(str(tarea) for tarea in self.tareas)
    
    def completar_tarea(self, nombre_tarea):
        for tarea in self.tareas:
            if tarea.nombre == nombre_tarea:
                tarea.marcar_completada()
                return f"Tarea '{nombre_tarea}' marcada como completada."
        return "Tarea no encontrada."

# Ejemplo de uso del Gestor de Tareas
gestor = GestorDeTareas()

# Agregar tareas
tarea1 = Tarea("Comprar comida", "2024-12-20")
tarea2 = Tarea("Estudiar Python", "2024-12-21")

gestor.agregar_tarea(tarea1)
gestor.agregar_tarea(tarea2)

# Mostrar tareas
print(gestor.mostrar_tareas())

# Completar tarea
gestor.completar_tarea("Comprar comida")
print(gestor.mostrar_tareas())

# Eliminar tarea
gestor.eliminar_tarea("Estudiar Python")
print(gestor.mostrar_tareas())