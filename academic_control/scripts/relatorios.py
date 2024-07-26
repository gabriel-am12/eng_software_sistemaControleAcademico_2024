def gerar_boletim(estudantes):
    boletim = ""
    for matricula, dados in estudantes.items():
        boletim += f"Matrícula: {matricula}\n"
        boletim += f"Nome: {dados['nome']}\n"
        for disciplina, nota in dados['disciplinas'].items():
            boletim += f"Disciplina: {disciplina} - Nota: {nota}\n"
        boletim += "\n"
    return boletim

def gerar_boletim_completo(estudantes):
    boletim_completo = ""
    for matricula, dados in estudantes.items():
        boletim_completo += f"Matrícula: {matricula}\n"
        boletim_completo += f"Nome: {dados['nome']}\n"
        for disciplina, info in dados['disciplinas'].items():
            if isinstance(info, dict):
                nota = info.get('nota', 'N/A')
                frequencia = info.get('frequencia', 'N/A')
                boletim_completo += f"Disciplina: {disciplina} - Nota: {nota} - Frequência: {frequencia}%\n"
            else:
                boletim_completo += f"Disciplina: {disciplina} - Nota: {info}\n"
        boletim_completo += "\n"
    return boletim_completo
