import string
from collections import Counter
from itertools import cycle

# Fréquences des lettres en français (pour comparer)
frequences_francaises = {
    'A': 8.2, 'B': 1.5, 'C': 3.3, 'D': 3.6, 'E': 17.8, 'F': 1.1, 'G': 1.2, 'H': 1.1, 'I': 7.3, 'J': 0.3,
    'K': 0.0, 'L': 5.7, 'M': 2.6, 'N': 7.1, 'O': 5.2, 'P': 3.0, 'Q': 0.9, 'R': 6.7, 'S': 7.9, 'T': 7.2,
    'U': 6.1, 'V': 1.8, 'W': 0.0, 'X': 0.4, 'Y': 0.3, 'Z': 0.1
}

# Fonction pour calculer l'Indice de Coïncidence (IC)
def indice_coincidence(text):
    N = len(text)
    freqs = Counter(text)
    IC = sum(f * (f - 1) for f in freqs.values()) / (N * (N - 1))
    
    print("\nFréquences des lettres dans le texte chiffré :")
    for letter, freq in sorted(freqs.items()):
        print(f"{letter}: {freq} occurrences", end=", ")
    
    return IC

# Fonction pour trouver les distances entre répétitions (Kasiski)
def kasiski_examination(text, min_length=3):
    sequences = {}
    for i in range(len(text) - min_length):
        seq = text[i:i + min_length]
        if seq in sequences:
            sequences[seq].append(i)
        else:
            sequences[seq] = [i]

    distances = []
    for seq, positions in sequences.items():
        if len(positions) > 1:
            for j in range(len(positions) - 1):
                distances.append(positions[j + 1] - positions[j])
    
    print("\nSéquences répétées détectées (Kasiski) :")
    for seq, positions in sequences.items():
        if len(positions) > 1:
            print(f"{seq} trouvé aux positions {positions}")
    
    return distances

# Fonction de déchiffrement Vigenère
def vigenere_decrypt(ciphertext, key):
    plaintext = []
    key_cycle = cycle(key)
    
    for c in ciphertext:
        shift = ord(next(key_cycle)) - ord('A')
        decrypted_char = chr(((ord(c) - ord('A') - shift) % 26) + ord('A'))
        plaintext.append(decrypted_char)
    
    return "".join(plaintext)

# Fonction pour analyser la fréquence des lettres et deviner la clé
def find_vigenere_key(cipher_text, key_length):
    key = ""
    
    print(f"\nAnalyse des fréquences pour une clé de longueur {key_length} :")
    
    for i in range(key_length):
        subtext = cipher_text[i::key_length]
        freqs = Counter(subtext)
        
        print(f"\n  ➡ Sous-texte {i+1} (taille {len(subtext)} caractères) : {subtext[:30]}...")
        
        most_common_letter, max_freq = freqs.most_common(1)[0]
        shift = (ord(most_common_letter) - ord('E')) % 26
        key += chr(ord('A') + shift)
        
        print(f"    - Lettre la plus fréquente : {most_common_letter} ({max_freq} occurrences)")
        print(f"    - Décalage estimé : {shift} → Lettre de la clé : {chr(ord('A') + shift)}")
    
    return key

# Texte chiffré donné
cipher_text = """entrez votre texte chiffré"""

# 1. Calcul de l'Indice de Coïncidence
IC = indice_coincidence(cipher_text)
print(f"\nIndice de Coïncidence (IC) : {IC:.4f}")

# 2. Analyse de Kasiski pour estimer la longueur de la clé
distances = kasiski_examination(cipher_text)

if distances:
    print(f"\nDistances entre répétitions (Kasiski) : {distances}")
    
    # Facteurs communs
    common_factors = Counter()
    for d in distances:
        for i in range(2, min(d, 20)):
            if d % i == 0:
                common_factors[i] += 1

    probable_lengths = [length for length, _ in common_factors.most_common(3)]
    print(f"\nLongueurs de clé probables : {probable_lengths}")

    # 3. Tester les longueurs de clé les plus probables
    for length in probable_lengths:
        print(f"\nEssai avec une clé de longueur : {length}")
        
        key_found = find_vigenere_key(cipher_text, length)
        print(f"\nClé estimée : {key_found}")

        # 4. Déchiffrer avec la clé trouvée
        decrypted_text = vigenere_decrypt(cipher_text, key_found)
        print("\nTexte déchiffré (500 premiers caractères) :")
        print(decrypted_text[:500])  # Affichage des 500 premiers caractères
else:
    print("\nAucune répétition détectée avec Kasiski.")
