from binascii import hexlify

from cipher import caesar_cipher, generate_iv, des_cipher, des_cipher_decode
from histogram import save_histogram

def ex1():
    plaintext = """
    Plot
    Gandalf tricks Bilbo Baggins into hosting a party for Thorin Oakenshield and his band of twelve dwarves (Dwalin, Balin, Kili, Fili, Dori, Nori, Ori, Oin, Gloin, Bifur, Bofur, and Bombur), who go over their plans to reclaim their ancient home, Lonely Mountain, and its vast treasure from the dragon Smaug. Gandalf unveils Thror's map showing a secret door into the Mountain and proposes that dumbfounded Bilbo should serve as the expedition's "burglar". The dwarves ridicule the idea, but Bilbo, indignant, joins despite himself.
    The group travels into the wild. Gandalf saves the company from trolls and leads them to Rivendell, where Elrond reveals more secrets from the map. When they attempt to cross the Misty Mountains, they are caught by goblins and driven deep underground. Although Gandalf kills the goblin king and rescues them, Bilbo gets separated from the others as they flee the goblins. Lost in the goblin tunnels, he stumbles across a mysterious ring and then encounters Gollum, who engages him in a game, each posing a riddle until one of them cannot solve it. If Bilbo wins, Gollum will show him the way out of the tunnels, but if he fails, his life will be forfeit. With the help of the ring, which confers invisibility when worn, Bilbo escapes and rejoins the dwarves, improving his reputation with them. The goblins and Wargs give chase, but the company are saved by eagles. They rest in the house of the skin-changer Beorn.
    The company enters the dark forest of Mirkwood without Gandalf, who has other responsibilities. In Mirkwood, Bilbo first saves the dwarves from giant spiders and then from the dungeons of the Wood-elves. Nearing the Lonely Mountain, the travellers are welcomed by the human inhabitants of Lake-town, who hope the dwarves will fulfil prophecies of Smaug's demise. The expedition reaches the mountain and finds the secret door. The dwarves send a reluctant Bilbo inside to scout the dragon's lair. He steals a great cup and, while conversing with Smaug, spots a gap in the ancient dragon's armour. The enraged dragon, deducing that Lake-town has aided the intruders, flies off to destroy the town. A thrush overhears Bilbo's report of Smaug's vulnerability and tells a Lake-town resident named Bard. Smaug wreaks havoc on the town, until Bard shoots an arrow into the chink in Smaug's armour, killing the dragon.
    When the dwarves take possession of the mountain, Bilbo finds the Arkenstone, the most-treasured heirloom of Thorin's family, and hides it away. The Wood-elves and Lake-men request compensation for Lake-town's destruction and settlement of old claims on the treasure. When Thorin refuses to give them anything, they besiege the mountain. However, Thorin manages to send a message to his kinfolk in the Iron Hills and reinforces his position. Bilbo slips out and gives the Arkenstone to the besiegers, hoping to head off a war. When they offer the jewel to Thorin in exchange for treasure, Bilbo reveals how they obtained it. Thorin, furious at what he sees as betrayal, banishes Bilbo, and battle seems inevitable when Dain, Thorin's second cousin, arrives with an army of dwarf warriors.
    Gandalf reappears to warn all of an approaching army of goblins and Wargs. The dwarves, men and elves band together, but only with the timely arrival of the eagles and Beorn, who fights in his bear form and kills the goblin general, do they win the climactic Battle of Five Armies. Thorin is fatally wounded and reconciles with Bilbo before he dies.
    Bilbo accepts only a small portion of his share of the treasure, having no want or need for more, but still returns home a very wealthy hobbit roughly a year and a month after he first left. Years later, he writes the story of his adventures.
    """
    plaintext = plaintext.replace("\n", " ")

    save_histogram(plaintext, "histogram_plaintext.png")

    caesar_text = caesar_cipher(plaintext, shift=1)
    save_histogram(caesar_text, "histogram_caesar_cipher.png")

    key = b'12345678'
    iv = generate_iv()
    des_text = des_cipher("CBC", plaintext, key, iv)
    save_histogram(des_text, "histogram_des_cbc.png")

def ex2():
    plaintext = "Bob's salary is $25000--Tom's salary is $15000"
    key = bytes.fromhex("11 22 33 44 55 66 77 88".replace(" ", ""))
    iv = generate_iv()

    print("\n===== Testing DES ECB =====")
    encrypted_text, encrypted_blocks, r_encrypted_text, r_encrypted_blocks = des_cipher("ECB", plaintext, key)
    decrypted_text, decrypted_blocks = des_cipher_decode("ECB", encrypted_text, encrypted_blocks, key)
    r_decrypted_text, _ = des_cipher_decode("ECB", r_encrypted_text, r_encrypted_blocks, key)

    print(f"\nDES ECB - Encrypted text         (hex): {hexlify(encrypted_text).decode()}")
    print(  f"DES ECB - Encrypted text C1<->C4 (hex): {hexlify(r_encrypted_text).decode()}")

    print("\nDES ECB - Encrypted blocks (hex) / Decrypted blocks:")
    for i, (en_block, r_dec_block) in enumerate(zip(encrypted_blocks, decrypted_blocks), 1):
        print(f"C{i}: {hexlify(en_block).decode()} -> {r_dec_block}")

    print(f"\nDES ECB - Decrypted text        : {decrypted_text}")
    print(  f"DES ECB - Decrypted text C1<->C4: {r_decrypted_text}")

    print("\n===== Testing DES CBC =====")
    encrypted_text, encrypted_blocks, r_encrypted_text, r_encrypted_blocks = des_cipher("CBC", plaintext, key, iv)
    decrypted_text, decrypted_blocks = des_cipher_decode("CBC", encrypted_text, encrypted_blocks, key, iv)
    r_decrypted_text, _ = des_cipher_decode("CBC", r_encrypted_text, r_encrypted_blocks, key, iv)

    print(f"\nDES CBC - Encrypted text         (hex): {hexlify(encrypted_text).decode()}")
    print(  f"DES CBC - Encrypted text C1<->C4 (hex): {hexlify(r_encrypted_text).decode()}")

    print("\nDES CBC - Encrypted blocks (hex) / Decrypted blocks:")
    for i, (en_block, r_dec_block) in enumerate(zip(encrypted_blocks, decrypted_blocks), 1):
        print(f"C{i}: {hexlify(en_block).decode()} -> {r_dec_block}")

    print(f"\nDES CBC - Decrypted text        : {decrypted_text}")
    print(  f"DES CBC - Decrypted text C1<->C4: {r_decrypted_text}")

    print('\n')

def ex3():
    plaintext = "Bob's salary is $25000--Tom's salary is $15000"

