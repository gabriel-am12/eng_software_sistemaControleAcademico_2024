def criar_usuario(usuarios, dados):
    username = dados['username']
    usuarios[username] = {
        "senha": dados['senha'],
        "tipo": dados['tipo']
    }
    print("Usuário criado com sucesso.")

def login(usuarios, username, senha):
    if username in usuarios and usuarios[username]["senha"] == senha:
        print("Login bem-sucedido!")
        return username, usuarios[username]["tipo"]
    else:
        return None, None
