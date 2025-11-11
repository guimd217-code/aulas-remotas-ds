class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f"Marca: {self.marca} | Modelo: {self.modelo}"


class Carro(Veiculo):  # Classe filha herdando da classe pai
    def __init__(self, marca, modelo, numero_portas):
        super().__init__(marca, modelo)  # Herda atributos da classe Veiculo
        self.numero_portas = numero_portas

    def exibir_info(self):
        return f"Marca: {self.marca} | Modelo: {self.modelo} | Portas: {self.numero_portas}"

carro1 = Carro("Toyota", "Corolla", 4)
print(carro1.exibir_info())