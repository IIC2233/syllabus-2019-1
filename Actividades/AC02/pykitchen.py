class PyKitchen:
    def __init__(self, chefs, clientes):
        self.chefs = chefs
        self.clientes = clientes

    def atender(self):
        for i in range(3):  # Se hace el estudio por 3 días
            print(f"----- Día {i + 1} -----")
            platos = []
            for chef in self.chefs:
                for j in range(2):  # Cada chef cocina 2 platos
                    platos.append(chef.cocinar())  # Retorna los platos
            for cliente in self.clientes:
                for plato in platos:
                    cliente.comer(plato)
