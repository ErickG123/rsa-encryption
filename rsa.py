import sympy

# Função para gerar um número primo aleatório
def generate_prime(bits=16):
    return sympy.randprime(2**(bits-1), 2**bits)

# Função para calcular o inverso modular
def mod_inverse(e, phi):
    return pow(e, -1, phi)

# Gerar números primos aleatórios
p = generate_prime()
q = generate_prime()
n = p * q
phi_n = (p - 1) * (q - 1)

e = 65537  # Valor comum para e
d = mod_inverse(e, phi_n)

# Chaves RSA
public_key = (e, n)
private_key = (d, n)

print(f"Chaves RSA Geradas:\nPublic Key: {public_key}\nPrivate Key: {private_key}")

# Função para criptografar
def encrypt(message, e, n):
    return [pow(ord(char), e, n) for char in message]

# Função para descriptografar
def decrypt(ciphertext, d, n):
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

# Criptografar mensagem
message = "Olá, RSA!"
ciphertext = encrypt(message, public_key[0], public_key[1])
print(f"Mensagem criptografada: {ciphertext}")

# Descriptografar mensagem
decrypted_message = decrypt(ciphertext, private_key[0], private_key[1])
print(f"Mensagem descriptografada: {decrypted_message}")
