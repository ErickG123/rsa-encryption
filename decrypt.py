def carregar_criptografia(nome_arquivo):
    with open(nome_arquivo, "r") as f:
        return list(map(int, f.read().split(",")))

def decriptografar(mensagem_cripto, chave_privada):
    n, d = chave_privada
    return "".join(chr(pow(char, d, n)) for char in mensagem_cripto)
