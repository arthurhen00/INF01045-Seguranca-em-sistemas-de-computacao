# This has nothing to do with Valorant.
# I declare here all my hatred for Valorant,
# Riot, its players and community.

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from typing import Tuple, List

def aes_cipher(text: str, key: bytes) -> Tuple[bytes, List[bytes]]:
    cipher = AES.new(key, AES.MODE_ECB)
    padded_text = pad(text.encode("utf-8"), AES.block_size)
    encrypted = cipher.encrypt(padded_text)
    blocks = [encrypted[i:i+AES.block_size] for i in range(0, len(encrypted), AES.block_size)]
    return encrypted, blocks

def aes_cipher_decode(ciphertext: bytes, key: bytes) -> Tuple[bytes, List[bytes]]:
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    decrypted_blocks = [cipher.decrypt(ciphertext[i:i+AES.block_size])
                        for i in range(0, len(ciphertext), AES.block_size)]
    return decrypted, decrypted_blocks
