import os
import pyaes

# Abrir o arquivo criptografado
file_name = "test_file.txt.thisisnotavirus"
file = open(file_name, "rb")
file_data = file.read()
file.close()

# Chave descriptografia
key = b"isnotavirustest"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# Remover o arquivo criptografado
os.remove(file_name)

# Criar o arquivo descriptografado
new_file = "test_file.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
