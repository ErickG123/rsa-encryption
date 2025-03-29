from prime import gerar_primo
from math import gcd

def gerar_chaves(bits=128):
    p = gerar_primo(bits // 2)
    q = gerar_primo(bits // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    while gcd(e, phi) != 1:
        e += 2
    d = pow(e, -1, phi)
    return (n, e), (n, d)

def salvar_chave(nome_arquivo, chave):
    with open(nome_arquivo, "w") as f:
        f.write(f"{chave[0]},{chave[1]}")

def carregar_chave(nome_arquivo):
    with open(nome_arquivo, "r") as f:
        n, exp = map(int, f.read().split(","))
    return n, exp
