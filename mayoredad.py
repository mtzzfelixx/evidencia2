class Persona:
    def inicializar(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def mostrar(self):
        print("Nombre:",self.nombre)
        print("Edad",self.edad)
    
    def mayor_edad(self):
        if self.edad >= 18:
            print("ES mayor de edad.")
        else:
            print("No es mayor de edad.")

#Bloque principal
persona1 = Persona()
persona1.inicializar("Felix", 19)
persona1.mostrar()
persona1.mayor_edad()
print("")
persona2 = Persona()
persona2.inicializar("Roberto", 16)
persona2.mostrar()
persona2.mayor_edad()