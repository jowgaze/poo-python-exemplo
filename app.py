from models import Aluno, Turma

# Criando alunos
a1 = Aluno("José Maria", 20, "A123")
a2 = Aluno("Maria José", 22, "B456")

# Criando turma
turma = Turma("Escolinha do Python")

# Adicionando alunos
turma.add_aluno(a1)
turma.add_aluno(a2)

# Adicionando notas de a1
turma.add_nota("A123", 9.0)
turma.add_nota("A123", 10.0)
turma.add_nota("A123", 1.0)

# Adicionando notas de a2
turma.add_nota("B456", 9.0)
turma.add_nota("B456", 10.0)
turma.add_nota("B456", 8.0)

# Listando médias
turma.listar_medias()