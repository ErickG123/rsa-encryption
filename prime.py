import random

def eh_primo(n, k=5):
    if n < 2:
        return False
    for _ in range(k):
        a = random.randint(2, n - 1)
        if pow(a, n - 1, n) != 1:
            return False
    return True

def gerar_primo(bits):
    while True:
        candidato = random.getrandbits(bits) | 1
        if eh_primo(candidato):
            return candidato
