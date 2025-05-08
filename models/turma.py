from .aluno import Aluno


class Turma:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__alunos: list[Aluno] = []

    def add_aluno(self, aluno: Aluno):
        self.__alunos.append(aluno)

    def add_nota(self, matricula: str, nota: float) -> None:
        for aluno in self.__alunos:
            if aluno.matricula == matricula:
                aluno.add_nota(nota)
                return
        print("Aluno não encontrado")

    def listar_medias(self) -> None:
        for aluno in self.__alunos:
            print(aluno)

