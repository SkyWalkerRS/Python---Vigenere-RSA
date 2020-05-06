class Vigenere:

    def encrypt(self, plaintext, password):
        key_length = len(password)
        key_as_int = [ord(i) for i in password]
        #print(key_as_int)
        plaintext_int = [ord(i) for i in plaintext]
        #print(plaintext_int)

        while 32 in plaintext_int:
            plaintext_int.remove(32)
        ciphertext = ''
        for i in range(len(plaintext_int)):
            value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
            ciphertext += chr(value + 65)
        return ciphertext

    def decrypt(self, ciphertext, password):
        key_length = len(password)
        key_as_int = [ord(i) for i in password]
        ciphertext_int = [ord(i) for i in ciphertext]
        #print("cjyperint:",ciphertext_int)
        plaintext = ''
        for i in range(len(ciphertext_int)):
            value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
            plaintext += chr(value + 65)
        return plaintext
