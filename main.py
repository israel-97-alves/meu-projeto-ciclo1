from veiculo import CarroPasseio, CaminhaoCarga

def main():
    # Criando instâncias dos veículos
    carro = CarroPasseio(
        marca="Toyota",
        modelo="Corolla",
        ano_fabricacao=2020,
        chassi="ABC1234",
        cor="Prata",
        quilometragem=25000.0,
        numero_portas=4,
        tipo_combustivel="Gasolina"
    )

    caminhao = CaminhaoCarga(
        marca="Volvo",
        modelo="FH",
        ano_fabricacao=2018,
        chassi="XYZ5678",
        cor="Preto",
        quilometragem=180000.0,
        capacidade_toneladas=20.0,
        eixos=6
    )

    # Registrando manutenções
    carro.registrar_manutencao("Troca de óleo", 200.00)
    caminhao.registrar_manutencao("Troca de pneus", 1000.00)

    # Exibindo informações detalhadas
    print("\nInformações detalhadas do Carro Passeio:")
    carro.exibir_informacoes(detalhado=True)

    print("\nInformações detalhadas do Caminhão de Carga:")
    caminhao.exibir_informacoes(detalhado=True)

    # Depreciação do carro
    depreciacao = carro.calcular_depreciacao(anos_uso=5, taxa_extra=0.02)
    print(f"\nDepreciação do Carro após 5 anos: {depreciacao:.2f}")

    # Vistoria do caminhão
    caminhao.registrar_vistoria("Inspeção obrigatória", multa=150.00)


if __name__ == "__main__":
    main()
