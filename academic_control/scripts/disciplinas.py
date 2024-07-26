def adicionar_disciplina(disciplinas, dados):
    codigo = dados['codigo']
    disciplinas[codigo] = {
        "nome": dados['nome'],
        "carga_horaria": dados['carga_horaria'],
        "pre_requisitos": dados['pre_requisitos'],
        "programa": dados['programa'],
        "turmas": {}
    }
    print("Disciplina adicionada com sucesso.")

def consultar_disciplina(disciplinas, codigo):
    disciplina = disciplinas.get(codigo)
    if disciplina:
        return disciplina
    else:
        return "Disciplina não encontrada."
