class Coche:
    def __init__(self, marca):
        self.__marca = marca      # atributo privado
        self.__velocidad = 0      # atributo privado

    def acelerar(self, incremento):
        self.__velocidad += incremento

    def frenar(self, decremento):
        self.__velocidad -= decremento
        if self.__velocidad < 0:
            self.__velocidad = 0

    def mostrar_datos(self):
        print(f"Marca: {self.__marca} | Velocidad: {self.__velocidad} km/h")


# Ejecución de prueba
mi_coche = Coche("Toyota")
mi_coche.acelerar(50)
mi_coche.mostrar_datos()
mi_coche.frenar(20)
mi_coche.mostrar_datos()

