class calculadora:
    # Atributo da classe
    PI=3.1416

    # Metodos da classe
    @staticmethod
    def circunferencia(raio) -> float:
        return 2*calculadora.PI*raio
    @staticmethod
    def area(raio) -> float:
        return calculadora.PI*raio**2
    