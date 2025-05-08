class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str) -> None:
        if not novo_nome or not novo_nome.strip():
            raise ValueError("Não pode ser vazio")
        self.__nome = novo_nome

    @property
    def idade(self) -> int:
        return self.__idade

    @idade.setter
    def idade(self, nova_idade: int) -> None:
        if not nova_idade or nova_idade < 0:
            raise ValueError("Não pode ser vazio ou menor que 0")
        self.__idade = nova_idade

    def __str__(self) -> str:
        return f"Nome: {self.__nome}, Idade: {self.__idade}"
