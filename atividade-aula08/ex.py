from cipher import aes_cipher, aes_cipher_decode
from histogram import save_histogram

def ex1():
    plaintext = "AES is a subset of the Rijndael block cipher developed by two Belgian cryptographers, Vincent Rijmen and Joan Daemen."
    key = bytes.fromhex("FD E8 F7 A9 B8 6C 3B FF 07 C0 D3 9D 04 60 5E DD")

    encrypted, blocks = aes_cipher(plaintext, key)
    print(f"Encrypted:")
    print(f"{encrypted.hex()}\n")

    decrypted, decrypted_blocks = aes_cipher_decode(encrypted, key)
    print(f"Decrypted:")
    print(f"{decrypted.decode()}\n")

    save_histogram(plaintext, "histogram_plaintext.png")
    save_histogram(encrypted, "histogram_aes.png")

    return plaintext

def ex2():
    ciphertext = (
        "25956395B60AA5BA2D44618266E432B5A48DF86B9F7C0AB8C10C33653118423D8A3BC9DEC32C4D"
        "9B430678687AF29550FDF697984CC5035DE497BCF2FB9165AF52E5E2E3A61BD8A9B1E7A862529AFB"
        "DD6FFEF81797F8ECB86DFB19693EB3CB7059A42905104F74E7D27B5737AFA27DEE29860FC30FBC12"
        "8F1F93A4F16F902D37AB04B6FDFF3AF16262E28E471D70C5080F1E85210D98B63554C3D3959C3B92"
        "DBDCD1660CB7334870F3FC1990A8BEEC788967E11CDF665C06E8F1CD7C63AB97BBB0B0A1ADB640"
        "4CF185A2172171625E53"
    )
    ciphertext_bytes = bytes.fromhex(ciphertext)