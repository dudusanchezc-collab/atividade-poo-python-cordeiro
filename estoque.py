class estoque:
    def __init__(self, ingrediente):
        self.ingrediente = ingrediente
        self.calor = 0;
        self.temperatura = 0

    def temperar(self):
        print("Comida temperada")

    def esquentar(self):
        self.temperatura += 10
        print("Esquentando")
        print("Temperatura", self.temperatura)

e = estoque("Arroz")

e.temperar()
e.esquentar()
e.esquentar()

    
    