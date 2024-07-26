def adicionar_professor(professores, dados):
    id_professor = dados['id_professor']
    professores[id_professor] = {
        "nome": dados['nome'],
        "departamento": dados['departamento'],
        "email": dados['email']
    }
    print("Professor adicionado com sucesso.")

def consultar_professor(professores, id_professor):
    professor = professores.get(id_professor)
    if professor:
        return professor
    else:
        return "Professor não encontrado."
