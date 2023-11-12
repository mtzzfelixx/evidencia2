class Persona:
    def inicializar(self, nombre):
        self.nombre = nombre
        
    def mostrar(self):
        print("Nombre:",self.nombre)
        
#bloque principal
persona1 = Persona()
persona1.inicializar("Felix")
persona1.mostrar()
