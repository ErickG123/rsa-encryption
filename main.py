from keys import gerar_chaves, salvar_chave, carregar_chave
from encrypt import criptografar, salvar_criptografia
from decrypt import carregar_criptografia, decriptografar

def main():
    pub, priv = gerar_chaves()
    salvar_chave("chave_publica.cpa", pub)
    salvar_chave("chave_privada.csa", priv)
    print("Chaves geradas e salvas.")
    
    mensagem = input("Digite a mensagem para criptografar: ")
    mensagem_cripto = criptografar(mensagem, pub)
    salvar_criptografia("mensagem.cript", mensagem_cripto)
    print("Mensagem criptografada e salva.")
    
    mensagem_cripto = carregar_criptografia("mensagem.cript")
    mensagem_original = decriptografar(mensagem_cripto, priv)
    print("Mensagem decriptografada:", mensagem_original)

if __name__ == "__main__":
    main()
