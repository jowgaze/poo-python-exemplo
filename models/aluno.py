from .pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome: str, idade: int, matricula: str):
        super().__init__(nome, idade)
        self.__matricula = matricula
        self.__notas: list[float] = []

    @property
    def matricula(self) -> str:
        return self.__matricula

    @matricula.setter
    def matricula(self, nova_matricula: str) -> None:
        if not nova_matricula or not nova_matricula.strip():
            raise ValueError("Matricula não pode ser vazia")
        self.__matricula = nova_matricula

    @property
    def notas(self) -> list[float]:
        return self.__notas

    def add_nota(self, nova_nota: float) -> None:
        if 0 <= nova_nota <= 10:
            self.__notas.append(nova_nota)
        else:
            raise ValueError("Nota deve estar entre 0 e 10")

    def media(self) -> float:
        if not self.__notas:
            return 0
        return sum(self.__notas) / len(self.__notas)

    def situacao(self) -> str:
        if self.media() >= 7:
            return "Aprovado"
        elif self.media() >=4:
            return "Prova Final"
        return "Reprovado"

    def __str__(self) -> str:
        return f"{self.nome} - {self.idade} anos ({self.__matricula}): {self.media():.2f} ({self.situacao()})"
