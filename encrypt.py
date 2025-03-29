def criptografar(mensagem, chave_publica):
    n, e = chave_publica
    return [pow(ord(char), e, n) for char in mensagem]

def salvar_criptografia(nome_arquivo, mensagem_cripto):
    with open(nome_arquivo, "w") as f:
        f.write(",".join(map(str, mensagem_cripto)))
