import hashlib
import time

def sha256_hex(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_lines(path):
    lines = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if s:
                lines.append(s)
    return lines

def mutations(word):
    suffixes = ["", "1", "12", "123", "!", "2025"]
    variants = set()
    w = word.strip()
    if not w:
        return []
    variants.add(w)
    variants.add(w.upper())
    variants.add(w.lower())
    variants.add(w.capitalize())

    for base in [w, w.lower(), w.capitalize()]:
        for suf in suffixes:
            variants.add(f"{base}{suf}")
    return list(variants)

def crack_sha256(targets, words):
    cracked = {}
    for word in words:
        for guess in mutations(word):
            h = sha256_hex(guess)
            if h in targets and h not in cracked:
                cracked[h] = guess
    return cracked


def main():
    hashes = load_lines("hashes.txt")
    words = load_lines("wordlist.txt")
    targets = set(hashes)

    print(f"Loaded {len(hashes)} hashes, {len(words)} words")

    start = time.time()
    cracked = crack_sha256(targets, words)
    elapsed = time.time() - start

    print("\n=== Results ===")
    print(f"Cracked:   {len(cracked)} / {len(hashes)}")
    print(f"Uncracked: {len(hashes) - len(cracked)}")
    print(f"Time:      {elapsed:.3f}s\n")

    # print cracked pairs
    for h, plain in cracked.items():
        print(f"{h}  ->  {plain}")

    # list uncracked hashes
    if len(cracked) != len(hashes):
        print("\n=== Uncracked Hashes ===")
        for h in hashes:
            if h not in cracked:
                print(h)



if __name__ == "__main__":
    main()

