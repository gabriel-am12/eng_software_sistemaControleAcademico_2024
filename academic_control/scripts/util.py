import json
import os

def salvar_dados(dados, nome_arquivo):
    with open(nome_arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

def carregar_dados(nome_arquivo):
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as f:
            return json.load(f)
    return {}
