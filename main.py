from rsa.key_generation import generate_keys_carmichael
from rsa.encryption import rsa_encrypt
from rsa.decryption import rsa_decrypt

def main():

    public_key, private_key = generate_keys_carmichael(61, 53, 17)

    message = "CARLOS"

    ciphertext = rsa_encrypt(message, public_key)
    plaintext = rsa_decrypt(ciphertext, private_key)

    print("Original message:", message)
    print("Public key:", public_key)
    print("Private key:", private_key)
    print("Encrypted blocks:", ciphertext)
    print("Decrypted message:", plaintext)

if __name__ == "__main__":
    main()