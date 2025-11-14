class calculadora:
    # Atributo da classe
    PI=3.1416

    # Metodos da classe
    def circunferencia(self,raio) -> float:
        return 2 * self.PI * raio
    def area(self,raio) -> float:
        return self.PI*raio**2
    