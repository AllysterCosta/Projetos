import secrets

numero = secrets.token_bytes(10)
print(f"Número aleatório seguro: {numero}")

hextoken = secrets.token_hex(16)
print(f"Token hexadecimal seguro: {hextoken}")

senhaurl = secrets.token_urlsafe(16)
print(f"Senha segura gerada: {senhaurl}")
