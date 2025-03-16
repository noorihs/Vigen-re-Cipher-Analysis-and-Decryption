# Vigen-re-Cipher-Analysis-and-Decryption

This project provides a set of Python tools for analyzing and decrypting text encrypted using the Vigenère cipher. It utilizes frequency analysis, Kasiski examination, and index of coincidence to determine the possible key length and recover the encryption key.

## Features

- **Index of Coincidence Calculation:** Determines the likelihood of a text being encrypted using a polyalphabetic cipher.
- **Kasiski Examination:** Identifies repeating sequences in the ciphertext to estimate key length.
- **Letter Frequency Analysis:** Uses frequency distribution of letters to guess the key.
- **Vigenère Cipher Decryption:** Recovers the original plaintext using the estimated key.

## Requirements

This script requires Python 3 and the following libraries:

- `collections`
- `itertools`
- `string`

## Installation

To use this tool, clone the repository and navigate to the project directory:

## Usage

1. **Run the script:**
   ```sh
   python VIGENERE_analysis.py
   ```

2. **Modify the `cipher_text` variable** inside the script to analyze a different encrypted message.

3. **Follow the output:** The script will display the estimated key length, probable key, and attempt to decrypt the message.

## Explanation of Methods

- **Index of Coincidence (IC):** Measures the probability that two randomly chosen letters from the ciphertext are the same.
- **Kasiski Examination:** Detects repeated substrings in the ciphertext and calculates the distances between them to infer the key length.
- **Frequency Analysis:** Assumes the most common letter in a ciphertext segment corresponds to 'E' in English, helping determine the key.
- **Decryption Function:** Uses the estimated key to decrypt the text back to readable plaintext.

## Example Output

```
Index of Coincidence (IC): 0.0432
Detected repeating sequences (Kasiski): ['XYZ', 'ABC']
Probable key lengths: [5, 10]
Estimated Key: "SECRET"
Decrypted text: "THIS IS A TEST MESSAGE"
```

