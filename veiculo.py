class Veiculo:
    def __init__(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem):
        self.marca = marca
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao
        self.chassi = chassi
        self.cor = cor
        self.quilometragem = quilometragem

    def registrar_manutencao(self, tipo, custo):
        print(f"Manutenção do tipo {tipo} realizada. Custo: R${custo:.2f}")

    def exibir_informacoes(self, detalhado=False):
        if detalhado:
            print(f"Marca: {self.marca}")
            print(f"Modelo: {self.modelo}")
            print(f"Ano de Fabricação: {self.ano_fabricacao}")
            print(f"Chassi: {self.chassi}")
            print(f"Cor: {self.cor}")
            print(f"Quilometragem: {self.quilometragem} km")
        else:
            print(f"Marca: {self.marca}")
            print(f"Modelo: {self.modelo}")
            print(f"Quilometragem: {self.quilometragem} km")


class CarroPasseio(Veiculo):
    def __init__(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem, numero_portas, tipo_combustivel):
        super().__init__(marca, modelo, ano_fabricacao, chassi, cor, quilometragem)
        self.numero_portas = numero_portas
        self.tipo_combustivel = tipo_combustivel

    def calcular_depreciacao(self, anos_uso, taxa_extra):
        depreciacao = anos_uso * 0.15
        depreciacao_total = depreciacao + (taxa_extra * anos_uso)
        return depreciacao_total

    def exibir_informacoes(self, detalhado=False):
        super().exibir_informacoes(detalhado)
        if detalhado:
            print(f"Número de Portas: {self.numero_portas}")
            print(f"Tipo de Combustível: {self.tipo_combustivel}")


class CaminhaoCarga(Veiculo):
    def __init__(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem, capacidade_toneladas, eixos):
        super().__init__(marca, modelo, ano_fabricacao, chassi, cor, quilometragem)
        self.capacidade_toneladas = capacidade_toneladas
        self.eixos = eixos

    def registrar_vistoria(self, motivo, multa=0):
        print(f"Vistoria realizada. Motivo: {motivo}. Multa: R${multa:.2f}")

    def exibir_informacoes(self, detalhado=False):
        super().exibir_informacoes(detalhado)
        if detalhado:
            print(f"Capacidade de Carga: {self.capacidade_toneladas} toneladas")
            print(f"Número de Eixos: {self.eixos}")
