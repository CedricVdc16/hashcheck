#!/usr/bin/env python3
import argparse, hashlib, os, sys, json

def sha256_bytes(data: bytes) -> str:
    h = hashlib.sha256()
    h.update(data)
    return h.hexdigest()

def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    parser = argparse.ArgumentParser(description="hashcheck: SHA256 calc & verify")
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument("--text", help="texte en clair à hasher")
    g.add_argument("--file", help="chemin de fichier à hasher")
    parser.add_argument("--verify", help="SHA256 attendu pour vérification")
    parser.add_argument("--json", action="store_true", help="sortie JSON")
    args = parser.parse_args()

    if args.text is not None:
        digest = sha256_bytes(args.text.encode("utf-8"))
        source = {"type":"text","length":len(args.text)}
    else:
        if not os.path.exists(args.file):
            print(f"Erreur: fichier introuvable: {args.file}", file=sys.stderr)
            sys.exit(2)
        digest = sha256_file(args.file)
        source = {"type":"file","path":args.file,"size":os.path.getsize(args.file)}

    ok = None
    if args.verify:
        ok = (digest.lower() == args.verify.lower())

    if args.json:
        out = {"algo":"SHA256","digest":digest,"verify":ok,"source":source}
        print(json.dumps(out))
    else:
        print(f"SHA256: {digest}")
        if ok is not None:
            print("VERIFY:", "OK" if ok else "MISMATCH")
    sys.exit(0 if (ok is None or ok) else 1)

if __name__ == "__main__":
    main()
