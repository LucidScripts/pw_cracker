# Password Cracker (Dictionary + Mutations)

This project is a small Python-based password analysis tool designed to demonstrate how dictionary-based password attacks work when hashes are used instead of plaintext. It focuses on clarity, correctness, and core programming concepts rather than performance or large-scale cracking.

The implementation is intentionally scoped and educational.

---

## Overview

The program:
- Loads a list of **SHA-256 hashed passwords**
- Loads a **wordlist** of candidate base words
- Generates common password mutations (case changes, numeric and symbol suffixes)
- Hashes each generated guess
- Compares hashes against the target set
- Reports cracked and uncracked hashes along with runtime statistics

This mirrors how basic password auditing tools operate at a conceptual level.

---

## Purpose

The goal of this project is to reinforce:
- Python fundamentals (functions, loops, data structures)
- Hash-based password verification
- Efficient lookup using sets and dictionaries
- Program flow and modular design

It also serves as a compact example of applying security concepts in code.

---

## How It Works

1. Read target hashes from `hashes.txt`
2. Read base words from `wordlist.txt`
3. Generate realistic variations for each word
4. Hash each candidate using SHA-256
5. Compare generated hashes against the target set
6. Record and display any successful matches

---

## Project Structure

pw_cracker/
├── cracker.py
├── hashes.txt
├── wordlist.txt
└── README.md

- `cracker.py` – core program logic
- `hashes.txt` – SHA-256 hashes to evaluate (one per line)
- `wordlist.txt` – base words used to generate guesses

---

## Usage

1. Populate `hashes.txt` with SHA-256 hashes
2. Populate `wordlist.txt` with candidate words
3. Run the script:

```bash
python cracker.py
