class Tarta1:
    def __init__(self,sabor_tarta):
        print ("constructor con", sabor_tarta)
        self.sabor = sabor_tarta
        self.puntuacion = 0
    
    def mayor_puntuacion(self, lista_tartas):
        mayor = lista_tartas[0]
        for element in lista_tartas:
            if element.puntuacion > mayor.puntuacion:
                mayor = element
        return mayor


tarta_chocolate = Tarta("chocolate")
tarta_nueces = Tarta("nueces")
tarta_coco = Tarta("coco")
tarta_zanahoria = Tarta ("zanahoria")
tarta_yogur= Tarta ("yogur")

tarta_chocolate.puntuacion = 5
tarta_nueces.puntuacion = 7
tarta_coco.puntuacion= 10
tarta_zanahoria = 0
tarta_yogur = 8
tarta_ganadora = mayor.puntuacion(lista_tartas)
    
print(tarta_ganadora)


class Tarta:
    # si yo ejecuto t=Tarta(), me dice que t es un objeto (que pertenece a la clase Tarta), incluso sin constructor. Se crea sin datos ni nada hasta que le ponemos el constructor
    



