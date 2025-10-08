# 🧩 hashcheck

> **FR 🇫🇷** – Outil simple et léger pour calculer ou vérifier le **SHA256** d’un texte ou d’un fichier.  
> **EN 🇬🇧** – Lightweight CLI tool to compute or verify **SHA256** checksums for text or files.

![Docker Pulls](https://img.shields.io/docker/pulls/cedricvdc16/hashcheck)
![CI](https://github.com/CedricVdc16/hashcheck/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 🧠 Présentation | Overview

`hashcheck` est une petite application Python empaquetée dans une image Docker minimaliste.  
Elle permet de vérifier rapidement l’intégrité d’un texte ou d’un fichier, localement ou dans un pipeline CI/CD.

`hashcheck` is a small Python-based utility packed inside a minimal Docker image.  
It helps you quickly compute or verify file integrity in security or automation contexts.

---

## 🚀 Utilisation rapide | Quick usage

### 📝 Hasher une chaîne de texte

```bash
docker run --rm cedricvdc16/hashcheck:latest --text "hello"
```

**Résultat attendu :**
```
SHA256: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```

---

### 📁 Hasher un fichier local

```bash
docker run --rm -v "$PWD:/data" cedricvdc16/hashcheck:latest --file /data/monfichier.txt
```

---

### 🧩 Vérifier un hash connu

```bash
docker run --rm cedricvdc16/hashcheck:latest   --text "hello"   --verify 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```

**Résultat attendu :**
```
SHA256: 2cf24dba5f...
VERIFY: OK
```

---

### 💾 Exemple pratique : vérifier une image ISO Ubuntu

```bash
docker run --rm -v "$PWD:/data" cedricvdc16/hashcheck:latest   --file /data/ubuntu-25.10-beta-desktop-amd64.iso   --verify 0f8ddc6db21d3414d1611ff9cedf5dba0bc58a77c064e71930b3ecec295c6716
```

---

## ⚙️ Options disponibles | Command-line options

| Option | Description |
|--------|--------------|
| `--text "..."` | Hash d’un texte brut |
| `--file /chemin/fichier` | Hash d’un fichier local |
| `--verify <hash>` | Compare le résultat au hash fourni |
| `--json` | Sortie au format JSON |
| `--help` | Aide et options disponibles |

---

## 🛠️ Caractéristiques | Features

- 🐍 Basé sur **Python 3.12**
- 🔒 Utilise **SHA256** pour l’intégrité
- 📦 Image Docker légère (`python:3.12-slim`)
- 👷 Exécute le conteneur avec un utilisateur **non-root**
- 🧪 Tests automatisés via **pytest** et **GitHub Actions**
- 💡 Parfait pour les pipelines DevSecOps ou les vérifications locales

---

## 🧰 Exemple d’intégration CI/CD

```yaml
- name: Verify ISO integrity
  run: |
    docker run --rm -v "$PWD:/data" cedricvdc16/hashcheck:latest       --file /data/ubuntu.iso       --verify $(cat /data/SHA256SUMS | grep ubuntu.iso | cut -d ' ' -f1)
```

---

## 🧾 Licence

MIT License © [CedricVdc16](https://github.com/CedricVdc16)

---

## 🔗 Liens utiles | Useful links

- 🐙 [Source on GitHub](https://github.com/CedricVdc16/hashcheck)
- 🐳 [Docker Hub page](https://hub.docker.com/r/cedricvdc16/hashcheck)
- 📚 [SHA256 info (Wikipedia)](https://en.wikipedia.org/wiki/SHA-2)

---

## 👤 À propos de l’auteur | About the author

**Cedric Vdc**  

> “L’efficacité, c’est la simplicité bien pensée.”

---
