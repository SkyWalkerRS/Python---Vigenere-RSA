from rsa import Rsa
from vigenere import Vigenere

import time
import binascii

while True:
    msg = input('Mensagem a ser cifrada: ')
    key = input('Chave: ')

    cipher = Vigenere()
    rsa = Rsa()
    start = time.time()
    cipherText = cipher.encrypt(msg.upper(), key)
    keyPublic = rsa.createPublicKey()
    keyPrivate = rsa.createPrivateKey()
    encryptedText = rsa.encript(cipherText.encode(), keyPublic)
    decodedText = rsa.decript(encryptedText, keyPrivate.upper())
    texto_original = cipher.decrypt(decodedText.decode(), key)

    finish = time.time()
    print('Texto encriptado em Vigenere:',cipherText)
    print('\nTexto encriptado em RSA:', binascii.hexlify(encryptedText))
    print('\nTexto decriptado em RSA:' + decodedText.decode())
    print('\nTexto decriptado em Vigenere: ' + texto_original)
    print('\nTempo de Duração: ' + str(finish - start))
    outra = input('\nQuer testar outra frase?\n1-Para sim')
    if outra != '1':
        break

#joga pro alto e reza
#aaron rodgers
#VURZIJSQWGHRYASJMXOGMRCEWXHV
#gadod+