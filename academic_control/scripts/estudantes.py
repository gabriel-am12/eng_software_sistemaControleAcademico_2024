def adicionar_estudante(estudantes, dados):
    matricula = dados['matricula']
    estudantes[matricula] = {
        "nome": dados['nome'],
        "data_nascimento": str(dados['data_nascimento']),
        "endereco": dados['endereco'],
        "disciplinas": {}
    }
    print("Estudante adicionado com sucesso.")

def consultar_estudante(estudantes, matricula):
    estudante = estudantes.get(matricula)
    if estudante:
        return estudante
    else:
        return "Estudante não encontrado."
